import os
import json
import re
from openai import OpenAI
import csv
import random

import pandas as pd
from prompt_python import get_prompt_python


topics_pool = [
    "Future Technologies & Society", "Art & Design", "Science & Nature",
    "Health & Psychology", "Culture & Society", "Economics & Finance",
    "Education & Learning", "Entertainment & Leisure", "Environment & Climate Change",
    "Food & Nutrition", "Travel & Adventure", "Fashion & Beauty",
    "Politics & Governance", "Sports & Fitness", "History & Archaeology",
    "Philosophy & Ethics", "Music & Performing Arts", "Literature & Writing",
    "Business & Entrepreneurship", "Astronomy & Space Exploration"
]

def load_matplotlib_code(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def extract_and_save_data(plot_code, csv_path):
    """
    Extracts data from the Matplotlib code and saves it to a CSV file.
    """
    # Assuming the data is provided in the Matplotlib code as a list of dictionaries
    data_match = re.search(r'data\s*=\s*(\[[^\]]+\])', plot_code)
    if data_match:
        data_str = data_match.group(1)
        data = json.loads(data_str.replace("'", '"'))
        df = pd.DataFrame(data)
        df.to_csv(csv_path, index=False)
        print(f'Saved data to {csv_path}')
    else:
        print(f"No data found in the Matplotlib code for {csv_path}")

def generate_diversified_python_code(file_path, save_dir, chart_type, method):
    client = OpenAI(base_url='', 
                    api_key='')

    original_vl_code = load_matplotlib_code(file_path)

    filename = os.path.basename(file_path)

    random.shuffle(topics_pool)
    # Constructing the prompt for GPT-4 to diversify the given Vega-Lite code
    # 6. Add text labels (or remove) in reasonable positions, but avoid give text label in stacked bar to prevent clutter.\
    prompt_messages = get_prompt_python(method, chart_type, original_vl_code, topics_pool)

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
        # code for table
        table = vega_lite_code_blocks[0]
        print(table)
        # csv_data = re.findall(r'```(.*?)```', table, re.DOTALL)
        csv_data = table
        if csv_data and isinstance(csv_data[0], str):
            # csv_data = csv_data[0].strip()
            if csv_data.startswith('json'):
                csv_data = csv_data.lstrip('json')
            if csv_data.startswith('csv'):
                csv_data = csv_data.lstrip('csv')
            if csv_data.startswith('plaintext'):
                csv_data = csv_data.lstrip('plaintext')
            csv_lines = csv_data.split('\n')

            # 提取实体数量
            filename_pre = filename.split('.')[0]
            file_path = os.path.join(save_dir, f'_4_{filename_pre}.csv')

            with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                for line in csv_lines:
                    writer.writerow(line.replace('"', '').split(','))

            print(f"table data saved to {file_path}")
        # code for code
        vega_lite_code = vega_lite_code_blocks[1].strip()


        if vega_lite_code.startswith('python'):
            vega_lite_code = vega_lite_code.lstrip('python')
        if vega_lite_code.startswith('json'):
            vega_lite_code = vega_lite_code.lstrip('json')
        # vega_lite_code = json.loads(vega_lite_code)

        # Save the diversified Vega-Lite code as a JSON file
        diversified_json_path = os.path.join(save_dir, f"_4_{filename}")
        with open(diversified_json_path, 'w', encoding='utf-8') as file:
            file.write(vega_lite_code)
        print(f'Saved diversified python code to {diversified_json_path}')
    except Exception as e:
        print(f"Failed to generate diversified code for {filename}: {e}")



