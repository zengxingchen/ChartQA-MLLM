import os
import json
import numpy as np
import glob
from sklearn.neighbors import BallTree

def feature_dict_to_vector(feature_dict, max_length):
    vector = []
    for feature in feature_dict[:]:
        for key, value in feature.items():
            if key in ['fid', 'field_id']:
                continue  # Skip ID fields
            # Process numerical data and boolean values
            if isinstance(value, bool):
                vector.append(1.0 if value else 0.0)
            elif isinstance(value, (int, float)) and not np.isnan(value):
                vector.append(float(value))
    # Normalize the vector if it's shorter than max_length
    if len(vector) < max_length:
        padding = np.zeros(max_length - len(vector))
        vector = np.concatenate((vector, padding))
    # Normalize the vector to unit length
    vector = np.array(vector)
    norm = np.linalg.norm(vector)
    if norm > 0:
        vector /= norm
    else:
        # Handle the case where the norm is zero
        vector = np.zeros_like(vector)
    return vector

def clean_matrix(matrix):
    matrix = np.nan_to_num(matrix, nan=0.0)
    matrix[matrix == np.inf] = np.finfo('float64').max
    matrix[matrix == -np.inf] = np.finfo('float64').min
    return matrix

def load_features_to_matrix(feature_folder, max_length):
    vectors = []
    filenames = []
    for json_file in glob.glob(os.path.join(feature_folder, '*.json')):
        with open(json_file, 'r') as f:
            data = json.load(f)
        vector = feature_dict_to_vector(data['df_field_level_features'], max_length)
        vectors.append(vector)
        filenames.append(os.path.basename(json_file))
    return np.array(vectors), filenames

def compare_and_save_similarities(feature_folder_1, feature_folder_2, max_length, output_path):
    matrix_1, names_1 = load_features_to_matrix(feature_folder_1, max_length)
    matrix_2, names_2 = load_features_to_matrix(feature_folder_2, max_length)
    # 清理矩阵中的 NaN 和无穷大值
    matrix_1 = clean_matrix(matrix_1)
    matrix_2 = clean_matrix(matrix_2)
    
    if matrix_2.ndim == 1:
        print(f"Skipping folder {feature_folder_2} due to insufficient data.")
        return

    try:
        # Initialize BallTree with matrix_2
        tree = BallTree(matrix_2)
        # Query the BallTree for the 3 nearest neighbors of each vector in matrix_1
        distances, indices = tree.query(matrix_1, k=3)

        similarities_record = {}
        for i, name_1 in enumerate(names_1):
            # Retrieve the names of the 3 nearest neighbors
            nearest_names = [names_2[j] for j in indices[i]]
            similarities_record[name_1] = nearest_names

        # Save the similarities record to a JSON file
        with open(output_path, 'w') as f:
            json.dump(similarities_record, f, indent=4)
    except ValueError as e:
        print(f"Error processing {feature_folder_1} and {feature_folder_2}: {e}")

def main():
    base_dir_path = r'..\diverse_scripts\seaborn_generation'
    max_length = 2025  # 假定已知的最大长度
    for sub_dir in os.listdir(base_dir_path):
        sub_dir_path = os.path.join(base_dir_path, sub_dir)
        if os.path.isdir(sub_dir_path):
            feature_dir_path = os.path.join(sub_dir_path, 'feature')
            seed_feature_dir_path = os.path.join(sub_dir_path, 'seed', 'feature')
            if os.path.exists(feature_dir_path) and os.path.exists(seed_feature_dir_path):
                output_path = os.path.join(sub_dir_path, 'similarity_record.json')
                compare_and_save_similarities(feature_dir_path, seed_feature_dir_path, max_length, output_path)

if __name__ == '__main__':
    main()
