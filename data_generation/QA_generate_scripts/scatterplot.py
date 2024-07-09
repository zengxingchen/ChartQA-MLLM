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
        "value": "What is the Y value of the point at (X=5)?"
    }
    },
    {
        "from": "gpt",
        "value": "To find the value of the point at (X=5), we locate the point with X-coordinate 5 on the scatterplot. The Y value at this point is 10.",
        "label": "10"
    },
    {
        "from": "human",
        "type_of_question": "Find Extremum",
        "value": "Which point has the highest Y-value?"
    },
    {
        "from": "gpt",
        "value": "To identify the point with the highest Y-value, we look for the point that is the highest on the vertical axis. The point with the highest Y-value is (X=7, Y=15).",
        "label": "(7,15)"
    },
    {
        "from": "human",
        "type_of_question": "Determine Range",
        "value": "What is the range of X-values?"
    },
    {
        "from": "gpt",
        "value": "To determine the range of X-values, we look at the minimum and maximum X-values on the scatterplot. The X-values range from 1 to 10.",
        "label": "1 to 10"
    },
    {
        "from": "human",
        "type_of_question": "Characterize Distribution",
        "value": "How are the points distributed across the X and Y axes?"
    },
    {
        "from": "gpt",
        "value": "The points are scattered across the X and Y axes, with a concentration of points in the middle range of X (4 to 6) and Y (8 to 12). There are fewer points at the extremes of both axes.",
        "label": "Concentrated in the middle"
    },
    {
        "from": "human",
        "type_of_question": "Find Anomalies",
        "value": "Are there any points that stand out as anomalies?"
    },
    {
        "from": "gpt",
        "value": "To find anomalies, we look for points that are far from the rest of the data. There is one point at (X=2, Y=14) that stands out as an anomaly since it is significantly higher than other points with similar X-values.",
        "label": "Anomaly"
    },
    {
        "from": "human",
        "type_of_question": "Find Clusters",
        "value": "Are there any clusters of points?"
    {
        "from": "gpt",
        "value": "To identify clusters, we look for groups of points that are close together. There are two main clusters: one around (X=4, Y=8) and another around (X=6, Y=12).",
        "label": "Two clusters"
    },
    {
        "from": "human",
        "type_of_question": "Find Correlations/Trends",
        "value": "Is there a trend or correlation between the X and Y values?"
    },
    {
        "from": "gpt",
        "value": "By examining the scatterplot, we can observe that as the X-values increase, the Y-values also tend to increase. This indicates a positive correlation between X and Y.",
        "label": "Positive correlation"
    },
    {
        "from": "human",
        "type_of_question": "Make Comparisons",
        "value": "How do the points at (X=3, Y=7) and (X=9, Y=13) compare?"
    },
    {
        "from": "gpt",
        "value": "To compare the points at (X=3, Y=7) and (X=9, Y=13), we look at their positions on the scatterplot. The point at (X=9, Y=13) is higher on the Y-axis and further to the right on the X-axis compared to the point at (X=3, Y=7), indicating higher values in both dimensions.",
        "label": "Higher in both dimensions"
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
    with open(file_path, 'r', encoding='utf-8') as file:
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
    question = f''' Here is a scatter plot presented by {chart_type} code and table data {table_data}.{spec}
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
                        default=r'scatterplot')
    parser.add_argument('--save_dir', type=str,
                        default=r'scatterplot_QA')
    parser.add_argument('--output_file', type=str,
                        default='output.json')
    parser.add_argument('--max_workers', type=int,
                        default=200, help='Number of worker processes')
    parser.add_argument('--multiprocessing', type=bool, default=True)
    parser.add_argument('--table_dir', type=str, required=True, help='Path to the table data CSV file.')

    args = parser.parse_args()
    os.makedirs(args.save_dir, exist_ok=True)
    main(chart_dir=args.chart_dir, save_dir=args.save_dir, table_dir=args.table_dir, max_workers=args.max_workers)
