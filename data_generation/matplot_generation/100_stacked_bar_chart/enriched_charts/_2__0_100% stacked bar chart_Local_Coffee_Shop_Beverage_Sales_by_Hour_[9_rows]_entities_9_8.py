
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Country A', 'Country B', 'Country C', 'Country D', 'Country E', 
              'Country F', 'Country G', 'Country H', 'Country I', 'Country J']
renewable_energy = [30, 25, 35, 20, 40, 30, 25, 35, 30, 20]
carbon_emissions = [20, 30, 15, 25, 20, 30, 35, 25, 25, 30]
water_usage = [25, 20, 30, 25, 20, 25, 20, 15, 30, 30]
biodiversity = [25, 25, 20, 30, 20, 15, 20, 25, 15, 20]

# Stacked bar chart data
data = np.array([renewable_energy, carbon_emissions, water_usage, biodiversity])
data_cum = data.cumsum(axis=0)

# Category names and colors
category_names = ['Renewable Energy', 'Carbon Emissions', 'Water Usage', 'Biodiversity']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Plot
fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.5

# Plot each layer of the bar chart
for i, (colname, color) in enumerate(zip(category_names, colors)):
    widths = data[i]
    starts = data_cum[i] - widths
    ax.barh(categories, widths, left=starts, height=bar_width, label=colname, color=color)

# Add labels, title, and legend
ax.set_xlabel('Percentage')
ax.set_title('Environmental Indicators by Country', loc='left')
ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')

plt.tight_layout()
plt.show()