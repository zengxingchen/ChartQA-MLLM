import os
import torch
import numpy as np
import random
import pandas as pd
import torchvision.models as models
import torchvision.transforms as transforms
import sys
os.chdir('~/projects/LLaVA')
current_path = os.getcwd()
sys.path.append(current_path + '/data-engine')

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
from utils import set_env
set_env(seed=1234)

import clip
from torch.utils.data import Dataset, DataLoader
from PIL import Image
from tqdm import tqdm


model_list = ['clip', 'resnet50', 'convnext']
model_name = model_list[2]
print(model_name)
# 加载CLIP模型和预处理

if model_name == 'clip':
    model, preprocess = clip.load("ViT-B/32", device=device)
elif model_name == 'resnet50':
    model = models.resnet50(pretrained=True).to(device)
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
elif model_name == 'convnext':
    model = models.convnext_large(pretrained=True).to(device)  # 你可以选择不同的ConvNeXt模型，例如 'convnext_tiny', 'convnext_small', 'convnext_base', 'convnext_large'
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
else:
    raise Exception


class TestDataset(Dataset):
    def __init__(self, dataframe, parent_dir, transform=None):
        self.dataframe = dataframe
        self.parent_dir = parent_dir
        self.transform = transform

    def __len__(self):
        return len(self.dataframe)

    def __getitem__(self, idx):
        imgname  = self.dataframe[idx]
        image = Image.open(f"{self.parent_dir}/{imgname}").convert('RGB')
        if self.transform:
            image = self.transform(image)
        return image, imgname

# 假设这是你要合并的三个Parquet文件的路径
file_paths = [
    './playground/data/unichart-pretrain-data/data/train-00000-of-00003-db40b2e51df9cb23.parquet',
    './playground/data/unichart-pretrain-data/data/train-00001-of-00003-176f88b6a51ec36d.parquet',
    './playground/data/unichart-pretrain-data/data/train-00002-of-00003-1e538839dce74b46.parquet'
]

# 读取每个Parquet文件并存储在列表中
dfs = [pd.read_parquet(file_path) for file_path in file_paths]

# 使用concat函数合并所有DataFrame
merged_df = pd.concat(dfs, ignore_index=True)
imgnames = merged_df['imgname'].unique()


# 使用示例数据集和变换
parent_dir = '~/projects/LLaVA/playground/data/unichart-pretrain-data/content/images'
neural_dataset = TestDataset(imgnames, parent_dir=parent_dir, transform=preprocess)

# One-for-All Feature Extraction
model.eval()
all_features = []
all_imgnames = []
with torch.no_grad():
    for images, imgnames in tqdm(DataLoader(neural_dataset, batch_size=1024, shuffle=False, num_workers=8)):
        images = images.to(device)
        if model_name == 'clip':
            features = model.encode_image(images).float()
        else:
            features = model(images)
        all_features.append(features.cpu().numpy())
        all_imgnames.extend(imgnames)

# 将特征和图像名称分别保存
all_features = np.concatenate(all_features, axis=0)
np.save(f'data-engine/precomputed_features/existing-data-{model_name}-feature.npy', all_features)

# 将图像名称保存为csv文件
# imgnames_df = pd.DataFrame({'imgname': all_imgnames})
# imgnames_df.to_csv('data-engine/precomputed_features/existing-data-imgnames.csv', index=False)