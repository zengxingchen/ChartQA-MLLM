
import matplotlib.pyplot as plt
import numpy as np

categories = ['Basketball', 'Soccer', 'Tennis', 'Swimming', 'Cycling']
years = ['1990', '2000', '2010', '2020', '2030']
data = np.array([
    [30, 35, 40, 45, 50],  # Basketball
    [25, 30, 35, 30, 25],  # Soccer
    [20, 15, 10, 15, 20],  # Tennis
    [15, 10, 8, 5, 3],     # Swimming
    [10, 10, 7, 5, 2]      # Cycling
])

data_cum = data.cumsum(axis=0)
category_colors = ['#4c72b0', '#55a868', '#c44e52', '#8172b2', '#ccb974']

fig, ax = plt.subplots(figsize=(8, 10))

for i, (colname, color) in enumerate(zip(categories, category_colors)):
    heights = data[i]
    starts = data_cum[i] - heights
    ax.bar(years, heights, bottom=starts, width=0.8, label=colname, color=color)

ax.set_ylabel('Percentage')
ax.set_xlabel('Year')
ax.set_title('Popularity of Sports Over Time', pad=20)
ax.legend(loc='upper left')

plt.show()