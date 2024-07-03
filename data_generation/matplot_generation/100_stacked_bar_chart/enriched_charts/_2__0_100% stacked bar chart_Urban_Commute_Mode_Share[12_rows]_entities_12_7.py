
import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    [20, 30, 25, 25],
    [35, 25, 15, 25],
    [30, 35, 20, 15],
    [25, 20, 35, 20],
    [20, 25, 30, 25]
])

years = ['2019', '2020', '2021', '2022', '2023']
categories = ['Action', 'Adventure', 'Strategy', 'Role-Playing']
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']

data_cum = data.cumsum(axis=1)
fig, ax = plt.subplots(figsize=(10, 6))

for i, color in enumerate(colors):
    widths = data[:, i]
    starts = data_cum[:, i] - widths
    ax.barh(years, widths, left=starts, height=0.8, label=categories[i], color=color)

ax.set_xlabel('Percentage')
ax.set_ylabel('Year')
ax.set_title('Distribution of Game Genres Over Years', pad=20)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()