import os
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from generate_diversed_echart import generate_diversified_echart_code
from generate_diversed_python import generate_diversified_python_code
from generate_diversed_vega import generate_diversified_vega_lite_code

def get_generator_function(method):
    generator_mapping = {
        "vega-lite": generate_diversified_vega_lite_code,
        "echart": generate_diversified_echart_code,
        "matplot": generate_diversified_python_code,
        "seaborn": generate_diversified_python_code,
    }
    return generator_mapping.get(method, None)

def get_file_extension(method):
    extension_mapping = {
        "vega-lite": ".json",
        "echart": ".html",
        "matplot": ".py",
        "seaborn": ".py",

    }
    return extension_mapping.get(method, None)

def main(data_dir, save_dir, max_workers, method, chart_type):
    os.makedirs(save_dir, exist_ok=True)
    file_extension = get_file_extension(method)
    file_paths = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith(file_extension)]

    args_list = [(file_path, save_dir, chart_type, method) for file_path in file_paths]
    
    generate_function = get_generator_function(method)
    
    if generate_function is None:
        print(f"Unsupported method: {method}")
        return

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(generate_function, file_path, save_dir, chart_type, method) for file_path, save_dir, chart_type, method in args_list]
        for future in tqdm(as_completed(futures), total=len(args_list), desc='Processing files'):
            try:
                future.result()
            except Exception as exc:
                print(f'Generated exception: {exc}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate Vega-Lite code from CSV data using OpenAI API.")
    parser.add_argument('--method', type=str, required=True,
                    help='Type of method (e.g., matplot, echart, seaborn, etc.)')
    parser.add_argument('--chart_type', type=str, required=True,
                    help='Type of chart to generate (e.g., bar_chart, line_chart, pie_chart, etc.)')
    parser.add_argument('--data_dir', type=str, default=r"enriched_charts",
                        help='Directory path containing CSV tables')
    parser.add_argument('--save_dir', type=str, default=r'generate_result',
                        help='Directory path to save generated Vega-Lite JSON files')
    parser.add_argument('--max_workers', type=int, default=100,
                        help='Maximum number of processes to use for concurrent requests. Defaults to number of CPUs')
    parser.add_argument('--multiprocessing', type=bool, default=True)
    
    args = parser.parse_args()
    if args.method == "vega-lite":
        args.data_dir = os.path.join("..", f"{args.method}_generation", args.chart_type, args.data_dir,f"code")
        args.save_dir = os.path.join("..",f"{args.method}_generation", args.chart_type, args.save_dir)
    else:
        args.data_dir = os.path.join("..",f"{args.method}_generation", args.chart_type, args.data_dir)
        args.save_dir = os.path.join("..",f"{args.method}_generation", args.chart_type, args.save_dir)
    
    os.makedirs(args.save_dir, exist_ok=True)
    main(data_dir=args.data_dir, save_dir=args.save_dir, chart_type=args.chart_type, method=args.method, max_workers=args.max_workers)
