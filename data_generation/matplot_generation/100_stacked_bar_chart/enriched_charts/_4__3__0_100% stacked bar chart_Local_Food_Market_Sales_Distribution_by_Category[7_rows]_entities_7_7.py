
import matplotlib.pyplot as plt
import numpy as np

# Data
sectors = ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023', 'Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024']
categories = ['Technology', 'Healthcare', 'Finance', 'Energy', 'Consumer Goods']
data = np.array([
    [25, 20, 15, 10, 30],
    [30, 15, 20, 10, 25],
    [20, 25, 25, 15, 15],
    [22, 18, 28, 12, 20],
    [28, 22, 15, 15, 20],
    [25, 20, 22, 18, 15],
    [20, 15, 30, 20, 15],
    [18, 25, 20, 22, 15]
])

# Plotting
fig, ax = plt.subplots(figsize=(10, 12))
bar_width = 0.6

# Colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Create stacked bar chart
bottoms = np.zeros(len(sectors))
for i in range(data.shape[1]):
    ax.bar(sectors, data[:, i], bottom=bottoms, width=bar_width, color=colors[i], label=categories[i])
    bottoms += data[:, i]

# Add legend
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

# Add title and labels
ax.set_title('Market Share by Sector', pad=20)
ax.set_ylabel('Percentage')
ax.set_xlabel('Quarters')

# Show plot
plt.tight_layout()
plt.show()