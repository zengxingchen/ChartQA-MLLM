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

def generate_diversified_vega_lite_code(args):
    client = OpenAI(base_url='',
        api_key='')
    file_path, save_dir = args
    with open(file_path, 'r') as json_file:
        original_vl_code = json.load(json_file)

    # original_vl_code = remove_data_property(original_vl_code)

    filename = os.path.basename(file_path)
    print(filename)

    prompt_messages = [
        {"role": "system", "content": "You are a highly intelligent AI familiar with data visualization and Vega-Lite."},
        {"role": "user", "content": "Given the following Vega-Lite code of chart related to scatter plot: " + json.dumps(original_vl_code) +
         " Please generate a diversified bubble chart code of this Vega-Lite code.Here are some options you should follow:\
            1. Generate data points that fit the chart and the number of data points should be as much as you can to provide, but you should not skip any data point in your code. Do not add any comment in your code\
            2. Add or change some entities with new corresponding values to enrich the visualization.\
            3. Modify the color scheme using specific color codes (e.g., #RRGGBB) for better clarity or visual appeal. Avoid using color categories.\
            4. change width and height of the chart reasonably\
            5. change the topic,headline and data type (which fit the topic) of the chart,put the headline in appropriate place that does not overlap with other things (make sure the headline does not overlap with legend! put these two things away), you can refer and choose one (not all) of the topic from: " +str(topics_pool) + " but reduce using global...topic \
            We are not generating bubble chart, so the size of point should be same for each point.\
            You should choose some of these options not all of them to diversfy the visualization\
            You should give FULL code with ALL data points and don't miss any detail\
            Do not draw points too small, set the size of point that easy to read\
            Include the code with ```json ``` format."}
    ]

    response = client.chat.completions.create(
        model="gpt-4",
        # model="gpt-3.5-turbo-16k",
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
        vega_lite_code = json.loads(vega_lite_code)

        # Save the diversified Vega-Lite code as a JSON file
        diversified_json_path = os.path.join(save_dir, f"_6_{filename}")
        with open(diversified_json_path, 'w') as json_file:
            json.dump(vega_lite_code, json_file, indent=4)
        print(f'Saved diversified Vega-Lite code to {diversified_json_path}')

        # Save the data to a CSV file
        csv_filename = f"_6_{os.path.splitext(filename)[0]}.csv"
        csv_path = os.path.join(save_dir, csv_filename)
        extract_and_save_data(vega_lite_code, csv_path)

    except Exception as e:
        print(f"Failed to generate diversified code for {filename}: {e}")

def main(data_dir, save_dir, max_workers):
    os.makedirs(save_dir, exist_ok=True)
    file_paths = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith('.json')]

    args_list = [(file_path, save_dir) for file_path in file_paths]

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(generate_diversified_vega_lite_code, args) for args in args_list]
        for future in tqdm(as_completed(futures), total=len(args_list), desc='Processing files'):
            try:
                future.result()
            except Exception as exc:
                print(f'Generated exception: {exc}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate Vega-Lite code from CSV data using OpenAI API.")
    parser.add_argument('--data_dir', type=str, default=r"enriched_charts\code",
                        help='Directory path containing CSV tables')
    parser.add_argument('--save_dir', type=str, default=r'enriched_charts\code',
                        help='Directory path to save generated Vega-Lite JSON files')

    parser.add_argument('--max_workers', type=int, default=20,
                        help='Maximum number of processes to use for concurrent requests. Defaults to number of CPUs')
    parser.add_argument('--multiprocessing', type=bool, default=True)

    args = parser.parse_args()
    os.makedirs(args.save_dir, exist_ok=True)
    main(data_dir=args.data_dir, save_dir=args.save_dir, max_workers=args.max_workers)