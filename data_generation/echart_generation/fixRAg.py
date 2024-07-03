import os
import re

def replace_absolute_with_relative_paths(file_path, target_root):
    """将Python文件中的绝对路径替换为相对路径。"""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 使用正则表达式查找所有以 target_root 开头的绝对路径
    pattern = re.escape(target_root) + r'[^\'\"\n]*'
    matches = re.findall(pattern, content)

    for match in matches:
        # 计算相对路径
        rel_path = os.path.relpath(match, os.path.dirname(file_path))
        # 替换绝对路径为相对路径
        content = content.replace(match, rel_path)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Processed file: {file_path}")

def process_directory(directory, target_root):
    """遍历主目录下的所有Python文件，并替换绝对路径为相对路径。"""
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.py'):
                file_path = os.path.join(root, file_name)
                replace_absolute_with_relative_paths(file_path, target_root)

if __name__ == "__main__":
    main_directory = r'data_engine\bench_space_data\table_data_csv'
    target_root = r"E:\VIS2024\chart-understanding"
    process_directory(main_directory, target_root)
