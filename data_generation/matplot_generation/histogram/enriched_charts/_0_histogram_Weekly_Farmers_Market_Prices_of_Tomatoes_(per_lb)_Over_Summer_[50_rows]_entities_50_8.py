
import matplotlib.pyplot as plt
import numpy as np

# Data points
temperatures = np.array([
    12, 14, 15, 13, 17, 18, 19, 21, 22, 23,
    20, 18, 18, 17, 15, 16, 15, 14, 13, 14,
    15, 18, 19, 21, 25, 24, 22, 21, 19, 17, 16
])

# Parameters for the histogram
bin_width = 1
bins = np.arange(min(temperatures) - bin_width/2, max(temperatures) + bin_width/2, bin_width)

fig, ax = plt.subplots(figsize=(14, 8))  # Change width and height of the chart
ax.hist(temperatures, bins=bins, orientation='horizontal', color='#FF5733', rwidth=0.85)  # Vertical chart, modify color and width

# Add titles and labels
plt.title('Distribution of Average Daily Temperatures Over a Month', fontsize=16)
plt.xlabel('Frequency', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)

# Customize the grid
plt.grid(True, linestyle='--', linewidth=0.5, color='#aaaaaa')

# Customize the ticks
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Show the plot
plt.show()