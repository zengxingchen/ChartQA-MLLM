import os
import json
import pandas as pd
import numpy as np
from pathlib import Path
from collections import OrderedDict
from features.aggregate_pairwise_field_features import extract_aggregate_pairwise_field_features
from features.aggregate_single_field_features import extract_aggregate_single_field_features
from features.pairwise_field_features import extract_pairwise_field_features
from features.single_field_features import extract_single_field_features
from outcomes.chart_outcomes import extract_chart_outcomes
from outcomes.field_encoding_outcomes import extract_field_outcomes
from features.transform import supplement_features

MAX_FIELDS = 25
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
    first_row = pd.read_csv(csv_file_path, nrows=0)
    column_names = first_row.columns[:n]
    return list(column_names)

def json_serializable(obj):
    if isinstance(obj, (np.int_, np.intc, np.intp, np.int8, np.int16, np.int32, np.int64,
                        np.uint8, np.uint16, np.uint32, np.uint64)):
        return int(obj)
    elif isinstance(obj, (np.float_, np.float16, np.float32, np.float64)):
        return float(obj)
    elif isinstance(obj, (np.ndarray,)):
        return obj.tolist()
    elif isinstance(obj, (np.bool_,)):
        return bool(obj)
    else:
        raise TypeError("类型 %s 不可序列化" % type(obj))

def extract_features_from_fields(fields, compute_features_config, chart_obj={}, fid=None):
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
        single_field_features, parsed_fields = extract_single_field_features(fields, fid, MAX_FIELDS=MAX_FIELDS)
        for i, field_features in enumerate(single_field_features):
            field_num = i + 1
            for field_feature_name, field_feature_value in field_features.items():
                if field_feature_name not in ['fid', 'field_id']:
                    field_feature_name_with_num = '{}_{}'.format(field_feature_name, field_num)
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
        aggregate_single_field_features = extract_aggregate_single_field_features(single_field_features)
        if compute_features_config['supplement']:
            aggregate_single_field_features = supplement_features(aggregate_single_field_features)
        for k, v in aggregate_single_field_features.items():
            df_feature_tuples[k] = v
            df_feature_tuples_if_exists[k] = v
            feature_names_by_type['aggregate_single_field'].append(k)
        results['aggregate_single_field_features'] = aggregate_single_field_features

    if compute_features_config['pairwise_field'] or compute_features_config['aggregate_pairwise_field']:
        pairwise_field_features = extract_pairwise_field_features(parsed_fields, single_field_features, fid, MAX_FIELDS=MAX_FIELDS)
        results['pairwise_field_features'] = pairwise_field_features

    if compute_features_config['aggregate_pairwise_field']:
        aggregate_pairwise_field_features = extract_aggregate_pairwise_field_features(pairwise_field_features)
        if compute_features_config['supplement']:
            aggregate_pairwise_field_features = supplement_features(aggregate_pairwise_field_features)
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
        feature_names_by_type['field_outcomes'] = list(list(field_level_outcomes)[0].keys())
        results['df_field_level_outcomes'] = field_level_outcomes

    results['df_feature_tuples'] = df_feature_tuples
    results['df_feature_tuples_if_exists'] = df_feature_tuples_if_exists
    results['df_outcomes_tuples'] = df_outcomes_tuples
    results['feature_names_by_type'] = feature_names_by_type

    return results

def read_csv_and_extract_features(csv_file_path, n_columns=10):
    if os.stat(csv_file_path).st_size == 0:
        print(f"File {csv_file_path} is empty, skipping.")
        return None

    try:
        df_preview = pd.read_csv(csv_file_path, nrows=0)
    except pd.errors.EmptyDataError:
        print(f"No columns to parse from file {csv_file_path}, skipping.")
        return None

    columns_to_use = get_first_n_column_names(csv_file_path, n=n_columns)
    df = pd.read_csv(csv_file_path, usecols=columns_to_use, nrows=100)
    fields = []
    for column in df.columns:
        if column not in ['rownames', 'date']:
            fields.append({
                'name': column,
                'uid': column,
                'order': np.nan,
                'data': df[column].tolist()
            })
    fid = 'example_fid'
    all_field_features = extract_features_from_fields(fields, compute_features_config, fid=fid)
    return all_field_features

def process_csv_files(csv_dir_path, feature_dir_path):
    Path(feature_dir_path).mkdir(parents=True, exist_ok=True)
    csv_files = [f for f in os.listdir(csv_dir_path) if f.endswith('.csv')]
    for csv_file in csv_files:
        csv_file_path = os.path.join(csv_dir_path, csv_file)
        feature_file_name = os.path.splitext(csv_file)[0] + '.json'
        feature_file_path = os.path.join(feature_dir_path, feature_file_name)
        print(f"Processing {csv_file}")
        if os.path.exists(feature_file_path):
            print(f"文件 {feature_file_name} 已存在，跳过处理。")
            continue
        all_field_features = read_csv_and_extract_features(csv_file_path)
        if all_field_features is None:
            continue
        with open(feature_file_path, 'w') as feature_file:
            json.dump(all_field_features, feature_file, ensure_ascii=False, indent=4, default=json_serializable)
        print(f"特征已保存到JSON文件：{feature_file_path}")

def main():
    base_dir_path = r'..\..\diverse_scripts\seaborn_generation'
    for sub_dir in os.listdir(base_dir_path):
        sub_dir_path = os.path.join(base_dir_path, sub_dir)
        if os.path.isdir(sub_dir_path):
            table_dir_path = os.path.join(sub_dir_path, 'table')
            seed_table_dir_path = os.path.join(sub_dir_path, 'seed', 'table')
            if os.path.exists(table_dir_path):
                feature_dir_path = os.path.join(sub_dir_path, 'feature')
                process_csv_files(table_dir_path, feature_dir_path)
            if os.path.exists(seed_table_dir_path):
                seed_feature_dir_path = os.path.join(sub_dir_path, 'seed', 'feature')
                process_csv_files(seed_table_dir_path, seed_feature_dir_path)

if __name__ == '__main__':
    main()
