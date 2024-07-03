import numpy as np
import pandas as pd
from scipy.stats import pearsonr, ks_2samp, chi2_contingency, f_oneway
from collections import OrderedDict

def calculate_overlap(a, b):
    """计算两组数据的重叠部分的比例。"""
    set_a, set_b = set(a), set(b)
    intersection_len = len(set_a.intersection(set_b))
    smallest_set_len = min(len(set_a), len(set_b))
    if smallest_set_len == 0:
        return False, 0
    return True, intersection_len / smallest_set_len

def get_general_pairwise_features(col_a, col_b):
    """计算两个列的一般特征。"""
    r = OrderedDict()
    num_identical_elements = np.sum(col_a == col_b)
    unique_a, unique_b = set(col_a.unique()), set(col_b.unique())
    shared_unique_elements = unique_a.intersection(unique_b)

    r['has_shared_elements'] = num_identical_elements > 0
    r['num_shared_elements'] = num_identical_elements
    r['percent_shared_elements'] = num_identical_elements / len(col_a)
    r['identical'] = np.array_equal(col_a, col_b)
    r['has_shared_unique_elements'] = len(shared_unique_elements) > 0
    r['num_shared_unique_elements'] = len(shared_unique_elements)
    r['percent_shared_unique_elements'] = len(shared_unique_elements) / max(len(unique_a), len(unique_b))
    r['identical_unique'] = unique_a == unique_b
    return r

def get_statistical_pairwise_features(col_a, col_b, MAX_GROUPS=50):
    """计算两个列的统计学特征。"""
    r = OrderedDict()
    if col_a.dtype == 'float64' and col_b.dtype == 'float64':
        correlation_value, correlation_p = pearsonr(col_a, col_b)
        overlap_exists, overlap_percent = calculate_overlap(col_a, col_b)
        r['correlation_value'] = correlation_value
        r['correlation_p'] = correlation_p
        r['correlation_significant_005'] = correlation_p < 0.05
        r['overlap_exists'] = overlap_exists
        r['overlap_percent'] = overlap_percent
    elif col_a.dtype == 'O' and col_b.dtype == 'O':
        if len(col_a.unique()) <= MAX_GROUPS and len(col_b.unique()) <= MAX_GROUPS:
            chi2_statistic, chi2_p, _, _ = chi2_contingency(pd.crosstab(col_a, col_b))
            r['chi2_statistic'] = chi2_statistic
            r['chi2_p'] = chi2_p
            r['chi2_significant_005'] = chi2_p < 0.05
    return r

def get_name_pairwise_features(name_a, name_b):
    """计算两个名称的特征，例如编辑距离。"""
    r = OrderedDict()
    edit_distance_value = len(set(name_a).symmetric_difference(set(name_b)))
    r['edit_distance'] = edit_distance_value
    r['normalized_edit_distance'] = edit_distance_value / max(len(name_a), len(name_b))
    shared_words = set(name_a.split()).intersection(name_b.split())
    r['has_shared_words'] = len(shared_words) > 0
    r['num_shared_words'] = len(shared_words)
    r['percent_shared_words'] = len(shared_words) / max(len(name_a.split()), len(name_b.split()))
    return r
