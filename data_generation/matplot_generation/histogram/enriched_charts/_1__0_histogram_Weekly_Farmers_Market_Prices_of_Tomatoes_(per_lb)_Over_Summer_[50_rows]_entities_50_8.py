
import matplotlib.pyplot as plt
import numpy as np

# Data points
sales_revenue = np.array([
    5, 6, 8, 7, 12, 11, 10, 15, 14, 13,
    12, 11, 10, 14, 16, 17, 18, 19, 20, 21,
    22, 23, 21, 19, 17, 16, 15, 14, 13, 12,
    11, 10, 9, 8, 7, 6, 5, 4, 3, 2,
    3, 4, 5, 7, 8, 9, 10, 12, 11, 10,
    14, 16, 15, 14, 13, 12, 11, 10, 9, 8
])

# Parameters for the histogram
bin_height = 1
bins = np.arange(min(sales_revenue) - bin_height/2, max(sales_revenue) + bin_height/2, bin_height)

fig, ax = plt.subplots(figsize=(10, 12))  # Change width and height of the chart
ax.hist(sales_revenue, bins=bins, orientation='vertical', color='#3399FF', rwidth=0.75)  # Horizontal chart, modify color and width

# Add titles and labels
plt.title('Distribution of Monthly Sales Revenue Over Two Years', fontsize=16)
plt.xlabel('Sales Revenue ($1000s)', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

# Customize the grid
plt.grid(True, linestyle='--', linewidth=0.5, color='#aaaaaa')

# Customize the ticks
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Show the plot
plt.show()