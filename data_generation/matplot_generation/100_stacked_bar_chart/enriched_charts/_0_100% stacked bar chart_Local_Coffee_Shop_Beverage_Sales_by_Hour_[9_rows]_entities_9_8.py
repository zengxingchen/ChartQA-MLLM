
import matplotlib.pyplot as plt
import numpy as np

# Data
quarters = ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023']
hardware = np.array([25000, 30000, 20000, 40000])
software = np.array([15000, 20000, 25000, 30000])
services = np.array([5000, 7000, 8000, 10000])
accessories = np.array([2500, 3000, 3500, 5000])
total_revenue = hardware + software + services + accessories
hardware_percentage = (hardware / total_revenue) * 100
software_percentage = (software / total_revenue) * 100
services_percentage = (services / total_revenue) * 100
accessories_percentage = (accessories / total_revenue) * 100

# Plot
fig, ax = plt.subplots(figsize=(10, 6))  # Change the size of the chart

bar_width = 0.6  # Change width of bars
bar_positions = np.arange(len(quarters))  # Horizontal bar chart requires bar positions

# Create stacked bars
rects1 = ax.barh(bar_positions, hardware_percentage, bar_width, color='#FF5733', label='Hardware')
rects2 = ax.barh(bar_positions, software_percentage, bar_width, left=hardware_percentage, color='#33FF57', label='Software')
rects3 = ax.barh(bar_positions, services_percentage, bar_width, left=hardware_percentage + software_percentage, color='#3357FF', label='Services')
rects4 = ax.barh(bar_positions, accessories_percentage, bar_width, left=hardware_percentage + software_percentage + services_percentage, color='#F9FF33', label='Accessories')

# Labels, title and custom x-axis tick labels
ax.set_xlabel('Percentage (%)')
ax.set_title('Quarterly Revenue Breakdown by Product Category')
ax.set_yticks(bar_positions)
ax.set_yticklabels(quarters)
ax.set_xlim(0, 100)  # So that 100% is the max x-axis value

# Adding a legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Display chart
plt.tight_layout()  # Adjust the padding between and around subplots.
plt.show()