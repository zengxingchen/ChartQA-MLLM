
import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    [25, 35, 15, 25],
    [30, 25, 20, 25],
    [35, 20, 25, 20],
    [40, 30, 10, 20],
    [30, 25, 20, 25],
    [25, 30, 25, 20],
    [35, 20, 30, 15]
])

years = ['2019', '2020', '2021', '2022', '2023', '2024', '2025']
categories = ['Cardio', 'Strength', 'Flexibility', 'Balance']
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']

data_cum = data.cumsum(axis=1)
fig, ax = plt.subplots(figsize=(8, 12))

for i, color in enumerate(colors):
    heights = data[:, i]
    starts = data_cum[:, i] - heights
    ax.bar(years, heights, bottom=starts, width=0.8, label=categories[i], color=color)

ax.set_ylabel('Percentage')
ax.set_xlabel('Year')
ax.set_title('Fitness Activity Distribution Over Years', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1))

plt.tight_layout()
plt.show()