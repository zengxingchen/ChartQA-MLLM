
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023']
apple = [25, 30, 20, 25]
microsoft = [35, 25, 30, 25]
google = [30, 20, 25, 25]
amazon = [10, 25, 25, 25]

# Stacked bar chart data
data = np.array([apple, microsoft, google, amazon])
data_cum = data.cumsum(axis=0)

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#FFD700']

# Plot
fig, ax = plt.subplots(figsize=(12, 8))
categories = np.array(categories)

# Plot bars
for i, (colname, color) in enumerate(zip(['Apple', 'Microsoft', 'Google', 'Amazon'], colors)):
    heights = data[i]
    starts = data_cum[i] - heights
    ax.bar(categories, heights, bottom=starts, width=0.6, label=colname, color=color)

# Add title and legend
ax.set_title('Market Share of Tech Giants in 2023', loc='center', fontsize=18, pad=20)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Adjust the layout
plt.tight_layout()

# Show plot
plt.show()