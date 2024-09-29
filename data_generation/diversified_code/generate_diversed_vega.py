import os
import json
import re
import pandas as pd
from openai import OpenAI
import random
from prompt_vega import get_prompt_vega

topics_pool = [
    "Future Technologies & Society", "Art & Design", "Science & Nature",
    "Health & Psychology", "Culture & Society", "Economics & Finance",
    "Education & Learning", "Entertainment & Leisure", "Environment & Climate Change",
    "Food & Nutrition", "Travel & Adventure", "Fashion & Beauty",
    "Politics & Governance", "Sports & Fitness", "History & Archaeology",
    "Philosophy & Ethics", "Music & Performing Arts", "Literature & Writing",
    "Business & Entrepreneurship", "Astronomy & Space Exploration"
]

def remove_data_property(vl_code):
    """
    Removes the 'data' property from the Vega-Lite specification.
    """
    if 'data' in vl_code:
        vl_code['data'] = ''
    if 'datasets' in vl_code:
        vl_code['datasets'] = ''
    return vl_code


def extract_and_save_data(vl_code, csv_path):
    """
    Extracts data from the Vega-Lite code and saves it to a CSV file.
    """
    if 'data' in vl_code and 'values' in vl_code['data']:
        data = vl_code['data']['values']
        df = pd.DataFrame(data)
        df.to_csv(csv_path, index=False)
        print(f'Saved data to {csv_path}')
    else:
        print(f"No data found in the Vega-Lite code for {csv_path}")

def generate_diversified_vega_lite_code(file_path, save_dir, chart_type, method):
    client = OpenAI(base_url='', 
                    api_key='')
    with open(file_path, 'r') as json_file:
        original_vl_code = json.load(json_file)
    # original_vl_code = remove_data_property(original_vl_code)
    random.shuffle(topics_pool)
    filename = os.path.basename(file_path)


    prompt_messages = get_prompt_vega(method, chart_type, original_vl_code, topics_pool)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=prompt_messages
    )

    try:
        # Attempt to extract the Vega-Lite code from the response
        assistant_reply = response.choices[0].message.content
        vega_lite_code_blocks = re.findall(
            r'```(.*?)```', assistant_reply, re.DOTALL)
        assert vega_lite_code_blocks[0] != ''
        vega_lite_code = vega_lite_code_blocks[0].strip()
        
        if vega_lite_code.startswith('json'):
            vega_lite_code = vega_lite_code.lstrip('json')
        vega_lite_code = json.loads(vega_lite_code)

        # Save the diversified Vega-Lite code as a JSON file
        diversified_json_path = os.path.join(save_dir, f"_5_{filename}")
        with open(diversified_json_path, 'w') as json_file:
            json.dump(vega_lite_code, json_file, indent=4)
        print(f'Saved diversified Vega-Lite code to {diversified_json_path}')

        # Save the data to a CSV file
        csv_filename = f"_5_{os.path.splitext(filename)[0]}.csv"
        csv_path = os.path.join(save_dir, csv_filename)
        extract_and_save_data(vega_lite_code, csv_path)

    except Exception as e:
        print(f"Failed to generate diversified code for {filename}: {e}")
