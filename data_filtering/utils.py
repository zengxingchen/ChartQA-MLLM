import torch
import torch.nn as nn
import torch.nn.functional as F
import os
import random
import numpy as np
from torch.utils.data import Dataset

class FocalLoss(nn.Module):
    def __init__(self, alpha=None, gamma=2, reduction='mean'):
        super(FocalLoss, self).__init__()
        self.alpha = alpha
        self.gamma = gamma
        self.reduction = reduction

    def forward(self, inputs, targets):
        # 计算基本的交叉熵损失
        BCE_loss = F.cross_entropy(inputs, targets, reduction='none')
        # 计算概率 pt
        pt = torch.exp(-BCE_loss)
        # 计算 Focal Loss
        F_loss = (1 - pt) ** self.gamma * BCE_loss

        # 如果设置了 alpha，调整 Focal Loss
        if self.alpha is not None:
            at = self.alpha[targets]
            F_loss = at * F_loss

        # 选择 reduction 方法
        if self.reduction == 'mean':
            return torch.mean(F_loss)
        elif self.reduction == 'sum':
            return torch.sum(F_loss)
        else:
            return F_loss
        
def set_env(seed):
    os.environ['CUDA_VISIBLE_DEVICES'] = "0"
    os.environ['PYTHONHASHSEED'] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.benchmark = False  # find fittest convolution
    torch.backends.cudnn.deterministic = True  # keep experiment result stable
  
    
# 数据集定义
class ChartFeatureDataset(Dataset):
    def __init__(self, dataframe, clip_features, feature_column_name):
        self.dataframe = dataframe
        self.clip_features = clip_features
        self.feature_column_name = feature_column_name
        self.num_classes = len(self.dataframe[feature_column_name].unique())

    def __len__(self):
        return len(self.dataframe)

    def __getitem__(self, idx):
        row = self.dataframe.iloc[idx]
        feature = self.clip_features[idx]
        label = int(row[self.feature_column_name])
        if label > self.num_classes:
            label = self.num_classes - 1
        return feature, label
    
class UniChartFeatureDataset(Dataset):
    def __init__(self, imgnames, clip_features):
        self.imgnames = imgnames
        self.clip_features = clip_features
        assert len(self.imgnames) == len(self.clip_features)
        
    def __len__(self):
        return len(self.imgnames)
    
    def __getitem__(self, idx):
        feature = self.clip_features[idx]
        imgnames = self.imgnames[idx]
        return feature, imgnames
        
    
    
        
    
        