
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Breakfast', 'Lunch', 'Dinner', 'Snacks']
vegetables = [20, 25, 30, 10]
fruits = [30, 20, 20, 40]
grains = [10, 15, 20, 5]
proteins = [30, 30, 20, 15]
dairy = [10, 10, 10, 30]

# Create numpy array for stack bars
data = np.array([vegetables, fruits, grains, proteins, dairy])

# Colors for each stack
colors = ['#FF6347', '#FFD700', '#8A2BE2', '#3CB371', '#4682B4']

# Create horizontal stacked bar chart
fig, ax = plt.subplots(figsize=(12, 6))

# Stacked bars
bars = ax.barh(categories, data[0], color=colors[0], height=0.5)
for i in range(1, data.shape[0]):
    bars = ax.barh(categories, data[i], left=np.sum(data[:i], axis=0), color=colors[i], height=0.5)

# Add legend and title
ax.legend(['Vegetables', 'Fruits', 'Grains', 'Proteins', 'Dairy'], bbox_to_anchor=(1.05, 1), loc='upper left')
ax.set_title('Food Consumption by Meal Type', fontsize=16, pad=20)

# Show plot
plt.tight_layout()
plt.show()