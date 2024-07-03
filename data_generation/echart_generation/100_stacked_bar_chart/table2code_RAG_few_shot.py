import logging
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

def read_html_file(file_path):
    """读取HTML文件内容。"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        logging.warning(f"Failed to read HTML file {file_path}: {e}")
        return ""

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


def generate_diversified_vega_lite_code(args):
    #client = OpenAI(base_url='',
    #        api_key='')

    client = OpenAI(base_url='',
        api_key='')
    
    # seed_path, table_data_path, save_dir = args
    seed_path_set, table_data_path, save_dir = args


    seed_vl_codes = []
    for seed_path in seed_path_set:
        try:
            seed_vl_code = read_html_file(seed_path)
        
            seed_vl_codes.append(seed_vl_code)
        except:
            seed_vl_codes.append({})

    # 确保seed_vl_codes至少有三个元素
    while len(seed_vl_codes) < 3:
        seed_vl_codes.append({})

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
    filename = f"{filename_without_ext}.html"
    print('going to process: ' + filename)

    # Check if the file already exists in the save directory
    diversified_json_path = os.path.join(save_dir, filename)
    if os.path.exists(diversified_json_path):
        print(f"File {filename} already exists. Skipping...")
        return

    # Constructing the prompt for GPT-4 to diversify the given Vega-Lite code
    prompt_messages = [
        {"role": "system", "content": "You are a highly intelligent AI familiar with data visualization and echart."},
        {"role": "user", "content": " Here is some chart table data:" + str(table_data_records) + "and examples of echart code that you can refer to the visual encoding: " + seed_vl_codes[0] + seed_vl_codes[1]  + seed_vl_codes[2]  +
         " Please generate a diversified echart code of a 100 percentage stacked bar chart based on the given table data and examples, use as diversified visual encoding in the example as possible.\
           You should give code with all detail and don's miss any data points.\
           you only need to generate code start from 'var dom = document.getElementById('container');' and  end at 'if (option && typeof option === 'object') myChart.setOption(option);', make sure you include these two in your code\
            Include the code with ``` ``` format."}
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
        if vega_lite_code.startswith('html'):
            vega_lite_code = vega_lite_code.lstrip('html')
        if vega_lite_code.startswith('json'):
            vega_lite_code = vega_lite_code.lstrip('json')
        if vega_lite_code.startswith('javascript'):
            vega_lite_code = vega_lite_code.lstrip('javascript')
        # vega_lite_code = json.loads(vega_lite_code)
        echart_code = vega_lite_code

        html_content = f'''<!DOCTYPE html>
        <html lang="en" style="height: 100%">
        <head>
        <meta charset="utf-8">
        <title>ECharts 100% Stacked Bar Chart</title>
        </head>
        <body style="height: 100%; margin: 0">
        <div id="container" style="height: 100%"></div>

        <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/echarts/dist/echarts.min.js"></script>

        <script type="text/javascript">

            {echart_code}

            window.addEventListener('resize', myChart.resize);
        </script>
        </body>
        </html>'''



        # Save the diversified Vega-Lite code as a JSON file
        diversified_json_path = os.path.join(save_dir, f"{filename}")
        with open(diversified_json_path, 'w', encoding='utf-8') as file:
            file.write(html_content)
        print(f'Saved diversified python code to {diversified_json_path}')
    except Exception as e:
        print(f"Failed to generate diversified code for {filename}: {e}")


def main(data_table_dir, seed_dir, save_dir, max_workers):
    os.makedirs(save_dir, exist_ok=True)

    csv_file_paths = [os.path.join(data_table_dir, f) for f in os.listdir(data_table_dir) if f.endswith('.csv')]
    precomputed_json_path = r"..\..\vega-lite_generation\100_stacked_bar_chart\similarity_record.json"
    closest_features_info = load_closest_features_info(precomputed_json_path)
    all_json_files = [os.path.join(seed_dir, f) for f in os.listdir(seed_dir) if f.endswith('.json')]
    if len(all_json_files) > 3:
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
    else:
        args_list = []
        for csv_file_path in csv_file_paths[:]:
            print('Processing file:', csv_file_path)
            target_feature_name = os.path.basename(csv_file_path).replace('.csv', '.json')
            closest_json_files = all_json_files
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
