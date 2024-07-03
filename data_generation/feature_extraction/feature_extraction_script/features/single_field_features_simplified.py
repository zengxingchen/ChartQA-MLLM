import pandas as pd
import numpy as np
from scipy.stats import entropy, skew, kurtosis
from collections import OrderedDict


def extract_basic_features(dataframe):
    """
    提取给定DataFrame的每个列的基本特征。

    参数:
    dataframe: 输入的pandas DataFrame。

    返回:
    feature_results: 包含每列特征的字典。
    """
    feature_results = OrderedDict()

    for column in dataframe.columns:
        # 初始化该列的特征字典
        features = OrderedDict()
        col_data = dataframe[column].dropna()  # 去除NaN值

        # 检测数据类型
        if dataframe[column].dtype == 'bool' or np.unique(dataframe[column].dropna()).size <= 2:
            # 布尔或二元列
            features['true_ratio'] = np.mean(col_data)
        elif dataframe[column].dtype == 'object':
            # 分类数据
            features['unique_values'] = col_data.unique().size
            features['mode'] = col_data.mode()[0] if not col_data.mode().empty else None
        else:
            # 数值数据
            features['mean'] = np.mean(col_data)
            features['std'] = np.std(col_data)
            features['min'] = np.min(col_data)
            features['max'] = np.max(col_data)
            features['skewness'] = skew(col_data)
            features['kurtosis'] = kurtosis(col_data)

        # 将该列的特征添加到结果字典中
        feature_results[column] = features

    return feature_results


# 假设df是您从CSV加载的DataFrame
# df = pd.read_csv("your_csv_file.csv", nrows=5)
# 示例用的表格数据
data = {
    'mdu': [0, 2, 0, 0, 0, 0, 0, 1, 0, 0],
    'lc': [0] * 10,
    'idp': [True] * 10,
    'lpi': [6.907755] * 10,
    'fmde': [0] * 10,
    'physlim': [False] * 10
}
df = pd.DataFrame(data)

# 提取特征
features = extract_basic_features(df)
for col, feats in features.items():
    print(f"特征 - {col}: {feats}")
