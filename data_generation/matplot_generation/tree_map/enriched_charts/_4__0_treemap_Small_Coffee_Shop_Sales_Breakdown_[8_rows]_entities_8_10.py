
import matplotlib.pyplot as plt
import squarify  # pip install squarify (algorithm for treemap)

# Data
categories = ['Vegetables', 'Fruits', 'Dairy', 'Meat', 'Grains', 'Snacks', 'Beverages', 'Condiments', 'Sweets', 'Seafood', 'Frozen Foods', 'Baked Goods']
amounts = [500, 300, 200, 450, 250, 150, 200, 100, 150, 350, 250, 200]

# Color Scheme in HEX
colors = ['#ff9999', '#66b2ff', '#99ff99', '#ffcc99', '#ff6666', '#a0a0ff', '#ffd700', '#ffb6c1', '#c0c0c0', '#ff6347', '#4682b4', '#dda0dd']

# Creating a figure to accommodate a larger treemap
fig, ax = plt.subplots(1, figsize=(14, 8))

# Creating the treemap
squarify.plot(sizes=amounts, label=categories, color=colors, alpha=0.8)

# Title of the treemap
plt.title('Monthly Food & Nutrition Expenses Distribution', fontsize=18)

# Removing the axes for better aesthetic
plt.axis('off')

# Display the plot
plt.show()