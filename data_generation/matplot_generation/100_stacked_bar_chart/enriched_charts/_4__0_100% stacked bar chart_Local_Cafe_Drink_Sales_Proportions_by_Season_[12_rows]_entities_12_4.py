
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Marketing', 'R&D', 'Operations', 'Customer Support', 'Miscellaneous']
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
data = np.array([
    [20, 18, 22, 19, 21, 24, 23, 25, 26, 22, 20, 21],
    [25, 27, 24, 26, 25, 22, 24, 23, 24, 25, 27, 28],
    [15, 17, 16, 15, 14, 15, 14, 15, 13, 12, 13, 14],
    [30, 28, 29, 31, 30, 32, 31, 29, 30, 32, 31, 29],
    [10, 10, 9, 9, 10, 7, 8, 8, 7, 9, 9, 8]
])

# Normalize data to sum up to 100%
data_cum = data.cumsum(axis=0)
data_cum = data_cum / data_cum[-1, :]

# Colors for each category
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#EE82EE']

# Plot
fig, ax = plt.subplots(figsize=(12, 8))  # Change width and height reasonably

bar_height = 0.85  # Change the band height for bars

# Create vertical bars
for i, (colname, color) in enumerate(zip(categories, colors)):
    heights = data_cum[i, :] if i == 0 else data_cum[i, :] - data_cum[i-1, :]
    ax.bar(months, heights, color=color, edgecolor='white', width=bar_height, 
           label=colname, bottom=(0 if i == 0 else data_cum[i-1, :]))

# Add y ticks
ax.set_xticks(np.arange(len(months)))
ax.set_xticklabels(months, rotation=45, ha='right')

# Add y labels to the bars
for i in ax.patches:
    ax.text(i.get_x() + i.get_width() / 2., i.get_height() + i.get_y(), 
            f'{i.get_height() * 100:.1f}%', ha='center', va='bottom')

# Add a legend
ax.legend(ncol=1, bbox_to_anchor=(1, 1), loc='upper left', fontsize='small')

# Set the title
ax.set_title('Monthly Department Expense Distribution', pad=20)

plt.tight_layout()
plt.show()