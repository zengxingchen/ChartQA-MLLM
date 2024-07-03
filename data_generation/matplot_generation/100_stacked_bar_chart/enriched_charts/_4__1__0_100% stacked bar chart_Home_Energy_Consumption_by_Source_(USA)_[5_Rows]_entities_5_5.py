
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Philosophy', 'Ethics', 'Metaphysics', 'Epistemology', 'Logic']
A = np.array([10, 15, 20, 25, 30])
B = np.array([15, 10, 25, 20, 30])
C = np.array([20, 30, 15, 35, 25])
D = np.array([25, 45, 40, 20, 15])

# Stack the data
data = np.vstack([A, B, C, D])
data_cum = data.cumsum(axis=0)

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']

# Plot settings
fig, ax = plt.subplots(figsize=(10, 12))

# Bar width
bar_width = 0.6

# Create the stacked bar chart
for i, (colname, color) in enumerate(zip(['A', 'B', 'C', 'D'], colors)):
    heights = data[i]
    starts = data_cum[i] - heights
    ax.bar(categories, heights, bottom=starts, width=bar_width, label=colname, color=color)

# Add labels
ax.set_ylabel('Percentage')
ax.set_title('Philosophy & Ethics: Distribution of Topics', pad=20)
ax.legend(loc='upper right')

plt.show()