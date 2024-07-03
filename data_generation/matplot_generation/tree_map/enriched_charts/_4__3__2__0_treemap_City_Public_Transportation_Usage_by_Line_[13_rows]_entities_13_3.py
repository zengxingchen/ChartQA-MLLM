
import matplotlib.pyplot as plt
import squarify

# Data for the treemap
labels = [
    'Fruits', 'Vegetables', 'Dairy', 'Meat', 
    'Grains', 'Beverages', 'Snacks', 'Sweets', 
    'Seafood', 'Nuts', 'Spices', 'Condiments', 
    'Oils', 'Herbs'
]
sizes = [25, 20, 15, 13, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
colors = [
    '#FF6347', '#32CD32', '#FFD700', '#8B4513', 
    '#DAA520', '#4682B4', '#FF4500', '#C71585', 
    '#4169E1', '#8FBC8F', '#D2691E', '#BDB76B', 
    '#2E8B57', '#6B8E23'
]

# Create a figure of specified width and height
plt.figure(figsize=(18, 10))

# Create a treemap with specified data, labels, and color
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8)

# Set the title of the chart
plt.title('Popular Food Categories', fontsize=22)

# Remove the axis
plt.axis('off')

# Display the treemap
plt.show()