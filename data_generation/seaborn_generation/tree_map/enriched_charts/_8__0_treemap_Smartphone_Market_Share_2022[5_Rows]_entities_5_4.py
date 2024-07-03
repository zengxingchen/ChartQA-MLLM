
import matplotlib.pyplot as plt
import pandas as pd
import squarify  # treemap library

# Prepare the data
data = {
    'Region': ['Fruits', 'Fruits', 'Fruits', 'Vegetables', 'Vegetables', 
               'Vegetables', 'Grains', 'Grains', 'Grains', 'Protein', 
               'Protein', 'Protein', 'Dairy', 'Dairy', 'Dairy', 'Fats', 
               'Fats', 'Fats', 'Sweets', 'Sweets', 'Sweets'],
    'Food': ['Apple', 'Banana', 'Orange', 'Carrot', 'Spinach', 'Broccoli', 
             'Rice', 'Wheat', 'Quinoa', 'Chicken', 'Beef', 'Tofu', 'Milk', 
             'Cheese', 'Yogurt', 'Butter', 'Olive Oil', 'Avocado', 
             'Chocolate', 'Ice Cream', 'Cake'],
    'NutritionalValue': [52, 89, 43, 41, 23, 55, 130, 340, 120, 239, 250, 
                         76, 42, 402, 59, 717, 884, 160, 546, 207, 257]
}

df = pd.DataFrame(data)

# Create a color list
colors = ['#FF9999', '#FFCC99', '#FFFF99', '#99FF99', '#99FFFF', 
          '#9999FF', '#FF99FF', '#FF6666', '#FF9966', '#FFCC66', 
          '#FFFF66', '#66FF66', '#66FFFF', '#6699FF', '#9966FF', 
          '#FF66FF', '#FF3333', '#FF6633', '#FFCC33', '#FFFF33', 
          '#33FF33']

# Create a figure with a defined size
plt.figure(figsize=(18, 9))

# Plot
squarify.plot(sizes=df['NutritionalValue'], label=df['Food'], color=colors, alpha=0.8)
plt.title('Nutritional Value of Different Foods', fontsize=24, y=1.05)

# Remove axes
plt.axis('off')

# Show the plot
plt.show()