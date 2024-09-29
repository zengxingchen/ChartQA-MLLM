import os
import json
import re
import pandas as pd
from openai import OpenAI
import csv
from prompt_rag import get_prompt_rag_vega


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
    client = OpenAI(base_url='',
        api_key='')
    seed_path_set, table_data_path, save_dir, chart_type = args


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
    prompt_messages = get_prompt_rag_vega(chart_type, table_data_records, seed_vl_code1,seed_vl_code2,seed_vl_code3)

    response = client.chat.completions.create(

       model="gpt-4o-mini",
        messages=prompt_messages
    )
    # print(response)
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