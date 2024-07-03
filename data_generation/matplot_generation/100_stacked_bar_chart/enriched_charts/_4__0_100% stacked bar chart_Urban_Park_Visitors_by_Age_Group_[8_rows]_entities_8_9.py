
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {
    'Category': ['Fruits', 'Vegetables', 'Grains', 'Dairy', 'Meat', 'Nuts', 'Legumes'],
    'Protein': [1, 2, 3, 8, 20, 15, 10],
    'Fat': [0.2, 0.1, 0.5, 5, 15, 50, 1],
    'Carbohydrates': [14, 6, 20, 12, 0, 5, 20],
    'Fiber': [2, 3, 2, 0, 0, 8, 8],
    'Sugar': [10, 2, 0.5, 12, 0, 2, 1]
}

df = pd.DataFrame(data)
df.set_index('Category', inplace=True)

colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']

columns = df.columns
n_rows = len(df)

fig, ax = plt.subplots(figsize=(12, 8))

for i, column in enumerate(columns):
    values = df[column].values
    bottom_values = df[columns[:i]].sum(axis=1).values if i > 0 else np.zeros(n_rows)
    ax.bar(df.index, values, color=colors[i], edgecolor='white', width=0.6, bottom=bottom_values)

for i in range(n_rows):
    for j, column in enumerate(columns):
        value = df[column].values[i]
        bottom_value = df[columns[:j]].sum(axis=1).values[i]
        if value != 0:
            ax.text(i, bottom_value + value/2, f'{value}%', va='center', ha='center', color='black')

ax.set_xticks(np.arange(n_rows))
ax.set_xticklabels(df.index, rotation=45, ha='right')

ax.set_yticks(np.linspace(0, 100, 11))
ax.set_yticklabels([f'{i}%' for i in range(0, 101, 10)])

ax.set_title('Nutritional Composition of Different Food Categories', fontsize=18, pad=20)
ax.set_xlabel('Food Category', fontsize=14)
ax.set_ylabel('Percentage', fontsize=14)

ax.legend(columns, loc='upper left', bbox_to_anchor=(1, 1), fancybox=True, shadow=True, ncol=1)

plt.tight_layout()
plt.show()