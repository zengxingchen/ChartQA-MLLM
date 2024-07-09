from openai import OpenAI
import os
import json
import re
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

def read_csv_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_types_from_template(template):
    matches = re.findall(r'"type_of_question": "(.*?)"', template)
    return ", ".join(matches)


template = '''
```json
[
    {
        "from": "human",
        "type_of_question": "Data Retrieval",
        "value": "What was the percentage of Books sold in 1990?."
    },
    {
        "from": "gpt",
        "value": "Looking at the chart, the percentage of Books sold in 1990 can be found by locating the bar representing Books for the year 1990. The Books segment is the second section of the stacked bar and is colored in red. According to the visual encoding, the percentage for Books in 1990 is 20%.",
        "label": "20%"
    },
    {
        "from": "human",
        "type_of_question": "Find Extremum",
        "value": "In which year was the percentage of fiction sold the highest?"
    },
    {
        "from": "gpt",
        "value": "To determine the year when the percentage of fiction sold was the highest, we need to look at the yellow segments of the stacked bars across all the years. The highest yellow segment is in 1992, where the percentage is 32%. Therefore, the year with the highest percentage of fiction sold is 1992.",
        "label": "1992"
    },
    {
        "from": "human",
        "type_of_question": "Make Comparisons",
        "value": "Compare the percentage of cars sold between 2015 and 2023."
    },
    {
        "from": "gpt",
        "value": "To compare the percentage of cars sold between 2015 and 2023, we examine the orange segments in the stacked bars for those years. In 2015, the percentage for cars is 10%, while in 2023, it is 15%. Therefore, the percentage of cars sold increased from 10% in 2015 to 15% in 2023.",
        "label": "Increase"
    }
]
```
'''


def get_chart_type(file_name):
    if file_name.startswith('vl_'):
        return 'vega-lite'
    elif file_name.startswith('echart_'):
        return 'echart'
    elif file_name.startswith('matplot_'):
        return 'matplotlib'
    elif file_name.startswith('seaborn_'):
        return 'seaborn'
    else:
        return 'unknown'

def read_file_content(file_path):
    with open(file_path, 'r') as file:
        if file_path.endswith('.json'):
            return json.load(file)
        else:
            return file.read()


def generate_qa_pairs(args, table_data, task_types):
    spec, chart_name, save_dir = args

    chart_type = get_chart_type(chart_name)

    # client = OpenAI(base_url='',
    #     api_key='')
    client = OpenAI(base_url='',
        api_key='')
    question = f''' Here is a percentage stacked bar chart presented by {chart_type} and table data {table_data}.{spec}
    Please generate questions about the chart in different task types.
    The task types are {task_types}.
    You should imagine that you are looking at the image presented by the code, not the code itself.
    Remember in your answer, what is given is only an image of chart and you answer based on the image.
    The value and label are ground truth of your question, so make sure the answer is correct.
    Avoid using invalid escape character in string.
    Use approximate colour names rather than hexadecimal colours.
    Additionally, I want to save your output to a json file, so I hope you can organize your answer like
    {template}, and must include the answer with ```json ```.
    '''

    messages = [
        {"role": "system", "content": f"You are a highly intelligent AI familiar with data visualization and {chart_type}."},
        {"role": "user", "content": f"{question}"}
    ]
    try:
        response = client.chat.completions.create(
            # model="gpt-3.5-turbo-16k",
            model="gpt-4o",
            messages=messages
        )
        print(response)
    except:
        return
    try:
        assistant_reply = response.choices[0].message.content
        print(assistant_reply)
        json_spec_blocks = re.findall(
            r'```(.*?)```', assistant_reply, re.DOTALL)
        if json_spec_blocks:
            json_spec = json_spec_blocks[0].strip()
        else:
            json_spec = assistant_reply
        # assert json_spec.startswith('json')
        json_spec = json_spec.lstrip('json')
        qa_pairs = json.loads(json_spec)
        json_path = f'{save_dir}/{os.path.splitext(chart_name)[0]}.json'  # 强制保存为 .json 文件
        with open(json_path, 'w') as file:
            json.dump(qa_pairs, file, indent=4)
        print(f"Save qa_pairs to {json_path}")
    except Exception as e:
        print(f"Error processing {chart_name}: {e}")



def main(chart_dir, save_dir, table_dir, max_workers):
    task_types = extract_types_from_template(template)
    chart_list = [f for f in os.listdir(chart_dir) if f.endswith(('.json', '.py', '.html'))]
    args_list = [
        (read_file_content(os.path.join(chart_dir, chart_name)), chart_name, save_dir, read_csv_content(os.path.join(table_dir, f"{os.path.splitext(chart_name)[0]}.csv")), task_types)
        for chart_name in chart_list if not os.path.exists(os.path.join(save_dir, f"{os.path.splitext(chart_name)[0]}.json"))
    ]

    args_list = args_list[:]  # Limit for demonstration

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(generate_qa_pairs, args) for args in args_list]
        for future in tqdm(as_completed(futures), total=len(args_list), desc='Processing'):
            future.result()  # This will raise any exceptions caught during the execution of the task


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--chart_dir', type=str,
                        default=r'100_stacked_bar_chart')
    parser.add_argument('--save_dir', type=str,
                        default=r'100_stacked_bar_chart_QA')
    parser.add_argument('--output_file', type=str,
                        default='output.json')
    parser.add_argument('--max_workers', type=int,
                        default=100, help='Number of worker processes')
    parser.add_argument('--multiprocessing', type=bool, default=True)
    parser.add_argument('--table_dir', type=str, required=True, help='Path to the table data CSV file.')

    args = parser.parse_args()
    os.makedirs(args.save_dir, exist_ok=True)
    main(chart_dir=args.chart_dir, save_dir=args.save_dir, table_dir=args.table_dir, max_workers=args.max_workers)
