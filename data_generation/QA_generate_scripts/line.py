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
        "value": "What is the value at X=5?"
    },
    {
        "from": "gpt",
        "value": "To find the value at X=5, we locate the point on the line chart where the X-axis is 5. From the chart, the corresponding Y-value at X=5 is 10.",
        "label": "10"
    },
    {
        "from": "human",
        "type_of_question": "Find Extremum",
        "value": "What is the highest value in the chart?"
    },
    {
        "from": "gpt",
        "value": "To identify the highest value in the chart, we look for the peak point on the line chart. The highest value is at X=7 with a Y-value of 15.",
        "label": "15"
    },
    {
        "from": "human",
        "type_of_question": "Determine Range",
        "value": "What is the range of Y-values?"
    },
    {
        "from": "gpt",
        "value": "To determine the range of Y-values, we look at the minimum and maximum Y-values on the line chart. The Y-values range from 2 to 15.",
        "label": "2 to 15"
    },
    {
        "from": "human",
        "type_of_question": "Find Correlations/Trends",
        "value": "What trend can be observed in the data over time?"
    },
    {
        "from": "gpt",
        "value": "By examining the line chart, we can observe that the values generally increase over time, with some fluctuations. The overall trend shows a positive increase from X=1 to X=10.",
        "label": "Positive trend"
    },
    {
        "from": "human",
        "type_of_question": "Make Comparisons",
        "value": "How do the values at X=3 and X=9 compare?"
    },
    {
        "from": "gpt",
        "value": "To compare the values at X=3 and X=9, we look at their respective points on the line chart. At X=3, the Y-value is 5, and at X=9, the Y-value is 12. Therefore, the value at X=9 is higher than the value at X=3.",
        "label": "X=9 is higher"
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
    question = f''' Here is a line chart presented by {chart_type} code and table data {table_data}.{spec}
    Please generate questions about the chart in different task types.
    The task types are {task_types}.

    It is really important that you should imagine that you are looking at the image presented by the code, not the code itself! 
    Remember in your answer, what is given is only an image of chart and you answer based on the image!
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
        print(response)
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
                        default=r'line_chart')
    parser.add_argument('--save_dir', type=str,
                        default=r'line_chart_QA')
    parser.add_argument('--output_file', type=str,
                        default='output.json')
    parser.add_argument('--max_workers', type=int,
                        default=100, help='Number of worker processes')
    parser.add_argument('--multiprocessing', type=bool, default=True)
    parser.add_argument('--table_dir', type=str, required=True, help='Path to the table data CSV file.')

    args = parser.parse_args()
    os.makedirs(args.save_dir, exist_ok=True)
    main(chart_dir=args.chart_dir, save_dir=args.save_dir, table_dir=args.table_dir, max_workers=args.max_workers)
