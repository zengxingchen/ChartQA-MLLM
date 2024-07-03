
import matplotlib.pyplot as plt
import numpy as np

# Data
sectors = ["Electricity and Heat Production", "Transport", "Manufacturing and Construction", "Agriculture", "Commercial and Residential Buildings", "Other Sources"]
energy = [25, 0, 10, 5, 10, 20]
transport = [15, 50, 10, 5, 15, 5]
industry = [30, 10, 60, 10, 10, 15]
agriculture = [10, 5, 5, 65, 5, 10]
buildings = [10, 10, 5, 10, 50, 10]
other = [10, 25, 10, 5, 10, 40]

# Bar width
bar_width = 0.6

# Colors
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Stack the bars
bottom = np.zeros(len(sectors))

for data, color in zip([energy, transport, industry, agriculture, buildings, other], colors):
    ax.barh(sectors, data, left=bottom, height=bar_width, color=color)
    bottom += data

# Add title and labels
ax.set_title('Distribution of Greenhouse Gas Emissions by Sector', fontsize=16)
ax.set_xlabel('Percentage of Total Emissions', fontsize=12)
ax.set_ylabel('Sector', fontsize=12)

# Add legend
ax.legend(['Energy', 'Transport', 'Industry', 'Agriculture', 'Buildings', 'Other'], loc='upper right', bbox_to_anchor=(1.15, 1))

# Adjust layout to ensure everything fits without overlapping
plt.tight_layout()

# Show plot
plt.show()