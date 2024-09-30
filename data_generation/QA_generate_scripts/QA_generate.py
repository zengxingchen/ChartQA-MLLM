from openai import OpenAI
import os
import json
import re
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from template import get_template

def read_csv_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def read_file_content(file_path):
    with open(file_path, 'r') as file:
        if file_path.endswith('.json'):
            return json.load(file)
        else:
            return file.read()

# def generate_qa_pairs(args, table_data, task_types):
#     spec, chart_name, save_dir = args
def generate_qa_pairs(args):
    spec, chart_name, save_dir, table_data, task_types, chart_type= args
    template = get_template(chart_type)

    client = OpenAI(base_url='',
        api_key='')
    question = f''' Here is a {chart_type} presented by {task_types} and table data {table_data}.{spec}
    Please generate questions about the chart in different task types.
    The task types are {chart_type}.
    You should imagine that you are looking at the image presented by the code, not the code itself.
    Remember in your answer, what is given is only an image of chart and you answer based on the image.
    The value and label are ground truth of your question, so make sure the answer is correct.
    Avoid using invalid escape character in string.
    Use approximate colour names rather than hexadecimal colours.
    Additionally, I want to save your output to a json file, so I hope you can organize your answer like
    {template}, and must include the answer with ```json ```.
    '''

    messages = [
        {"role": "system", "content": f"You are a highly intelligent AI familiar with data visualization and {task_types}."},
        {"role": "user", "content": f"{question}"}
    ]
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
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



def main(method, chart_type, chart_dir, save_dir, table_dir, max_workers):
    task_types = method
    chart_list = [f for f in os.listdir(chart_dir) if f.endswith(('.json', '.py', '.html'))]

    args_list = [
        (read_file_content(os.path.join(chart_dir, chart_name)),
         chart_name,
         save_dir,
         read_csv_content(os.path.join(table_dir, f"{os.path.splitext(chart_name)[0]}.csv")),
         task_types,
         chart_type)
        for chart_name in chart_list if not os.path.exists(os.path.join(save_dir, f"{os.path.splitext(chart_name)[0]}.json"))
    ]

    args_list = args_list[:]  # Limit for demonstration

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(generate_qa_pairs, args) for args in args_list]
        for future in tqdm(as_completed(futures), total=len(args_list), desc='Processing'):
            future.result()  # This will raise any exceptions caught during the execution of the task


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--method', type=str, required=True,
                    help='Type of method (e.g., matplot, echart, seaborn, etc.)')
    parser.add_argument('--chart_type', type=str, required=True,
                    help='Type of method (e.g., bar_chart, line_chart, etc.)')
    parser.add_argument('--chart_dir', type=str,required=True)
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
    main(method=args.method, chart_type=args.chart_type, chart_dir=args.chart_dir, save_dir=args.save_dir, table_dir=args.table_dir, max_workers=args.max_workers)
