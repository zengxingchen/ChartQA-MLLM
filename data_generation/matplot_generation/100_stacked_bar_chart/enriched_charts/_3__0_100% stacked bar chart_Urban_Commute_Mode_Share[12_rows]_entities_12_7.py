
import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['Breakfast', 'Lunch', 'Dinner', 'Snacks']
fruits = [20, 15, 10, 25]
vegetables = [10, 25, 30, 15]
proteins = [15, 20, 30, 20]
grains = [30, 30, 20, 25]
dairy = [25, 10, 10, 15]

# Plot settings
barWidth = 0.5
fig, ax = plt.subplots(figsize=(12, 6))

# Stack the bars
p1 = ax.barh(labels, fruits, color='#FF6F61', edgecolor='white', height=barWidth, label='Fruits')
p2 = ax.barh(labels, vegetables, left=fruits, color='#6B5B95', edgecolor='white', height=barWidth, label='Vegetables')
p3 = ax.barh(labels, proteins, left=np.add(fruits, vegetables), color='#88B04B', edgecolor='white', height=barWidth, label='Proteins')
p4 = ax.barh(labels, grains, left=np.add(fruits, np.add(vegetables, proteins)), color='#F7CAC9', edgecolor='white', height=barWidth, label='Grains')
p5 = ax.barh(labels, dairy, left=np.add(fruits, np.add(vegetables, np.add(proteins, grains))), color='#92A8D1', edgecolor='white', height=barWidth, label='Dairy')

# Add legend and labels
ax.set_xlabel('Percentage of Daily Nutritional Requirements')
ax.set_title('Contribution of Food Groups to Daily Nutrition by Meal')
ax.legend(loc='upper right')

# Display chart
plt.show()