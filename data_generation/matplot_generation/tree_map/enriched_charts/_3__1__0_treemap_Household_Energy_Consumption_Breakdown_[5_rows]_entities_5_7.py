
import matplotlib.pyplot as plt
import squarify

# Data points
food_items = ['Apple', 'Banana', 'Orange', 'Broccoli', 'Chicken Breast', 'Almonds', 'Salmon', 'Eggs', 'Spinach', 
              'Sweet Potato', 'Quinoa', 'Greek Yogurt', 'Avocado', 'Blueberries', 'Carrots', 'Tofu', 'Walnuts', 
              'Oatmeal', 'Milk', 'Brown Rice']
calories = [95, 105, 62, 55, 165, 579, 208, 78, 23, 103, 120, 100, 234, 85, 41, 144, 654, 154, 103, 216]
protein = [0.5, 1.3, 1.2, 3.7, 31, 21, 20, 6, 2.9, 2, 4.1, 10, 3, 1.1, 0.9, 15, 15, 6, 8, 5]

# Color scheme using specific color codes
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF33A8', 
    '#A833FF', '#FF8F33', '#33FFF2', '#F233FF', '#FF3333',
    '#33FFA8', '#A8FF33', '#FF5733', '#33FF57', '#3357FF', 
    '#57FF33', '#FF33A8', '#A833FF', '#FF8F33', '#33FFF2'
]

# Create a figure with altered width and height
fig, ax = plt.subplots(figsize=(16, 12))

# Creating a treemap
squarify.plot(sizes=calories, label=food_items, color=colors, alpha=0.8, value=protein, edgecolor='white', linewidth=2)

# Chart title and subtitle
plt.title('Nutritional Values of Various Foods', fontsize=18, color='darkgreen')
plt.suptitle('Calories and Protein Content per Serving', fontsize=22)

# Remove the axes
plt.axis('off')

# Show plot
plt.show()