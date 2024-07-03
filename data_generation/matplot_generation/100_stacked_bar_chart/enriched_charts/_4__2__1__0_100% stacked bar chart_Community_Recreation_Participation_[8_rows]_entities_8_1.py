
import matplotlib.pyplot as plt
import numpy as np

# Data for the percentage stacked bar chart
labels = ['USA', 'China', 'India', 'Germany', 'Brazil']
years = ['2015', '2020', '2025', '2030']
data = np.array([
    [20, 25, 30, 35],   # USA
    [30, 28, 25, 20],   # China
    [15, 20, 22, 25],   # India
    [10, 12, 15, 18],   # Germany
    [25, 15, 8, 7]      # Brazil
])

data_cum = data.cumsum(axis=0)

# Colors for each year
colors = ['#ff6666', '#ffcc99', '#66b3ff', '#99ff99']

# Create figure and axes
fig, ax = plt.subplots(figsize=(8, 12))

# Plot bars
for i, (colname, color) in enumerate(zip(years, colors)):
    heights = data[:, i]
    starts = data_cum[:, i] - heights
    ax.bar(labels, heights, bottom=starts, width=0.5, label=colname, color=color)

# Add labels, title, legend, and format
ax.set_ylabel('Percentage')
ax.set_title('Market Share by Country and Year')
ax.legend(ncol=1, bbox_to_anchor=(1, 1), loc='upper left', fontsize='small')

# Show plot
plt.tight_layout()
plt.show()