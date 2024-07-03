import cv2
from base64 import b64encode, b64decode
import numpy as np
import os
import torch
import numpy as np
import random
import pandas as pd
import torchvision.models as models
import clip
from torch.utils.data import Dataset, DataLoader
from PIL import Image
import torchvision.transforms as transforms
from tqdm import tqdm

class ImageDataset(Dataset):
    def __init__(self, dataframe, parent_dir, transform=None):
        self.dataframe = dataframe
        self.parent_dir = parent_dir
        self.transform = transform

    def __len__(self):
        return len(self.dataframe)

    def __getitem__(self, idx):
        imgname  = self.dataframe[idx]
        image_path = f"{self.parent_dir}/{imgname}"
        return image_path
    
def read_image_as_base64(path):
    with open(path, 'rb') as image_file:
        return b64encode(image_file.read()).decode('utf-8')

def process_fn(sample):
    try:
        image_bytes = b64decode(sample)
        image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
        if image is None:
            raise ValueError("image decoded failed")
        return image
    except Exception as e:
        raise ValueError(f"image decoded failed: {e}")
    
def get_vector(image, bins=32):
    def normalization(data):
        _range = np.max(data) - np.min(data)
        return (data - np.min(data)) / _range
    red = cv2.calcHist([image], [2], None, [bins], [0, 256])
    green = cv2.calcHist([image], [1], None, [bins], [0, 256])
    blue = cv2.calcHist([image], [0], None, [bins], [0, 256])
    vector = np.concatenate([red, green, blue], axis=0)
    vector = vector.reshape(-1)
    normalized_vector = normalization(vector)
    return normalized_vector


# 使用示例数据集和变换
parent_dir = 'filtering/data'
data = pd.read_csv('filtering/all_data.csv')
neural_dataset = ImageDataset(data['img_path'], parent_dir=parent_dir)

# One-for-All Feature Extraction
all_features = []
all_imgnames = []
with torch.no_grad():
    for path_batch in tqdm(DataLoader(neural_dataset, batch_size=1024, shuffle=False, num_workers=8)):
        for path in tqdm(path_batch):
            try:
                img_base64 = read_image_as_base64(path)
                img_base64 = process_fn(img_base64)
                vector = get_vector(img_base64)
                all_features.append(vector)
            except:
                all_features.append(np.zeros(all_features[0].shape[0]))

all_features = np.concatenate(all_features, axis=0)
np.save('precomputed_features/existing-data-color-feature.npy', all_features)