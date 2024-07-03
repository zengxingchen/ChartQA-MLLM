
import matplotlib.pyplot as plt
import numpy as np

categories = ['Philosophy', 'Ethics', 'History', 'Archaeology', 'Literature']
years = ['Year1', 'Year2', 'Year3', 'Year4', 'Year5']
data = np.array([
    [15, 20, 25, 20, 25],
    [20, 25, 30, 25, 30],
    [30, 20, 25, 30, 35],
    [25, 30, 15, 20, 15],
    [10, 5, 5, 5, 5]
])

data_cum = data.cumsum(axis=0)
category_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

fig, ax = plt.subplots(figsize=(8, 10))
ax.invert_yaxis()
ax.xaxis.set_visible(True)
ax.set_xlim(0, np.sum(data, axis=0).max())

for i, (colname, color) in enumerate(zip(categories, category_colors)):
    widths = data[:, i]
    starts = data_cum[:, i] - widths
    ax.barh(years, widths, left=starts, height=0.6, label=colname, color=color)

ax.legend(ncol=1, bbox_to_anchor=(1, 1), loc='upper left', fontsize='small')
plt.title('Interest in Humanities Over 5 Years', pad=20)
plt.show()