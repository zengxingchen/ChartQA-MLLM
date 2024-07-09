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
        "value": "What is the size of the bubble at (X=5, Y=10)?"
    },
    {
        "from": "gpt",
        "value": "To find the size of the bubble at (X=5, Y=10), we locate the bubble at this position on the bubble chart. The size of this bubble is 20 units.",
        "label": "20 units"
    },
    {
        "from": "human",
        "type_of_question": "Find Extremum",
        "value": "Which bubble is the largest?"
    },
    {
        "from": "gpt",
        "value": "To identify the largest bubble, we look for the bubble with the greatest size on the chart. The largest bubble is at (X=7, Y=14) with a size of 30 units.",
        "label": "30 units"
    },
    {
        "from": "human",
        "type_of_question": "Determine Range",
        "value": "What is the range of X-values?"
    },
    {
        "from": "gpt",
        "value": "To determine the range of X-values, we look at the minimum and maximum X-values on the bubble chart. The X-values range from 1 to 10.",
        "label": "1 to 10"
    },
    {
        "from": "human",
        "type_of_question": "Characterize Distribution",
        "value": "How are the bubbles distributed across the X and Y axes?"
    },
    {
        "from": "gpt",
        "value": "The bubbles are scattered across the X and Y axes, with a higher concentration of larger bubbles around the middle range of X (4 to 7) and Y (8 to 12). There are fewer bubbles and smaller sizes at the extremes of both axes.",
        "label": "Concentrated in the middle"
    },
    {
        "from": "human",
        "type_of_question": "Find Anomalies",
        "value": "Are there any bubbles that stand out as anomalies?"
    },
    {
        "from": "gpt",
        "value": "To find anomalies, we look for bubbles that are significantly larger or positioned differently from the rest. There is one bubble at (X=2, Y=18) that stands out as an anomaly due to its unusually large size compared to other bubbles with similar X-values.",
        "label": "Anomaly"
    },
    {
        "from": "human",
        "type_of_question": "Find Clusters",
        "value": "Are there any clusters of bubbles?"
    },
    {
        "from": "gpt",
        "value": "To identify clusters, we look for groups of bubbles that are close together. There are two main clusters: one around (X=3, Y=7) and another around (X=6, Y=10), where bubbles are densely packed.",
        "label": "Two clusters"
    },
    {
        "from": "human",
        "type_of_question": "Find Correlations/Trends",
        "value": "Is there a trend or correlation between the X and Y values?"
    },
    {
        "from": "gpt",
        "value": "By examining the bubble chart, we can observe that as the X-values increase, the Y-values also tend to increase, indicating a positive correlation between X and Y. The size of the bubbles also generally increases with higher X and Y values.",
        "label": "Positive correlation"
    },
    {
        "from": "human",
        "type_of_question": "Make Comparisons",
        "value": "How do the bubbles at (X=3, Y=7) and (X=9, Y=13) compare?"
    },
    {
        "from": "gpt",
        "value": "To compare the bubbles at (X=3, Y=7) and (X=9, Y=13), we look at their respective sizes and positions on the bubble chart. The bubble at (X=3, Y=7) has a size of 15 units, while the bubble at (X=9, Y=13) has a size of 25 units. Therefore, the bubble at (X=9, Y=13) is larger.",
        "label": "Bubble at (X=9, Y=13) is larger"
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
    # client = OpenAI(base_url='',
    #     api_key='')
    client = OpenAI(base_url='',
        api_key='')
    



    # Here are some examples:{example_questions}
    question = f''' Here is a bubble chart presented by {chart_type} code and table data {table_data}.{spec}
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
                        default=r'bubble_chart')
    parser.add_argument('--save_dir', type=str,
                        default=r'bubble_chart_QA')
    parser.add_argument('--output_file', type=str,
                        default='output.json')
    parser.add_argument('--max_workers', type=int,
                        default=200, help='Number of worker processes')
    parser.add_argument('--multiprocessing', type=bool, default=True)
    parser.add_argument('--table_dir', type=str, required=True, help='Path to the table data CSV file.')

    args = parser.parse_args()
    os.makedirs(args.save_dir, exist_ok=True)
    main(chart_dir=args.chart_dir, save_dir=args.save_dir, table_dir=args.table_dir, max_workers=args.max_workers)
