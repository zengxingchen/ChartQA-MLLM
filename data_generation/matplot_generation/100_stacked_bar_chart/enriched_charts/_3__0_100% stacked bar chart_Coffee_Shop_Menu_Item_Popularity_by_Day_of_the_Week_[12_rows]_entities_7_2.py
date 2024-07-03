
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Electronics', 'Clothing', 'Food', 'Home', 'Other']
years = ['2019', '2020', '2021', '2022', '2023']
data = np.array([
    [15, 20, 30, 25, 10],
    [20, 25, 25, 20, 10],
    [25, 15, 20, 30, 10],
    [30, 20, 15, 25, 10],
    [10, 30, 20, 30, 10]
])

# Colors
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

# Stacked bar chart
for i in range(data.shape[1]):
    bottom = np.sum(data[:, :i], axis=1)
    ax.barh(years, data[:, i], left=bottom, color=colors[i], edgecolor='white', height=0.6)

# Title and labels
ax.set_title('Sales Distribution by Category (2019-2023)', loc='center', pad=20)
ax.set_xlabel('Percentage')
ax.set_ylabel('Year')

# Legend
ax.legend(categories, bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()