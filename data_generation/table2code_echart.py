import logging
import os
import re
import pandas as pd
from openai import OpenAI
import numpy as np
from prompt_rag import get_prompt_rag_echart

def read_html_file(file_path):
    """读取HTML文件内容。"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        logging.warning(f"Failed to read HTML file {file_path}: {e}")
        return ""

def generate_diversified_echart_code(args):
    client = OpenAI(base_url='',
           api_key='')

    seed_path_set, table_data_path, save_dir, chart_type= args

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
    prompt_messages = get_prompt_rag_echart(chart_type, table_data_records, seed_vl_codes)

    response = client.chat.completions.create(
       model="gpt-4o-mini",
        messages=prompt_messages
    )

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