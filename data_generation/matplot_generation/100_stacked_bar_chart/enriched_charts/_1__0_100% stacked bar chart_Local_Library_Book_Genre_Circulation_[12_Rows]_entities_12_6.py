
import matplotlib.pyplot as plt
import numpy as np

# Data
fruits = ['Apple', 'Banana', 'Orange', 'Strawberry', 'Grapes', 'Mango', 'Blueberry', 'Pineapple', 'Watermelon', 'Peach']
carbohydrates = np.array([13, 22, 12, 8, 16, 15, 14, 13, 7.6, 10])
proteins = np.array([0.3, 1.1, 0.9, 0.8, 0.6, 0.5, 0.7, 0.5, 0.6, 0.9])
fats = np.array([0.2, 0.3, 0.2, 0.4, 0.2, 0.2, 0.3, 0.1, 0.2, 0.3])
fibers = np.array([2.4, 2.6, 2.4, 2.0, 0.9, 1.6, 2.4, 1.4, 0.4, 1.5])

# Normalizing data to percentage
totals = carbohydrates + proteins + fats + fibers
carbohydrates = carbohydrates / totals * 100
proteins = proteins / totals * 100
fats = fats / totals * 100
fibers = fibers / totals * 100

# Plot
fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.5
x = np.arange(len(fruits))

ax.barh(x, carbohydrates, color='#FF9999', edgecolor='grey', height=bar_width, label='Carbohydrates')
ax.barh(x, proteins, left=carbohydrates, color='#66B3FF', edgecolor='grey', height=bar_width, label='Proteins')
ax.barh(x, fats, left=carbohydrates + proteins, color='#99FF99', edgecolor='grey', height=bar_width, label='Fats')
ax.barh(x, fibers, left=carbohydrates + proteins + fats, color='#FFCC99', edgecolor='grey', height=bar_width, label='Fibers')

# Labels and Title
ax.set_xlabel('Percentage')
ax.set_title('Nutritional Composition of Different Fruits', pad=20)
ax.set_yticks(x)
ax.set_yticklabels(fruits)
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1.15))

plt.tight_layout()
plt.show()