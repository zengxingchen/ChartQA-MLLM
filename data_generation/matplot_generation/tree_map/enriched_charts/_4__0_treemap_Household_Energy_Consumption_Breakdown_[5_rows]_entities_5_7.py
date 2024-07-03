
import matplotlib.pyplot as plt
import squarify

# Data points
categories = [
    'Fruits', 'Vegetables', 'Dairy', 'Meat', 'Beverages',
    'Snacks', 'Grains', 'Seafood', 'Confectionery',
    'Frozen', 'Canned', 'Spices'
]
values = [24000, 32000, 15000, 22000, 18000, 27000, 20000, 16000, 14000, 19000, 13000, 12000]
counts = [150, 120, 70, 80, 90, 110, 85, 60, 75, 95, 65, 55]

# Color scheme using specific color codes
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF',
    '#FF8C33', '#33FF8C', '#8C33FF', '#FF338C', '#8CFF33',
    '#338CFF', '#FF3333'
]

# Create a figure with altered width and height
fig, ax = plt.subplots(figsize=(14, 10))

# Creating a treemap
squarify.plot(sizes=values, label=categories, color=colors, alpha=0.8, value=counts, edgecolor='white', linewidth=2)

# Chart title and subtitle
plt.title('Category Sales and Item Count Distribution', fontsize=18, color='darkblue')
plt.suptitle('Food & Nutrition: Sales Performance by Category', fontsize=22)

# Remove the axes
plt.axis('off')

# Show plot
plt.show()