
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Fruits', 'Vegetables', 'Grains', 'Dairy', 'Meats', 'Nuts', 'Legumes', 'Seafood', 'Sweets', 'Beverages']
protein = [5, 25, 15, 20, 60, 15, 30, 50, 2, 0]
carbs = [90, 60, 75, 55, 0, 20, 50, 5, 95, 95]
fats = [2, 5, 7, 20, 35, 60, 15, 40, 2, 2]
fiber = [3, 10, 3, 5, 5, 5, 5, 5, 1, 3]

# Colors
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']

# Plot
bar_width = 0.6
fig, ax = plt.subplots(figsize=(12, 8))

# Stacked bar chart
ax.barh(categories, protein, color=colors[0], edgecolor='white', height=bar_width)
ax.barh(categories, carbs, left=protein, color=colors[1], edgecolor='white', height=bar_width)
ax.barh(categories, fats, left=np.array(protein)+np.array(carbs), color=colors[2], edgecolor='white', height=bar_width)
ax.barh(categories, fiber, left=np.array(protein)+np.array(carbs)+np.array(fats), color=colors[3], edgecolor='white', height=bar_width)

# Title and labels
ax.set_xlabel('Percentage')
ax.set_title('Macronutrient Composition in Various Food Categories', pad=20)
ax.legend(['Protein', 'Carbs', 'Fats', 'Fiber'], bbox_to_anchor=(1.05, 1), loc='upper left')

# Show plot
plt.tight_layout()
plt.show()