
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Group 1': [18, 28, 23, 19, 12],
    'Group 2': [17, 22, 31, 18, 12],
    'Group 3': [12, 25, 33, 21, 9],
    'Group 4': [23, 21, 24, 18, 14],
    'Group 5': [22, 27, 22, 18, 11],
    'Group 6': [31, 18, 22, 19, 10],
    'Group 7': [24, 17, 28, 22, 9],
    'Group 8': [19, 24, 21, 25, 11],
    'Group 9': [15, 27, 29, 18, 11],
    'Group 10': [20, 21, 32, 18, 9]
}

categories = list(data.keys())
labels = ['Health & Fitness', 'Travel & Adventure', 'Science & Nature', 'Entertainment & Leisure', 'Economics & Finance']
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2']

data_values = np.array(list(data.values()))
data_cum = data_values.cumsum(axis=1)

fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.7

for i in range(data_values.shape[1]):
    starts = data_cum[:, i] - data_values[:, i]
    ax.bar(categories, data_values[:, i], bottom=starts, width=bar_width, label=labels[i], color=colors[i])

ax.set_ylabel('Percentage')
ax.set_title('Distribution of Interests Across Different Groups')
ax.legend(loc='upper left')

plt.tight_layout()
plt.show()