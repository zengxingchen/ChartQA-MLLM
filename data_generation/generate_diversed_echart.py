import os
import json
import re
from openai import OpenAI
import csv
import random
from prompt_echart import get_prompt_echart

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
    
def load_json_skip_first_line_if_empty(file_path):
    with open(file_path, 'r') as json_file:
        lines = json_file.readlines()
        if lines and not lines[0].strip():
            lines = lines[1:]
        json_content = ''.join(lines)
        try:
            return json.loads(json_content)
        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON in file {file_path}: {e}")
            return None   
        
def generate_diversified_echart_code(file_path, save_dir, chart_type, method):
    client = OpenAI(base_url='', 
                    api_key='')
    
    original_vl_code = load_matplotlib_code(file_path)
    random.shuffle(topics_pool)
    filename = os.path.basename(file_path)
    print(filename)

    # Constructing the prompt for GPT-4 to diversify the given Vega-Lite code
    # 6. Add text labels (or remove) in reasonable positions, but avoid give text label in stacked bar to prevent clutter.\
    prompt_messages = get_prompt_echart(method, chart_type, original_vl_code, topics_pool)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=prompt_messages
    )
    print(response)
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
            file_path = os.path.join(save_dir, f'_10_{filename_pre}.csv')

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
        diversified_json_path = os.path.join(save_dir, f"_10_{filename}")
        with open(diversified_json_path, 'w', encoding='utf-8') as file:
            file.write(html_content)
        print(f'Saved diversified python code to {diversified_json_path}')
    except Exception as e:
        print(f"Failed to generate diversified code for {filename}: {e}")


