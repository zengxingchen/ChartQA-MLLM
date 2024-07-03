
import matplotlib.pyplot as plt
import numpy as np

regions = [
    '2015', '2016', '2017', '2018', '2019',
    '2020', '2021', '2022', '2023', '2024'
]

north = np.array([15, 25, 20, 30, 25, 20, 35, 25, 30, 20])
south = np.array([20, 15, 30, 25, 30, 20, 25, 30, 20, 35])
east = np.array([25, 20, 25, 20, 20, 35, 20, 25, 30, 25])
west = np.array([40, 40, 25, 25, 25, 25, 20, 20, 20, 20])

bar_width = 0.6

fig, ax = plt.subplots(figsize=(12, 10))

ax.bar(regions, north, color='#FF5733', edgecolor='white', width=bar_width)
ax.bar(regions, south, bottom=north, color='#33FF57', edgecolor='white', width=bar_width)
ax.bar(regions, east, bottom=north + south, color='#3357FF', edgecolor='white', width=bar_width)
ax.bar(regions, west, bottom=north + south + east, color='#FF33FF', edgecolor='white', width=bar_width)

ax.set_ylabel('Percentage')
ax.set_title('Distribution of Revenue by Region (2015-2024)', pad=20)
ax.legend(['North', 'South', 'East', 'West'], bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()