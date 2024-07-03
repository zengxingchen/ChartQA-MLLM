
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Protein', 'Fat', 'Carbohydrate', 'Vitamins']
data = np.array([
    [2, 1, 95, 2],
    [3, 0.5, 95.5, 1],
    [45, 5, 45, 5],
    [90, 10, 0, 0],
    [60, 40, 0, 0],
    [13, 7, 78, 2],
    [21, 50, 20, 9],
    [20, 5, 70, 5],
    [50, 45, 0, 5],
    [30, 5, 60, 5]
])

food_items = ['Apple', 'Banana', 'Broccoli', 'Chicken Breast', 'Salmon', 'Oats', 'Almonds', 'Milk', 'Eggs', 'Spinach']

# Normalize data to 100%
data = data / data.sum(axis=1)[:, None] * 100

# Colors
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']

# Plot
fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.5
indices = np.arange(len(food_items))

bottoms = np.zeros(len(food_items))
for i, category in enumerate(categories):
    ax.barh(indices, data[:, i], bar_width, left=bottoms, color=colors[i], label=category)
    bottoms += data[:, i]

# Title and labels
ax.set_title('Nutritional Composition of Different Food Items')
ax.set_xlabel('Percentage')
ax.set_yticks(indices)
ax.set_yticklabels(food_items)
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

plt.tight_layout()
plt.show()