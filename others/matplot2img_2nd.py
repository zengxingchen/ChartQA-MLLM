import os
import matplotlib.pyplot as plt
import numpy as np
import concurrent.futures

# 设置文件路径
matplotlib_code_folder_path = r'E:\VIS2024\chart-understanding\data_engine\bench_space_data\diverse_scripts\matplot_generation\bar_chart\truncated_bar'  # 替换为存放Matplotlib代码文件的文件夹路径
output_folder_path = r'E:\VIS2024\chart-understanding\data_engine\bench_space_data\diverse_scripts\matplot_generation\bar_chart\truncated_bar'  # 替换为存放输出图片的文件夹路径

# 确保输出文件夹存在
os.makedirs(output_folder_path, exist_ok=True)

def process_file(filename):
    if not filename.endswith('.py'):
        return

    file_path = os.path.join(matplotlib_code_folder_path, filename)
    output_file_path = os.path.join(output_folder_path, filename.replace('.py', '.png'))

    # 检查目标文件是否已存在
    if os.path.exists(output_file_path):
        print(f"{output_file_path} 已存在，跳过。")
        return

    # 读取Matplotlib代码文件内容
    with open(file_path, 'r') as file:
        code = file.read()

    # 将代码中的 plt.show() 替换为 plt.savefig() 以防止 plt.show() 清空图像
    code = code.replace('plt.show()', '')  # 删除 plt.show()

    # 执行Matplotlib代码
    try:
        exec(code, {'plt': plt, 'np': np})
        
        # 保存生成的图表为图片
        plt.savefig(output_file_path)
        plt.close()
        print(f"{filename} 已成功转换为图片并保存。")
    except Exception as e:
        print(f"执行 {filename} 时出错: {e}")

if __name__ == '__main__':
    # 指定进程数量
    num_processes = 10

    # 使用多进程处理文件
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_processes) as executor:
        executor.map(process_file, os.listdir(matplotlib_code_folder_path))

    print("所有Matplotlib代码文件已转换为图片并保存。")
