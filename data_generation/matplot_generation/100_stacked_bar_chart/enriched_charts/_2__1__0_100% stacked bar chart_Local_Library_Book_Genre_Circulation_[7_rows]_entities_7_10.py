import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    [20, 30, 25, 25],
    [25, 25, 30, 20],
    [30, 20, 20, 30],
    [35, 15, 25, 25],
    [25, 30, 30, 15],
    [20, 35, 25, 20]
])

categories = ['2020', '2021', '2022', '2023', '2024', '2025']
labels = ['Science Fiction', 'Fantasy', 'Mystery', 'Non-Fiction']
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']

data_cum = data.cumsum(axis=1)
category_width = 0.8

fig, ax = plt.subplots(figsize=(12, 8))

for i, (colname, color) in enumerate(zip(labels, colors)):
    widths = data[:, i]
    starts = data_cum[:, i] - widths
    ax.barh(categories, widths, left=starts, height=category_width, label=colname, color=color)

ax.set_xlabel('Percentage')
ax.set_title('Book Genre Popularity Over Time')
ax.legend(loc='lower right')
plt.tight_layout()
plt.show()