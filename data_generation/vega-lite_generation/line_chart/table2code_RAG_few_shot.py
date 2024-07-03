import os
import json
import re
import argparse
import pandas as pd
from openai import OpenAI
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import requests
import io
import random
import numpy as np
import glob
import csv


def load_closest_features_info(json_file_path):
    """从JSON文件中加载预先计算的最近三个feature文件的信息。"""
    with open(json_file_path, 'r') as f:
        closest_features_info = json.load(f)
    return closest_features_info

def find_closest_features_from_precomputed(closest_features_info, target_feature_name):
    """根据目标feature文件名从预先计算的信息中找到最近的三个feature文件名。"""
    # 从加载的信息（字典）中获取目标特征文件名对应的值（最近的三个文件名）
    closest_features = closest_features_info.get(target_feature_name, [])
    return closest_features

def remove_data_property(vl_code):
    """
    Removes the 'data' property from the Vega-Lite specification.
    """
    if 'data' in vl_code:
        vl_code['data'] = ''
    if 'datasets' in vl_code:
        vl_code['datasets'] = ''
    return vl_code

def generate_diversified_vega_lite_code(args):
    #client = OpenAI(base_url='',
    #        api_key='')

    client = OpenAI(base_url='',
        api_key='')
    
    # seed_path, table_data_path, save_dir = args
    seed_path_set, table_data_path, save_dir = args


    try:
        with open(seed_path_set[0], 'r') as json_file:
            seed_vl_code1 = json.load(json_file)
        seed_vl_code1 = remove_data_property(seed_vl_code1)
        with open(seed_path_set[1], 'r') as json_file:
            seed_vl_code2 = json.load(json_file)
        seed_vl_code2 = remove_data_property(seed_vl_code2)
        with open(seed_path_set[2], 'r') as json_file:
            seed_vl_code3 = json.load(json_file)
        seed_vl_code3 = remove_data_property(seed_vl_code3)
        with open(seed_path_set[3], 'r') as json_file:
            seed_vl_code4 = json.load(json_file)
        seed_vl_code4 = remove_data_property(seed_vl_code4)

    except:
        print('read seed vega-lite code fail in: ' + 'seed_path')
        return

    try:
        # Read the CSV file and limit it to the first 50 rows if it has more
        table_data = pd.read_csv(table_data_path, nrows=15)
        table_data_records = table_data.to_dict(orient='records')
        table_data_in_json = table_data.to_json(orient='records')
    except Exception as e:
        print('read table data fail in: ' + table_data_path)
        print('Error:', e)
        return

    filename = os.path.basename(table_data_path)
    # Use the base name of the seed_path to derive the filename for the JSON
    filename_without_ext = os.path.splitext(os.path.basename(filename))[0]
    filename = f"{filename_without_ext}.json"
    print('going to process: ' + filename)

    # Check if the file already exists in the save directory
    diversified_json_path = os.path.join(save_dir, filename)
    if os.path.exists(diversified_json_path):
        print(f"File {filename} already exists. Skipping...")
        return

    # Constructing the prompt for GPT-4 to diversify the given Vega-Lite code
    prompt_messages = [
        {"role": "system", "content": "You are a highly intelligent AI familiar with data visualization and Vega-Lite."},
        {"role": "user", "content": " Here is some chart table data:" + str(table_data_records) + "and examples of vega-lite code that you can refer to the visual encoding: " + json.dumps(seed_vl_code1) + json.dumps(seed_vl_code2)  + json.dumps(seed_vl_code3)  +
         " Please generate a diversified Vega-Lite code of a line chart based on the given table data and examples, use as diversified visual encoding in the example as possible.\
           You should give code with all detail and don's miss any data points.\
            It is really important that do not miss the ''field'' assignment of x or y axis! After generating the code, you must check that the data fields of x and y axis are correctly bound to the corresponding axes, if not, complement the field! \
            Include the code with ```json ``` format."}
    ]

    response = client.chat.completions.create(
       # model="gpt-3.5-turbo-16k",
       model="gpt-4",
        messages=prompt_messages
    )
    print(response)
    try:
        # Attempt to extract the Vega-Lite code from the response
        assistant_reply = response.choices[0].message.content

        vega_lite_code_blocks = re.findall(
            r'```(.*?)```', assistant_reply, re.DOTALL)

        assert vega_lite_code_blocks[0] != ''

        vega_lite_code = vega_lite_code_blocks[0].strip()
        if vega_lite_code.startswith('json'):
            vega_lite_code = vega_lite_code.lstrip('json')

        json_data_value = []
        reader = csv.DictReader(table_data)
        # 遍历CSV中的每一行
        for row in reader:
            # 将每个值尝试转换为整数，如果失败，则保留为原始字符串
            converted_row = {key: (int(value) if value.isdigit() else value) for key, value in row.items()}
            json_data_value.append(converted_row)
        # check the replace the json_data_value with data value in vega_lite_code


        vega_lite_code = json.loads(vega_lite_code)

        # Save the diversified Vega-Lite code as a JSON file
        diversified_json_path = os.path.join(save_dir, f"{filename}")
        print(diversified_json_path)
        with open(diversified_json_path, 'w') as json_file:
            json.dump(vega_lite_code, json_file, indent=4)
        print(f'Saved diversified Vega-Lite code to {diversified_json_path}')
    except Exception as e:
        print(f"Failed to generate diversified code for {filename}: {e}")


def main(data_table_dir, seed_dir, save_dir, max_workers):
    os.makedirs(save_dir, exist_ok=True)

    csv_file_paths = [os.path.join(data_table_dir, f) for f in os.listdir(data_table_dir) if f.endswith('.csv')]
    precomputed_json_path = r"similarity_record.json"
    closest_features_info = load_closest_features_info(precomputed_json_path)
    all_json_files = [os.path.join(seed_dir, f) for f in os.listdir(seed_dir) if f.endswith('.json')]

    args_list = []
    for csv_file_path in csv_file_paths[:]:
        print('Processing file:', csv_file_path)
        target_feature_name = os.path.basename(csv_file_path).replace('.csv', '.json')
        closest_feature_files = find_closest_features_from_precomputed(closest_features_info, target_feature_name)
        closest_json_files = [os.path.join(seed_dir, feature_file) for feature_file in closest_feature_files]
        random_json_file = random.choice(all_json_files)
        random_json_file_2 = random.choice(all_json_files)
        closest_json_files.append(random_json_file)
        closest_json_files.append(random_json_file_2)
        args_list.append((closest_json_files, csv_file_path, save_dir))

    # 使用 ThreadPoolExecutor 替换 Pool
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 使用 submit 方法提交任务
        futures = [executor.submit(generate_diversified_vega_lite_code, args) for args in args_list]
        # 使用 as_completed 方法等待所有任务完成
        for future in tqdm(as_completed(futures), total=len(args_list), desc='Processing files'):
            try:
                # 获取任务结果，如果有异常会抛出
                future.result()
            except Exception as exc:
                print(f'Generated exception: {exc}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate Vega-Lite code from CSV data using OpenAI API.")
    parser.add_argument('--data_table_dir', type=str, default=r"table",
                        help='Directory path containing CSV tables')

    parser.add_argument('--seed_dir', type=str, default=r"seed\code",
                        help='Directory path containing CSV tables')

    parser.add_argument('--save_dir', type=str, default=r'expanded_seed',
                        help='Directory path to save generated Vega-Lite JSON files')

    parser.add_argument('--max_workers', type=int, default=1000,
                        help='Maximum number of processes to use for concurrent requests. Defaults to number of CPUs')
    parser.add_argument('--multiprocessing', type=bool, default=True)

    args = parser.parse_args()
    os.makedirs(args.save_dir, exist_ok=True)
    main(data_table_dir=args.data_table_dir, seed_dir=args.seed_dir, save_dir=args.save_dir,
         max_workers=args.max_workers)
