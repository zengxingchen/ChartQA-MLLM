
import matplotlib.pyplot as plt
import squarify

# Data points for the treemap
categories = ['Vegetables', 'Fruits', 'Grains', 'Dairy', 'Meat', 'Fish', 'Nuts', 'Legumes', 'Beverages', 'Snacks', 'Oils', 'Sweets', 'Eggs', 'Herbs', 'Spices', 'Sauces', 'Baked Goods', 'Seafood', 'Poultry']
consumption = [1500, 1300, 1200, 1100, 1050, 1000, 950, 900, 850, 800, 750, 700, 650, 600, 550, 500, 450, 400, 350]

# TreeMap customization
color_palette = ['#FF9999', '#FFCC99', '#FFFF99', '#99FF99', '#99FFFF', '#9999FF', '#CC99FF', '#FF99CC', '#FF6666', '#FFCC66', '#FFFF66', '#66FF66', '#66FFFF', '#6666FF', '#CC66FF', '#FF66CC', '#FF3333', '#FF9933', '#FFFF33']
plt.figure(figsize=(20, 12))

# Creating the treemap
squarify.plot(sizes=consumption, label=categories, color=color_palette, alpha=0.8)

# Title and labels
plt.title('Consumption of Different Food Categories (in grams)', fontsize=20, fontweight='bold')
plt.axis('off')

plt.show()