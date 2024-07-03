
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Group 1': [20, 30, 25, 15, 10],
    'Group 2': [15, 25, 30, 20, 10],
    'Group 3': [10, 20, 35, 25, 10],
    'Group 4': [25, 20, 20, 20, 15],
    'Group 5': [20, 25, 25, 20, 10],
    'Group 6': [30, 20, 20, 20, 10],
    'Group 7': [25, 15, 30, 20, 10],
    'Group 8': [20, 25, 20, 25, 10],
    'Group 9': [15, 30, 25, 20, 10],
    'Group 10': [20, 20, 30, 20, 10]
}

categories = list(data.keys())
labels = ['Fruits', 'Vegetables', 'Grains', 'Dairy', 'Protein']
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700']

data_values = np.array(list(data.values()))
data_cum = data_values.cumsum(axis=1)

fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.8

for i in range(data_values.shape[1]):
    starts = data_cum[:, i] - data_values[:, i]
    ax.barh(categories, data_values[:, i], left=starts, height=bar_width, label=labels[i], color=colors[i])

ax.set_xlabel('Percentage')
ax.set_title('Nutritional Composition by Food Groups')
ax.legend(loc='upper right')

plt.tight_layout()
plt.show()