
import matplotlib.pyplot as plt
import squarify  # pip install squarify (algorithm for treemap)

# Data
categories = ['Fruits', 'Vegetables', 'Grains', 'Protein Foods', 'Dairy', 'Oils', 'Sweets', 'Beverages', 'Nuts & Seeds', 'Herbs & Spices']
calories = [45, 35, 60, 50, 40, 20, 25, 30, 15, 10]

# Color Scheme in HEX
colors = ['#FFB6C1', '#98FB98', '#FFD700', '#D2691E', '#ADD8E6', '#FF4500', '#DA70D6', '#4169E1', '#8B4513', '#556B2F']

# Creating a figure to accommodate a larger treemap
fig, ax = plt.subplots(1, figsize=(16, 10))

# Creating the treemap
squarify.plot(sizes=calories, label=categories, color=colors, alpha=0.8, ax=ax)

# Title of the treemap
plt.title('Calorie Distribution in Different Food Categories', fontsize=18)

# Removing the axes for better aesthetics
plt.axis('off')

# Display the plot
plt.show()