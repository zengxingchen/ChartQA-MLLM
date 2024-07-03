import numpy as np
import pandas as pd
from scipy.stats import entropy
from collections import OrderedDict

def aggregate_boolean_features(values):
    """计算布尔型特征的聚合值。"""
    true_count = np.sum(values)
    false_count = len(values) - true_count
    return {
        'num': len(values),
        'has': true_count > 0,
        'only_one': true_count == 1,
        'all': true_count == len(values),
        'percentage': true_count / len(values) if len(values) > 0 else None
    }

def aggregate_numeric_features(values):
    """计算数值型特征的聚合值。"""
    values = np.array(values)
    mean = np.mean(values)
    std = np.std(values)
    min_val = np.min(values)
    max_val = np.max(values)
    range_val = max_val - min_val
    normalized_range = range_val / mean if mean else None
    return {
        'mean': mean,
        'var': np.var(values),
        'std': std,
        'avg_abs_dev': np.mean(np.abs(values - mean)),
        'med_abs_dev': np.median(np.abs(values - np.median(values))),
        'coeff_var': std / mean if mean else None,
        'min': min_val,
        'max': max_val,
        'range': range_val,
        'normalized_range': normalized_range
    }

def aggregate_features(df):
    """聚合DataFrame中的特征。"""
    aggregated_features = OrderedDict()
    for column in df.columns:
        data = df[column].dropna()
        if data.dtype == 'bool':
            aggregated_features.update({
                f'{column}-{key}': val for key, val in aggregate_boolean_features(data).items()
            })
        elif np.issubdtype(data.dtype, np.number):
            aggregated_features.update({
                f'{column}-{key}': val for key, val in aggregate_numeric_features(data).items()
            })
        if data.dtype == 'object' or data.dtype == 'bool':
            # 对于分类数据和布尔数据计算熵
            _, counts = np.unique(data, return_counts=True)
            aggregated_features[f'{column}-entropy'] = entropy(counts)
    return aggregated_features
