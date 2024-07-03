
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Chicken Breast', 'Salmon', 'Almonds', 'Broccoli', 'Apple', 'Milk', 'Cheese', 'Yogurt', 'Bread', 'Egg', 'Avocado', 'Tofu', 'Rice', 'Beans']
protein = [80, 70, 13, 30, 2, 21, 25, 24, 10, 35, 5, 40, 7, 25]
carbohydrates = [0, 0, 15, 60, 95, 49, 3, 50, 85, 2, 10, 8, 90, 65]
fat = [20, 30, 72, 10, 3, 30, 72, 26, 5, 63, 85, 52, 3, 10]

# Parameters
bar_width = 0.5
fig_width = 12
fig_height = 8

# Colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Stack bar chart
fig, ax = plt.subplots(figsize=(fig_width, fig_height))
bar1 = np.array(protein)
bar2 = np.array(carbohydrates)
bar3 = np.array(fat)

bars = np.vstack([bar1, bar2, bar3])
category_positions = np.arange(len(categories))

# Create the bars
ax.barh(category_positions, bars[0], color=colors[0], edgecolor='white', height=bar_width, label='Protein (%)')
ax.barh(category_positions, bars[1], left=bars[0], color=colors[1], edgecolor='white', height=bar_width, label='Carbohydrates (%)')
ax.barh(category_positions, bars[2], left=bars[0]+bars[1], color=colors[2], edgecolor='white', height=bar_width, label='Fat (%)')

# Y-axis labels
ax.set_yticks(category_positions)
ax.set_yticklabels(categories)

# Chart title and labels
ax.set_title('Macronutrient Composition of Various Foods', pad=20)
ax.set_xlabel('Percentage')
ax.set_ylabel('Food Items')

# Legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=3)

# Layout
plt.tight_layout()

# Show the plot
plt.show()