
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Housing', 'Food', 'Transportation', 'Entertainment', 'Healthcare']
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
data = np.array([
    [30, 25, 15, 20, 10],
    [28, 27, 15, 20, 10],
    [27, 25, 18, 20, 10],
    [26, 24, 20, 20, 10],
    [25, 24, 22, 19, 10],
    [23, 26, 20, 21, 10],
    [22, 25, 23, 20, 10],
    [21, 27, 22, 20, 10],
    [25, 26, 20, 19, 10],
    [30, 24, 18, 18, 10],
    [32, 22, 19, 17, 10],
    [31, 23, 17, 19, 10]
])

# Normalize data to sum up to 100%
data_cum = data.cumsum(axis=1)
data_cum = data_cum / data_cum[:, -1][:, None] * 100

# Colors for each category
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

# Plot
fig, ax = plt.subplots(figsize=(10, 8))  # Change width and height reasonably

bar_width = 0.85  # Change the band width for bars

# Create horizontal bars
for i, (colname, color) in enumerate(zip(categories, colors)):
    heights = data_cum[:, i] if i == 0 else data_cum[:, i] - data_cum[:, i-1]
    ax.barh(months, heights, color=color, edgecolor='white', height=bar_width, 
            label=colname, left=(0 if i == 0 else data_cum[:, i-1]))

# Add x ticks
ax.set_yticks(np.arange(len(months)))
ax.set_yticklabels(months)

# Add x labels to the bars
for i in ax.patches:
    ax.text(i.get_width()+1, i.get_y()+i.get_height()/2., 
            f'{i.get_width():.1f}%', ha='center', va='center')

# Add a legend
ax.legend(ncol=len(categories), bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')

# Set the title
ax.set_title('Monthly Expense Distribution')

plt.show()