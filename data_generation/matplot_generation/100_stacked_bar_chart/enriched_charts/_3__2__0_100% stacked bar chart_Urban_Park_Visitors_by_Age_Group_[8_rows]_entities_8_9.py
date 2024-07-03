
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Sustainable Energy', 'Carbon Emissions', 'Environmental Impact']
subcategories = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass', 'Transport', 'Industry', 'Agriculture', 'Residential', 'Commercial', 'Air Quality', 'Water Pollution', 'Deforestation', 'Soil Degradation', 'Biodiversity Loss']
values1 = [20, 35, 25, 15, 5, 40, 25, 35, 30, 20, 45, 30, 25, 20, 15]
values2 = [30, 25, 30, 35, 20, 30, 45, 30, 20, 25, 25, 35, 40, 30, 35]
values3 = [50, 40, 45, 50, 75, 30, 30, 35, 50, 55, 30, 35, 35, 50, 50]

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#F333FF', '#FF33A1', '#FFA533', '#33FFF6', '#A533FF', '#FFF633', '#33FFA5', '#FF3333', '#FF8633', '#33B2FF', '#FF33C4', '#33FFCC']

# Bar width
barWidth = 0.5

# Creating the figure
fig, ax = plt.subplots(figsize=(14, 8))

# Stacked bar chart
bars1 = np.add(values1, values2).tolist()
bars2 = np.add(bars1, values3).tolist()

ax.barh(subcategories, values1, color=colors, edgecolor='grey', height=barWidth)
ax.barh(subcategories, values2, left=values1, color=colors, edgecolor='grey', height=barWidth)
ax.barh(subcategories, values3, left=bars1, color=colors, edgecolor='grey', height=barWidth)

# Title and labels
plt.title('Environmental and Climate Change Factors Distribution', pad=20)
plt.xlabel('Percentage')
plt.ylabel('Factors')
plt.legend(categories, loc='upper right', bbox_to_anchor=(1.15, 1))

# Show the plot
plt.tight_layout()
plt.show()