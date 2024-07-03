
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = [
    {'Location': 'Pyramids of Giza', 'Ancient Structures (%)': 30, 'Pottery (%)': 15, 'Weapons and Tools (%)': 25, 'Human Remains (%)': 10, 'Art and Decorations (%)': 20},
    {'Location': 'Stonehenge', 'Ancient Structures (%)': 25, 'Pottery (%)': 20, 'Weapons and Tools (%)': 10, 'Human Remains (%)': 30, 'Art and Decorations (%)': 15},
    {'Location': 'Machu Picchu', 'Ancient Structures (%)': 20, 'Pottery (%)': 10, 'Weapons and Tools (%)': 30, 'Human Remains (%)': 15, 'Art and Decorations (%)': 25},
    {'Location': 'Acropolis of Athens', 'Ancient Structures (%)': 15, 'Pottery (%)': 25, 'Weapons and Tools (%)': 20, 'Human Remains (%)': 25, 'Art and Decorations (%)': 15},
    {'Location': 'Easter Island', 'Ancient Structures (%)': 10, 'Pottery (%)': 30, 'Weapons and Tools (%)': 15, 'Human Remains (%)': 20, 'Art and Decorations (%)': 25}
]

df = pd.DataFrame(data)
df.set_index('Location', inplace=True)

df_percentage = df.div(df.sum(axis=1), axis=0) * 100

plt.figure(figsize=(12, 8))

bottom = np.zeros(len(df))

colors = ['#8B0000', '#4682B4', '#9ACD32', '#FFD700', '#FF69B4']

for i, col in enumerate(df.columns):
    plt.bar(df_percentage.index, df_percentage[col], bottom=bottom, label=col, color=colors[i], width=0.5)
    bottom += df_percentage[col]

plt.xlabel('Archaeological Sites')
plt.ylabel('Percentage')
plt.title('Archaeological Findings Breakdown (100% Stacked)', pad=30)
plt.legend(title='Categories', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()