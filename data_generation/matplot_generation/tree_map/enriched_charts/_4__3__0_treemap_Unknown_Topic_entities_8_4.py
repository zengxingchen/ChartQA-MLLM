
import matplotlib.pyplot as plt
import squarify

# Data
food_items = [
    'Vegetables', 'Fruits', 'Grains', 'Protein Foods', 'Dairy', 
    'Sugary Foods', 'Oils', 'Beverages', 'Snacks', 'Other Foods'
]
consumption_percentage = [24.0, 15.0, 19.0, 18.0, 10.0, 5.0, 3.0, 2.0, 2.5, 1.5]
colors = [
    '#FF7F50', '#6495ED', '#FFD700', '#FF69B4', '#8A2BE2', 
    '#7FFF00', '#D2691E', '#1E90FF', '#FF4500', '#DA70D6'
]

# Create a figure with specified size
plt.figure(figsize=(14, 12))

# Create a treemap with the above data
squarify.plot(sizes=consumption_percentage, label=food_items, color=colors, alpha=0.8)

# Title of the treemap
plt.title('Food Consumption Distribution in 2023', fontsize=24, y=1.02)

# Remove the axes
plt.axis('off')

# Show the plot
plt.show()