
import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    [20, 35, 30, 10, 5],
    [15, 25, 30, 20, 10],
    [10, 20, 35, 25, 10],
    [25, 20, 25, 20, 10],
    [20, 20, 30, 20, 10],
    [15, 30, 25, 20, 10],
    [10, 25, 30, 25, 10],
    [20, 30, 30, 15, 5],
    [10, 20, 35, 25, 10],
    [15, 25, 30, 20, 10]
])

categories = ['Soccer', 'Basketball', 'Baseball', 'Swimming', 'Tennis', 'Running', 'Cycling', 'Gymnastics', 'Hiking', 'Yoga']
labels = ['Under 18', '18-25', '26-35', '36-50', 'Over 50']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

data_cum = data.cumsum(axis=1)
category_colors = plt.get_cmap('tab20b')(np.linspace(0.15, 0.85, data.shape[1]))

fig, ax = plt.subplots(figsize=(12, 8))
ax.invert_yaxis()
ax.xaxis.set_visible(False)
ax.set_xlim(0, np.sum(data, axis=1).max())

for i, (colname, color) in enumerate(zip(labels, colors)):
    widths = data[:, i]
    starts = data_cum[:, i] - widths
    ax.barh(categories, widths, left=starts, height=0.6, label=colname, color=color)

ax.legend(ncol=len(labels), bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')
ax.set_title('Age Distribution in Various Sports', loc='center')

plt.show()