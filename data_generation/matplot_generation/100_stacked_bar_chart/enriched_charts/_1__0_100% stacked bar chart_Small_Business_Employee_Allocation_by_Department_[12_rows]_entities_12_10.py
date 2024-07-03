
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Fruits', 'Vegetables', 'Grains', 'Meat', 'Dairy', 'Sweets']
protein = [1, 4, 13, 30, 21, 2]
carbohydrates = [91, 84, 75, 0, 45, 90]
fats = [8, 12, 12, 70, 34, 8]

# Plotting
bar_width = 0.5
index = np.arange(len(categories))

fig, ax = plt.subplots(figsize=(10, 7))
ax.barh(index, protein, bar_width, label='Protein', color='#1f77b4')
ax.barh(index, carbohydrates, bar_width, left=protein, label='Carbohydrates', color='#ff7f0e')
ax.barh(index, fats, bar_width, left=np.array(protein) + np.array(carbohydrates), label='Fats', color='#2ca02c')

# Labels and Titles
ax.set_xlabel('Percentage')
ax.set_title('Nutritional Composition of Various Food Categories')
ax.set_yticks(index)
ax.set_yticklabels(categories)
ax.legend()

# Display the plot
plt.show()