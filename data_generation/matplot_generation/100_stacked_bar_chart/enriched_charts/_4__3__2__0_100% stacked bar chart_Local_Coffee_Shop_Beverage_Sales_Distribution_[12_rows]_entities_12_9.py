
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['AI', 'Blockchain', 'IoT', 'AR/VR', 'Quantum Computing', '3D Printing']
years = ['2018', '2019', '2020', '2021', '2022', '2023']
data = np.array([
    [15, 20, 25, 30, 35, 40],
    [20, 15, 20, 25, 30, 35],
    [25, 30, 35, 40, 45, 50],
    [10, 15, 10, 15, 20, 25],
    [5, 10, 15, 10, 15, 20],
    [25, 10, 15, 20, 15, 30]
])

# Normalize the data to 100%
data = data / data.sum(axis=0) * 100

# Colors
colors = ['#0072B2', '#D55E00', '#F0E442', '#CC79A7', '#56B4E9', '#009E73']

# Plot
fig, ax = plt.subplots(figsize=(12, 8))
width = 0.7  # Bar width
x = np.arange(len(years))

bottom = np.zeros(len(years))
for i in range(len(categories)):
    ax.bar(x, data[i], bottom=bottom, color=colors[i], edgecolor='white', width=width)
    bottom += data[i]

# Add title and labels
ax.set_title('Adoption Rates of Emerging Technologies Over the Years', fontsize=18, pad=20)
ax.set_ylabel('Percentage (%)', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=12)
ax.legend(categories, bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12)
plt.tight_layout()

plt.show()