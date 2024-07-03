
import matplotlib.pyplot as plt
import numpy as np

data = [
    [55, 25, 10, 10],
    [35, 40, 15, 10],
    [45, 20, 25, 10],
    [25, 30, 35, 10],
    [30, 35, 25, 10],
    [40, 30, 20, 10],
    [50, 25, 15, 10],
    [20, 35, 35, 10],
    [45, 20, 25, 10],
    [30, 40, 20, 10],
    [25, 35, 30, 10],
    [55, 20, 15, 10],
    [35, 25, 30, 10],
    [50, 20, 20, 10],
    [45, 30, 15, 10]
]

categories = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12', 'Q13', 'Q14', 'Q15']

data = np.array(data)
data_cumsum = np.cumsum(data, axis=1)
category_colors = ['#4B8BBE', '#306998', '#FFE873', '#FFD43B']

fig, ax = plt.subplots(figsize=(10, 14))
bar_height = 0.6
for i, (colname, color) in enumerate(zip(['Type A', 'Type B', 'Type C', 'Type D'], category_colors)):
    heights = data[:, i]
    starts = data_cumsum[:, i] - heights
    ax.bar(categories, heights, bottom=starts, width=bar_height, label=colname, color=color)

ax.set_ylabel('Percentage')
ax.set_title('Quarterly Sales Distribution')
ax.legend(ncol=4, bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')

plt.show()