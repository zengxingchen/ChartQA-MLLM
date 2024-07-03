
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['AI Research', 'Quantum Computing', 'Renewable Energy', 'Biotech', 'Space Exploration']
years = ['2018', '2019', '2020', '2021', '2022']
data = np.array([
    [20, 30, 35, 40, 45],
    [15, 20, 25, 30, 35],
    [25, 30, 20, 25, 30],
    [10, 15, 20, 10, 5],
    [30, 5, 0, 5, 10]
])

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#FFC300']

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))
width = 0.5

# Stacking bars horizontally
for i in range(len(data)):
    if i == 0:
        ax.barh(years, data[i], color=colors[i], edgecolor='white', height=width)
    else:
        ax.barh(years, data[i], left=np.sum(data[:i], axis=0), color=colors[i], edgecolor='white', height=width)

# Title and labels
ax.set_title('Investment in Future Technologies (2018-2022)', fontsize=16)
ax.set_xlabel('Percentage (%)')
ax.set_ylabel('Years')
ax.legend(categories, bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# Show plot
plt.tight_layout()
plt.show()