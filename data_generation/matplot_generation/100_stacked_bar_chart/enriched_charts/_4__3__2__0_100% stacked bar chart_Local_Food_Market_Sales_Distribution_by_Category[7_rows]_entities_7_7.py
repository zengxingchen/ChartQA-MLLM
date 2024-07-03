
import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031', '2032']
category_a = [12, 14, 20, 25, 30, 36, 40, 45, 50, 58, 60, 65, 70]
category_b = [18, 22, 18, 20, 26, 22, 32, 28, 30, 18, 22, 25, 20]
category_c = [28, 32, 30, 25, 22, 22, 18, 20, 10, 12, 8, 5, 5]
category_d = [42, 32, 32, 30, 22, 20, 10, 7, 10, 12, 10, 5, 5]

# Create a 2D array of the data for stacking
data = np.array([category_a, category_b, category_c, category_d])

# Normalize data to 100% for stacked bar chart
data_percentage = data / data.sum(axis=0) * 100

# Color codes
colors = ['#FF5733', '#33FF57', '#3357FF', '#F7DC6F']

# Plot
fig, ax = plt.subplots(figsize=(12, 9))

# Create stacked bar chart
bars = []
for i in range(data_percentage.shape[0]):
    bars.append(ax.bar(labels, data_percentage[i], bottom=np.sum(data_percentage[:i], axis=0), color=colors[i], width=0.6))

# Add legend and title
ax.legend(bars, ['Undergraduate', 'Graduate', 'Doctorate', 'Post-Doctorate'], loc='upper left', bbox_to_anchor=(1, 1))
ax.set_title('Student Enrollment by Education Level Over Years')

# Labels and grid
ax.set_ylabel('Percentage')
ax.set_xlabel('Year')
ax.grid(True)

plt.tight_layout()
plt.show()