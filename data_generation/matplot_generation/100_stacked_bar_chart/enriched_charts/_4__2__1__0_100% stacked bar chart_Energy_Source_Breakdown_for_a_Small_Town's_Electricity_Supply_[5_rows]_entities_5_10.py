
import matplotlib.pyplot as plt
import numpy as np

# Data
sectors = ["North America", "South America", "Europe", "Africa", "Asia", "Australia", "Antarctica"]
medicine = [15, 10, 25, 5, 20, 15, 10]
wellness = [20, 15, 10, 10, 30, 15, 0]
research = [25, 20, 30, 15, 15, 25, 5]
education = [10, 15, 20, 40, 10, 15, 10]
technology = [20, 25, 10, 20, 15, 20, 10]
other = [10, 15, 5, 10, 10, 10, 65]

# Bar width
bar_width = 0.7

# Colors
colors = ['#4daf4a', '#377eb8', '#ff7f00', '#984ea3', '#e41a1c', '#ffff33']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 14))

# Stack the bars
bottom = np.zeros(len(sectors))

for data, color in zip([medicine, wellness, research, education, technology, other], colors):
    ax.bar(sectors, data, bottom=bottom, width=bar_width, color=color)
    bottom += data

# Add title and labels
ax.set_title('Investment Distribution in Different Sectors by Region', fontsize=16, pad=20)
ax.set_ylabel('Investment (%)', fontsize=12)
ax.set_xlabel('Region', fontsize=12)

# Add legend
ax.legend(['Medicine', 'Wellness', 'Research', 'Education', 'Technology', 'Other'], loc='upper left', bbox_to_anchor=(1, 1))

# Adjust layout to ensure everything fits without overlapping
plt.tight_layout()

# Show plot
plt.show()