
import matplotlib.pyplot as plt
import numpy as np

# Data
topics = ['Subject 1', 'Subject 2', 'Subject 3', 'Subject 4', 'Subject 5', 'Subject 6', 'Subject 7', 'Subject 8', 'Subject 9', 'Subject 10', 'Subject 11', 'Subject 12']
categories = ['Category A', 'Category B', 'Category C', 'Category D']
data = np.array([
    [20, 30, 25, 25],
    [15, 35, 30, 20],
    [25, 25, 20, 30],
    [30, 20, 30, 20],
    [20, 25, 35, 20],
    [25, 20, 25, 30],
    [20, 30, 20, 30],
    [30, 25, 25, 20],
    [25, 30, 20, 25],
    [20, 35, 25, 20],
    [25, 20, 30, 25],
    [30, 25, 20, 25]
])

data_cum = data.cumsum(axis=1)
category_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

fig, ax = plt.subplots(figsize=(14, 8))

bar_height = 0.75

for i, (colname, color) in enumerate(zip(categories, category_colors)):
    heights = data[:, i]
    starts = data_cum[:, i] - heights
    ax.bar(topics, heights, bottom=starts, width=bar_height, label=colname, color=color)

ax.set_ylabel('Percentage')
ax.set_title('Distribution of Education & Learning Data', pad=20)
ax.legend(ncol=len(categories), bbox_to_anchor=(1, 1), loc='upper left', fontsize='small')

plt.xticks(rotation=90)
plt.show()