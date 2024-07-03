
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']
tech = [20, 25, 30, 35, 40]
design = [30, 25, 20, 15, 10]
marketing = [15, 20, 25, 30, 35]
sales = [25, 20, 15, 10, 5]
hr = [10, 10, 10, 10, 10]

# Stack data
data = np.array([tech, design, marketing, sales, hr])
data_cum = data.cumsum(axis=0)

# Color scheme
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF']

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

categories = np.array(categories)
bar_width = 0.6

for i, color in enumerate(colors):
    heights = data[i]
    starts = data_cum[i] - heights
    ax.barh(categories, heights, left=starts, height=bar_width, color=color)

# Add title and labels
ax.set_title('Quarterly Departmental Contribution', pad=20)
ax.set_xlabel('Percentage (%)')
ax.set_ylabel('Quarters')

# Add legend
ax.legend(['Tech', 'Design', 'Marketing', 'Sales', 'HR'], bbox_to_anchor=(1.05, 1), loc='upper left')

# Show plot
plt.tight_layout()
plt.show()