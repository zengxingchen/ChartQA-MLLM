
import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    [15, 25, 35, 25],
    [20, 30, 25, 25],
    [30, 20, 25, 25],
    [35, 15, 25, 25],
    [25, 30, 20, 25],
    [20, 25, 35, 20],
    [15, 30, 25, 30],
    [30, 20, 20, 30]
])

categories = ["2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027"]
labels = ["Technology", "Ethics", "History", "Health"]
colors = ["#4e79a7", "#f28e2b", "#76b7b2", "#e15759"]

data_cumsum = data.cumsum(axis=1)
fig, ax = plt.subplots(figsize=(10, 8))

for i, (colname, color) in enumerate(zip(labels, colors)):
    heights = data[:, i]
    starts = data_cumsum[:, i] - heights
    ax.bar(categories, heights, bottom=starts, width=0.7, label=colname, color=color)

ax.set_ylabel('Percentage')
ax.set_xlabel('Year')
ax.set_title('Trends in Various Topics Over the Years')
ax.legend(ncol=1, bbox_to_anchor=(1, 1), loc='upper left', fontsize='small')

plt.show()