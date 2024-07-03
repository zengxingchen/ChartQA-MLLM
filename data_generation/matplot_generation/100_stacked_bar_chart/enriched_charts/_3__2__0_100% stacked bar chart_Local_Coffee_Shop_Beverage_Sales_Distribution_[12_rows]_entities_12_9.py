import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Reading', 'Exercise', 'Travel', 'Cooking']
years = ['2020', '2021', '2022']
data = np.array([
    [20, 25, 30],
    [30, 20, 25],
    [25, 35, 20],
    [25, 20, 25]
])

# Normalize the data to 100%
data = data / data.sum(axis=0) * 100

# Colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
width = 0.6  # Bar width
x = np.arange(len(years))

for i in range(len(categories)):
    if i == 0:
        ax.barh(x, data[i], color=colors[i], edgecolor='white', height=width)
        bottom = data[i]
    else:
        ax.barh(x, data[i], left=bottom, color=colors[i], edgecolor='white', height=width)
        bottom += data[i]

# Add title and labels
ax.set_title('Changes in Leisure Activities Over the Years', fontsize=16, pad=15)
ax.set_xlabel('Percentage (%)', fontsize=12)
ax.set_yticks(x)
ax.set_yticklabels(years, fontsize=12)
ax.legend(categories, bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12)
plt.tight_layout()

plt.show()