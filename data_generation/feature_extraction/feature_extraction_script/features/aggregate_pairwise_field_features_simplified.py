import numpy as np
import pandas as pd
from collections import OrderedDict
from scipy.stats import entropy

# 假设c_aggregation_functions和q_aggregation_functions与之前一样定义
c_aggregation_functions = ['num', 'has', 'only_one', 'all', 'percentage']
q_aggregation_functions = ['mean', 'var', 'std', 'avg_abs_dev', 'med_abs_dev', 'coeff_var', 'min', 'max', 'range', 'normalized_range']

def aggregate_boolean_features(values):
    """计算布尔型特征的聚合值。"""
    true_count = np.sum(values)
    return {
        'num': len(values),
        'has': np.any(values),
        'only_one': true_count == 1,
        'all': np.all(values),
        'percentage': true_count / len(values) if len(values) > 0 else None
    }

def aggregate_numeric_features(values):
    """计算数值型特征的聚合值。"""
    values = np.array(values)
    mean = np.mean(values)
    return {
        'mean': mean,
        'var': np.var(values),
        'std': np.std(values),
        'avg_abs_dev': np.mean(np.abs(values - mean)),
        'med_abs_dev': np.median(np.abs(values - np.median(values))),
        'coeff_var': np.std(values) / mean if mean else None,
        'min': np.min(values),
        'max': np.max(values),
        'range': np.ptp(values),
        'normalized_range': np.ptp(values) / mean if mean else None
    }

def extract_aggregate_pairwise_field_features(pairwise_field_features):
    final_field_features = OrderedDict()
    # 假设pairwise_field_features是一个包含所有成对字段特征字典的列表

    for feature_dict in pairwise_field_features:
        for feature_name, feature_value in feature_dict.items():
            if isinstance(feature_value, bool):
                aggregated = aggregate_boolean_features([feature_value])
                for agg_func, agg_value in aggregated.items():
                    final_field_features[f"{feature_name}-{agg_func}"] = agg_value
            elif np.issubdtype(type(feature_value), np.number):
                aggregated = aggregate_numeric_features([feature_value])
                for agg_func, agg_value in aggregated.items():
                    final_field_features[f"{feature_name}-{agg_func}"] = agg_value

    return final_field_features

# 示例使用，假设pairwise_field_features已经填充
# pairwise_field_features = [...]
# features = extract_aggregate_pairwise_field_features(pairwise_field_features)
# print(features)
