import matplotlib.pyplot as plt
import numpy as np

categories = ['Basketball', 'Soccer', 'Baseball', 'Tennis', 'Swimming']
years = ['Year1', 'Year2', 'Year3', 'Year4', 'Year5']
data = np.array([
    [20, 30, 25, 35, 40],
    [35, 25, 30, 30, 25],
    [25, 20, 20, 20, 20],
    [10, 15, 10, 5, 10],
    [10, 10, 15, 10, 5]
])

data_cum = data.cumsum(axis=1)
category_colors = ['#FF5733', '#33FF57', '#3357FF', '#F333FF', '#57FF33']

fig, ax = plt.subplots(figsize=(10, 6))
ax.invert_yaxis()
ax.xaxis.set_visible(True)
ax.set_xlim(0, np.sum(data, axis=0).max())

for i, (colname, color) in enumerate(zip(categories, category_colors)):
    widths = data[i]
    starts = data_cum[i] - widths
    ax.barh(years, widths, left=starts, height=0.8, label=colname, color=color)

ax.legend(ncol=len(categories), bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')
plt.title('Participation in Sports Over 5 Years', pad=20)
plt.show()