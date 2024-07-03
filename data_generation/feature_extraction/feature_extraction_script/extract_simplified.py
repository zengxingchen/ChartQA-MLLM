#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Feature and Outcome Extraction
'''

import traceback
import pandas as pd

import os
import json
from time import time, strftime

import multiprocessing
from multiprocessing import Pool
from collections import OrderedDict, Counter
from pprint import pprint

from features.aggregate_pairwise_field_features import extract_aggregate_pairwise_field_features
from features.aggregate_single_field_features import extract_aggregate_single_field_features
from features.pairwise_field_features import extract_pairwise_field_features
from features.single_field_features import extract_single_field_features
from outcomes.chart_outcomes import extract_chart_outcomes
from outcomes.field_encoding_outcomes import extract_field_outcomes
from features.transform import supplement_features
from general_helpers import load_raw_data, clean_chunk, persist_features
import numpy as np
from pathlib import Path

MAX_FIELDS = 25
total_charts = 0
charts_without_data = 0
chart_loading_errors = 0
feature_extraction_errors = 0
charts_exceeding_max_fields = 0
CHUNK_SIZE = 1000


compute_features_config = {
    'single_field': True,
    'aggregate_single_field': True,

    'pairwise_field': True,
    'aggregate_pairwise_field': True,

    'field_level_features': True,
    'chart_outcomes': False,
    'field_outcomes': False,
    'supplement': False,
}


def get_first_n_column_names(csv_file_path, n=3):
    # 仅读取第一行来获取列名
    first_row = pd.read_csv(csv_file_path, nrows=0)
    # 获取前n列的列名
    column_names = first_row.columns[:n]
    return list(column_names)
def json_serializable(obj):
    """
    将不可序列化的对象转换为可序列化的类型。
    """
    if isinstance(obj, (np.int_, np.intc, np.intp, np.int8, np.int16, np.int32, np.int64,
                        np.uint8, np.uint16, np.uint32, np.uint64)):
        return int(obj)
    elif isinstance(obj, (np.float_, np.float16, np.float32, np.float64)):
        return float(obj)
    elif isinstance(obj, (np.ndarray,)):  # 处理NumPy数组
        return obj.tolist()
    elif isinstance(obj, (np.bool_,)):
        return bool(obj)  # 将numpy.bool_转换为标准Python布尔类型
    else:
        raise TypeError("类型 %s 不可序列化" % type(obj))


def extract_features_from_fields(
        fields, compute_features_config, chart_obj={}, fid=None):
    results = {}

    feature_names_by_type = {
        'basic': ['fid'],
        'single_field': [],
        'aggregate_single_field': [],
        'pairwise_field': [],
        'aggregate_pairwise_field': [],
        'chart_outcomes': [],
        'field_outcomes': []
    }

    df_feature_tuples_if_exists = OrderedDict({'fid': fid})
    df_feature_tuples = OrderedDict({'fid': fid})
    df_outcomes_tuples = OrderedDict()

    if compute_features_config['single_field'] or compute_features_config['field_level_features']:
        single_field_features, parsed_fields = extract_single_field_features(
            fields, fid, MAX_FIELDS=MAX_FIELDS)

        for i, field_features in enumerate(single_field_features):
            field_num = i + 1

            for field_feature_name, field_feature_value in field_features.items():
                if field_feature_name not in ['fid', 'field_id']:
                    field_feature_name_with_num = '{}_{}'.format(
                        field_feature_name, field_num)
                    if field_features['exists']:
                        df_feature_tuples_if_exists[field_feature_name_with_num] = field_feature_value

        if compute_features_config['field_level_features']:
            df_field_level_features = []
            for i, f in enumerate(single_field_features):
                if f['exists']:
                    if compute_features_config['supplement']:
                        f = supplement_features(f)
                    df_field_level_features.append(f)
                    feature_names_by_type['single_field'] = list(f.keys())
            results['df_field_level_features'] = df_field_level_features
        results['single_field_features'] = single_field_features

    if compute_features_config['aggregate_single_field']:
        aggregate_single_field_features = extract_aggregate_single_field_features(
            single_field_features
        )

        if compute_features_config['supplement']:
            aggregate_single_field_features = supplement_features(
                aggregate_single_field_features)

        for k, v in aggregate_single_field_features.items():
            df_feature_tuples[k] = v
            df_feature_tuples_if_exists[k] = v
            feature_names_by_type['aggregate_single_field'].append(k)

        results['aggregate_single_field_features'] = aggregate_single_field_features

    if compute_features_config['pairwise_field'] or compute_features_config['aggregate_pairwise_field']:
        pairwise_field_features = extract_pairwise_field_features(
            parsed_fields,
            single_field_features,
            fid,
            MAX_FIELDS=MAX_FIELDS
        )

        results['pairwise_field_features'] = pairwise_field_features

    if compute_features_config['aggregate_pairwise_field']:
        aggregate_pairwise_field_features = extract_aggregate_pairwise_field_features(
            pairwise_field_features)

        if compute_features_config['supplement']:
            aggregate_pairwise_field_features = supplement_features(
                aggregate_pairwise_field_features)

        for k, v in aggregate_pairwise_field_features.items():
            df_feature_tuples[k] = v
            df_feature_tuples_if_exists[k] = v
            feature_names_by_type['aggregate_pairwise_field'].append(k)

        results['aggregate_pairwise_field_features'] = aggregate_pairwise_field_features

    if compute_features_config['chart_outcomes']:
        outcomes = extract_chart_outcomes(chart_obj)
        for k, v in outcomes.items():
           df_outcomes_tuples[k] = v
           feature_names_by_type['chart_outcomes'].append(k)

    if compute_features_config['field_outcomes']:
        field_level_outcomes = extract_field_outcomes(chart_obj)
        feature_names_by_type['field_outcomes'] = list(
            list(field_level_outcomes)[0].keys())
        results['df_field_level_outcomes'] = field_level_outcomes

    results['df_feature_tuples'] = df_feature_tuples
    results['df_feature_tuples_if_exists'] = df_feature_tuples_if_exists
    results['df_outcomes_tuples'] = df_outcomes_tuples
    results['feature_names_by_type'] = feature_names_by_type

    return results


def read_csv_and_extract_features(csv_file_path, n_columns=10):
    df_preview = pd.read_csv(csv_file_path, nrows=0)  # 读取0行数据，只获取列名
    # if 'date' in df_preview.columns:
    #     # df = pd.read_csv(csv_file_path, parse_dates=['date'])
    #     # # 提取年、月、日
    #     # df['year'] = df['date'].dt.year
    #     # df['month'] = df['date'].dt.month
    #     # df['day'] = df['date'].dt.day
    # else:
    columns_to_use = get_first_n_column_names(csv_file_path, n=n_columns)
    df = pd.read_csv(csv_file_path, usecols=columns_to_use, nrows=100)


    fields = []
    for column in df.columns:
        if column not in ['rownames', 'date']:  # 忽略rownames和原始的date列
            fields.append({
                'name': column,
                'uid': column,  # 使用列名作为唯一标识符
                'order': np.nan,  # 如果顺序不重要，可以设置为NaN
                'data': df[column].tolist()
            })

    # 假设fid和其他参数已经设置
    fid = 'example_fid'

    # 调用你的函数
    all_field_features = extract_features_from_fields(fields, compute_features_config, fid=fid)

    # 这里你可以进一步处理all_field_features和parsed_fields，例如保存到文件或直接返回
    return all_field_features


def process_csv_files(csv_dir_path, json_dir_path):
    """
    读取指定文件夹中的所有CSV文件，并将每个文件的特征保存为同名的JSON文件到另一个文件夹中。
    如果JSON文件已经存在，则跳过该文件。
    """
    # 确保JSON输出目录存在
    Path(json_dir_path).mkdir(parents=True, exist_ok=True)

    # 获取所有CSV文件
    csv_files = [f for f in os.listdir(csv_dir_path) if f.endswith('.csv')]

    for csv_file in csv_files:
        csv_file_path = os.path.join(csv_dir_path, csv_file)
        json_file_name = os.path.splitext(csv_file)[0] + '.json'
        json_file_path = os.path.join(json_dir_path, json_file_name)

        print(csv_file)

        # 检查JSON文件是否已存在
        if os.path.exists(json_file_path):
            print(f"文件 {json_file_name} 已存在，跳过处理。")
            continue

        # 计算特征
        all_field_features = read_csv_and_extract_features(csv_file_path)



        # 保存特征到JSON文件
        with open(json_file_path, 'w') as json_file:
            json.dump(all_field_features, json_file, ensure_ascii=False, indent=4, default=json_serializable)

        print(f"特征已保存到JSON文件：{json_file_path}")


def main():
    # 指定CSV文件夹的路径和JSON输出文件夹的路径
    csv_dir_path = r'..\seed_1981+vega_official_json_csv_pair'
    json_dir_path = r"..\test"
    process_csv_files(csv_dir_path, json_dir_path)

if __name__ == '__main__':
    main()