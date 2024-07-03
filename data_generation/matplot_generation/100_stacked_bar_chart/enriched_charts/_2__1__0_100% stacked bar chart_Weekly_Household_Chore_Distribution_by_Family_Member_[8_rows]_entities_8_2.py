
import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    [20, 30, 25, 25],
    [25, 25, 30, 20],
    [30, 20, 20, 30],
    [35, 15, 15, 35]
])

categories = ["2020", "2021", "2022", "2023"]
labels = ["Technology", "Ethics", "History", "Health"]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]

data_cumsum = data.cumsum(axis=1)
category_colors = plt.colormaps['tab20c'](np.linspace(0.15, 0.85, data.shape[1]))

fig, ax = plt.subplots(figsize=(12, 6))

for i, (colname, color) in enumerate(zip(labels, colors)):
    widths = data[:, i]
    starts = data_cumsum[:, i] - widths
    ax.barh(categories, widths, left=starts, height=0.5, label=colname, color=color)

ax.set_xlabel('Percentage')
ax.set_ylabel('Year')
ax.set_title('Distribution of Interests in Health & Psychology Over Years')
ax.legend(ncol=len(labels), bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')

plt.show()