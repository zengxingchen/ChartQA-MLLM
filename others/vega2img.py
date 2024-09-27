import os
import vl_convert as vlc
from multiprocessing import Pool, cpu_count
import argparse
from altair_saver import save



def process_file(chart_dir, img_dir, file_name_list):
    for file_name in file_name_list:
        if not file_name.endswith('.json'):
            continue
        print(file_name)
        
        file_path = os.path.join(chart_dir, file_name)
        img_file_path = os.path.join(img_dir, file_name.replace('.json', '.png'))
        if os.path.exists(img_file_path):
            print(f"File already exists, skipping: {img_file_path}")
            continue
        # 读取json文件内容到vl_spec
        with open(file_path, 'r', encoding='utf-8') as json_file:
            vl_spec = json_file.read()
        
        # 将vl_spec转换为PNG数据
        try:
            png_data = vlc.vegalite_to_png(vl_spec=vl_spec, scale = 2)
        
            # 保存PNG数据到img文件夹中，文件名与原json文件一致，但扩展名为.png
            with open(img_file_path, 'wb') as img_file:
                img_file.write(png_data)
        except:
            print(f"Error: {file_path}")

def split_into_chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def main(chart_dir, img_dir, multiprocessing):
    json_files = sorted([f for f in os.listdir(chart_dir) if f.endswith('.json')])

    if not multiprocessing:
        process_file(chart_dir, img_dir, json_files)
        return
    if multiprocessing:
        # num_files_per_chunk = len(json_files) // cpu_count()
        num_files_per_chunk = len(json_files) // 20
        chunks = list(split_into_chunks(json_files, num_files_per_chunk))
        # with Pool(processes=max(cpu_count(), len(json_files))) as pool:  
        with Pool(processes=max(20, len(json_files))) as pool:
            pool.starmap(process_file, [(chart_dir, img_dir, chunk) for chunk in chunks])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process Vega-Lite chart files')
    parser.add_argument('--chart_dir', type=str, default=r"", help='Path to the chart directory')
    parser.add_argument('--img_dir', type=str, default=r'', help='Path to the image directory')
    parser.add_argument('--multiprocessing', type=bool, default=False, help='Whether to use multiprocessing')
    args = parser.parse_args()
    os.makedirs(args.img_dir, exist_ok=True)
    main(args.chart_dir, args.img_dir, args.multiprocessing)

    