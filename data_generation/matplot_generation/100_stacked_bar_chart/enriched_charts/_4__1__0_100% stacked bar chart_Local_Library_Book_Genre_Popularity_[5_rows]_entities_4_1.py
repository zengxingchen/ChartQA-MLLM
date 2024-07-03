
import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['2015', '2016', '2017', '2018', '2019']
apples = np.array([40, 35, 30, 25, 20])
oranges = np.array([30, 25, 20, 15, 10])
bananas = np.array([20, 25, 30, 35, 40])
grapes = np.array([5, 10, 15, 20, 25])
pineapples = np.array([5, 5, 5, 5, 5])

# Stacked data
data = np.vstack([apples, oranges, bananas, grapes, pineapples])
data_cum = data.cumsum(axis=0)

# Colors
colors = ['#ff6666', '#ffcc66', '#99ff99', '#66b3ff', '#c2c2f0']

# Plot
fig, ax = plt.subplots(figsize=(12, 8))

# Vertical bar
bar_width = 0.5
for i, (colname, color) in enumerate(zip(['Apples', 'Oranges', 'Bananas', 'Grapes', 'Pineapples'], colors)):
    heights = data[i]
    starts = data_cum[i] - heights
    ax.bar(labels, heights, bottom=starts, width=bar_width, label=colname, color=color)

# Customize the plot
ax.set_ylabel('Percentage of Fruit Consumption')
ax.set_title('Annual Fruit Consumption', pad=20)
ax.legend(loc='upper right')

plt.tight_layout()
plt.show()