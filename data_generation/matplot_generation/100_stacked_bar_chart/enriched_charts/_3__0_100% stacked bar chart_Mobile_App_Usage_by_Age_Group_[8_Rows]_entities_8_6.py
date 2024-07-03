
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Fruits', 'Vegetables', 'Grains', 'Dairy', 'Meat', 'Nuts', 'Seafood', 'Legumes', 'Sweets', 'Beverages']
protein = [10, 20, 15, 20, 30, 15, 25, 25, 5, 0]
carbohydrates = [70, 60, 70, 50, 0, 10, 0, 50, 90, 80]
fats = [5, 5, 10, 25, 60, 70, 60, 10, 3, 0]
vitamins = [10, 10, 3, 3, 5, 3, 10, 10, 1, 10]
minerals = [5, 5, 2, 2, 5, 2, 5, 5, 1, 10]

# Stack data
data = np.array([protein, carbohydrates, fats, vitamins, minerals])
data_cum = data.cumsum(axis=0)

# Category colors
category_colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700']

# Figure and Axes
fig, ax = plt.subplots(figsize=(10, 7))

# Plotting
labels = ['Protein', 'Carbohydrates', 'Fats', 'Vitamins', 'Minerals']
for i, (colname, color) in enumerate(zip(labels, category_colors)):
    widths = data[i]
    starts = data_cum[i] - widths
    ax.barh(categories, widths, left=starts, height=0.6, label=colname, color=color)

# Customization
ax.set_title('Nutritional Composition of Various Food Categories', fontsize=15, pad=20)
ax.legend(ncol=5, bbox_to_anchor=(0.5, -0.1), loc='upper center', fontsize='small')
ax.set_xlabel('Percentage (%)')
ax.set_ylabel('Food Categories')

# Display
plt.tight_layout()
plt.show()