
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
topics = ['Economics Q1', 'Economics Q2', 'Economics Q3', 'Economics Q4', 'Finance Q1', 'Finance Q2', 'Finance Q3', 'Finance Q4']
data = np.array([
    [30, 25, 25, 20],
    [35, 20, 25, 20],
    [40, 20, 20, 20],
    [45, 15, 20, 20],
    [25, 30, 25, 20],
    [30, 25, 25, 20],
    [35, 20, 25, 20],
    [40, 20, 20, 20]
])

data_cum = data.cumsum(axis=1)
category_colors = ['#FF5733', '#33FF57', '#3357FF', '#F3FF33']

fig, ax = plt.subplots(figsize=(12, 7))

ax.invert_yaxis()
ax.xaxis.set_visible(True)

bar_width = 0.5

for i, (colname, color) in enumerate(zip(categories, category_colors)):
    widths = data[:, i]
    starts = data_cum[:, i] - widths
    ax.barh(topics, widths, left=starts, height=bar_width, label=colname, color=color)

ax.set_xlabel('Percentage')
ax.set_title('Distribution of Economic and Financial Data', pad=20)
ax.legend(ncol=len(categories), bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')

plt.show()