
import matplotlib.pyplot as plt
import numpy as np

data = [
    [30, 25, 20, 25],
    [40, 20, 25, 15],
    [35, 30, 20, 15],
    [50, 20, 15, 15],
    [25, 35, 30, 10],
    [20, 25, 35, 20],
    [45, 15, 25, 15],
    [30, 20, 30, 20],
    [40, 25, 20, 15],
    [35, 25, 20, 20],
    [25, 30, 25, 20],
    [30, 25, 30, 15],
    [20, 30, 30, 20],
    [45, 20, 20, 15],
    [35, 25, 25, 15]
]

categories = ['Sports', 'Fitness', 'Outdoor', 'Indoor', 'Extreme', 'Water', 'Winter', 'Team', 'Solo', 'Recreational', 'Professional', 'Adventure', 'Hiking', 'Running', 'Cycling']

data = np.array(data)
data_cumsum = np.cumsum(data, axis=1)
category_colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']

fig, ax = plt.subplots(figsize=(12, 7))
bar_width = 0.5
for i, (colname, color) in enumerate(zip(['Type A', 'Type B', 'Type C', 'Type D'], category_colors)):
    widths = data[:, i]
    starts = data_cumsum[:, i] - widths
    ax.barh(categories, widths, left=starts, height=bar_width, label=colname, color=color)

ax.set_xlabel('Percentage')
ax.set_title('Distribution of Sports and Fitness Activities')
ax.legend(ncol=4, bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')

plt.show()