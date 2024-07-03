
import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    [15, 35, 30, 20],
    [25, 20, 35, 20],
    [30, 25, 20, 25],
    [20, 30, 25, 25],
    [25, 25, 30, 20],
    [35, 20, 25, 20]
])

categories = ['2020', '2021', '2022', '2023', '2024', '2025']
labels = ['Science Fiction', 'Fantasy', 'Mystery', 'Non-Fiction']
colors = ['#6A5ACD', '#FF4500', '#32CD32', '#FFD700']

data_cum = data.cumsum(axis=0)
category_width = 0.8

fig, ax = plt.subplots(figsize=(10, 14))

for i, (colname, color) in enumerate(zip(labels, colors)):
    heights = data[:, i]
    starts = data_cum[:, i] - heights
    ax.bar(categories, heights, bottom=starts, width=category_width, label=colname, color=color)

ax.set_ylabel('Percentage')
ax.set_title('Book Genre Popularity Over Time', pad=20)
ax.legend(loc='upper right')
plt.tight_layout()
plt.show()