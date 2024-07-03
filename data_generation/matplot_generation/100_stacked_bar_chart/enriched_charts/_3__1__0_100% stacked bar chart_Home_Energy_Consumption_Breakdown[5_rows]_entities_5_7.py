
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Apple', 'Banana', 'Orange', 'Broccoli', 'Carrot', 'Chicken', 'Beef', 'Salmon', 'Milk', 'Egg']
protein = np.array([1, 1.3, 0.9, 2.8, 0.9, 27, 26, 20, 3.4, 13])
carbohydrates = np.array([25, 27, 21, 7, 10, 0, 0, 0, 5, 1.1])
fat = np.array([0.3, 0.4, 0.1, 0.4, 0.2, 3.6, 15, 13, 1, 11])

# Normalize the data
total = protein + carbohydrates + fat
protein_percent = protein / total * 100
carbohydrates_percent = carbohydrates / total * 100
fat_percent = fat / total * 100

# Stack data
data = [protein_percent, carbohydrates_percent, fat_percent]
labels = ['Protein', 'Carbohydrates', 'Fat']
colors = ['#ff9999','#66b3ff','#99ff99']

# Plotting
fig, ax = plt.subplots(figsize=(10, 8))
width = 0.5  # bar width

# Create stacked bar chart
ax.barh(categories, protein_percent, color=colors[0], edgecolor='white', height=width)
ax.barh(categories, carbohydrates_percent, left=protein_percent, color=colors[1], edgecolor='white', height=width)
ax.barh(categories, fat_percent, left=protein_percent + carbohydrates_percent, color=colors[2], edgecolor='white', height=width)

# Adding title and labels
ax.set_title('Nutritional Composition of Different Foods', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Percentage (%)', fontsize=12)
ax.set_ylabel('Food Items', fontsize=12)

# Adding legend
ax.legend(labels, loc='upper right', bbox_to_anchor=(1.15, 1))

plt.tight_layout()
plt.show()