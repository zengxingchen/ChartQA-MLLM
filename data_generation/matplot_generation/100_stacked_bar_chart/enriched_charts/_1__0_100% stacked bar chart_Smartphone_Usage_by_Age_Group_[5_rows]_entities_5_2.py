
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
data = np.array([
    [20, 30, 25, 25],
    [25, 20, 30, 25],
    [30, 25, 20, 25],
    [35, 20, 25, 20],
    [20, 35, 25, 20],
    [25, 25, 25, 25],
    [30, 20, 25, 25],
    [35, 25, 20, 20],
    [25, 30, 25, 20],
    [30, 20, 30, 20]
])

# Normalize data
data_cum = data.cumsum(axis=1)
data_sum = data.sum(axis=1)
data_normalized = data / data_sum[:, np.newaxis]

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#F3FF33']

# Plot
fig, ax = plt.subplots(figsize=(10, 7))
bar_width = 0.7

for i in range(len(categories)):
    if i == 0:
        ax.barh(years, data_normalized[:, i], color=colors[i], edgecolor='white', height=bar_width, label=categories[i])
    else:
        ax.barh(years, data_normalized[:, i], left=data_normalized[:, :i].sum(axis=1), color=colors[i], edgecolor='white', height=bar_width, label=categories[i])

# Title and labels
ax.set_title('Distribution of Data Across Categories Over Years', pad=20)
ax.set_xlabel('Percentage')
ax.set_ylabel('Year')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=len(categories))

# Show plot
plt.tight_layout()
plt.show()