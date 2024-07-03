import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030']
category_a = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
category_b = [20, 25, 15, 20, 25, 20, 30, 25, 30, 20, 25]
category_c = [30, 30, 35, 30, 25, 25, 20, 20, 10, 15, 10]
category_d = [40, 30, 30, 25, 20, 20, 10, 10, 10, 10, 5]

# Create a 2D array of the data for stacking
data = np.array([category_a, category_b, category_c, category_d])

# Normalize data to 100% for stacked bar chart
data_percentage = data / data.sum(axis=0) * 100

# Color codes
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']

# Plot
fig, ax = plt.subplots(figsize=(10, 8))

# Create stacked bar chart
bars = []
for i in range(data_percentage.shape[0]):
    bars.append(ax.barh(labels, data_percentage[i], left=np.sum(data_percentage[:i], axis=0), color=colors[i], height=0.6))

# Add legend and title
ax.legend(bars, ['Category A', 'Category B', 'Category C', 'Category D'], loc='upper right')
ax.set_title('Category Distribution Over Years')

# Labels and grid
ax.set_xlabel('Percentage')
ax.set_ylabel('Year')
ax.grid(True)

plt.show()