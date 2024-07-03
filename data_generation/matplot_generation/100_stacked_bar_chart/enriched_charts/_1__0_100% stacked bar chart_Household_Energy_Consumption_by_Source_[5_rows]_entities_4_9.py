
import matplotlib.pyplot as plt
import numpy as np

# Data
foods = ['Chicken', 'Beef', 'Tofu', 'Salmon', 'Lentils', 'Rice', 'Broccoli', 'Almonds', 'Eggs', 'Yogurt']
protein = np.array([40, 30, 35, 50, 25, 5, 30, 15, 35, 15])
carbs = np.array([0, 0, 5, 0, 60, 85, 60, 15, 1, 20])
fats = np.array([60, 70, 60, 50, 15, 10, 10, 70, 64, 65])

# Stacking the data
bottom1 = protein
bottom2 = protein + carbs

# Colors
colors = ['#FF9999', '#66B2FF', '#99FF99']

# Create horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(foods, protein, color=colors[0], edgecolor='white', height=0.6, label='Protein')
ax.barh(foods, carbs, left=bottom1, color=colors[1], edgecolor='white', height=0.6, label='Carbohydrates')
ax.barh(foods, fats, left=bottom2, color=colors[2], edgecolor='white', height=0.6, label='Fats')

# Add legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3)

# Title and labels
ax.set_title('Nutrient Distribution in Different Foods', pad=20)
ax.set_xlabel('Percentage')
ax.set_ylabel('Food')

# Display the chart
plt.tight_layout()
plt.show()