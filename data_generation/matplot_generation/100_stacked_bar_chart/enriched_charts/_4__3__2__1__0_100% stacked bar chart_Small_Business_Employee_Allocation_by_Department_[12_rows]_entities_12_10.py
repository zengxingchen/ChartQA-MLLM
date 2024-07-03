
import matplotlib.pyplot as plt
import numpy as np

categories = ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6', 'Week 7', 'Week 8', 'Week 9', 'Week 10']
physical_health = [25, 18, 22, 27, 24, 30, 21, 19, 26, 23]
mental_health = [30, 28, 33, 25, 22, 27, 26, 29, 23, 24]
nutrition = [20, 35, 27, 32, 33, 24, 28, 30, 25, 28]
wellness = [25, 19, 18, 16, 21, 19, 25, 22, 26, 25]

data = np.array([physical_health, mental_health, nutrition, wellness])
data_cum = data.cumsum(axis=0)

bar_width = 0.7

colors = ['#FF5733', '#33FFBD', '#335BFF', '#FFC133']

fig, ax = plt.subplots(figsize=(12, 8))

categories_pos = np.arange(len(categories))

for i, (colname, color) in enumerate(zip(['Physical Health', 'Mental Health', 'Nutrition', 'Wellness'], colors)):
    heights = data[i]
    starts = data_cum[i] - heights
    ax.bar(categories_pos, heights, bottom=starts, width=bar_width, label=colname, color=color)

ax.set_xticks(categories_pos)
ax.set_xticklabels(categories)
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
ax.set_ylabel('Percentage')
ax.set_title('Weekly Health & Wellness Data', pad=20)

plt.show()