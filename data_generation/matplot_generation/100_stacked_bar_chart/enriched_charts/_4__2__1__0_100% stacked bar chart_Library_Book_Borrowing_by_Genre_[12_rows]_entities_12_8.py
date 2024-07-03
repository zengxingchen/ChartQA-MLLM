
import matplotlib.pyplot as plt
import numpy as np

categories = ['Opera', 'Concert', 'Theater', 'Art Exhibition', 'Ballet', 'Museum Visit', 'Film Festival', 'Literary Reading', 'Dance Performance', 'Music Festival']
data = {
    '2019': [15, 25, 20, 30, 10, 25, 20, 15, 20, 30],
    '2020': [20, 30, 25, 35, 15, 30, 25, 20, 25, 35],
    '2021': [25, 35, 30, 40, 20, 35, 30, 25, 30, 40]
}

labels = list(data.keys())
data = np.array(list(data.values()))
data_cum = data.cumsum(axis=1)

category_colors = ['#E6B0AA', '#AED6F1', '#A9DFBF', '#F9E79F', '#F5B7B1', '#F1948A', '#76D7C4', '#A569BD', '#52BE80', '#F0B27A']

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.35

for i, (colname, color) in enumerate(zip(labels, category_colors)):
    heights = data[i]
    starts = data_cum[i] - heights
    ax.bar(categories, heights, bottom=starts, width=bar_width, label=colname, color=color)

ax.set_ylabel('Percentage')
ax.set_title('Popularity of Cultural Activities Over Years', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1.05))

plt.tight_layout()
plt.show()