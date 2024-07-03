
import matplotlib.pyplot as plt
import squarify

# Data points
fruits = [
    'Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grapes', 'Honeydew', 
    'Indian Fig', 'Jackfruit', 'Kiwi', 'Lemon', 'Mango', 'Nectarine', 'Orange', 
    'Papaya', 'Quince', 'Raspberry', 'Strawberry', 'Tangerine', 'Ugli fruit'
]
calories = [52, 96, 50, 282, 73, 74, 69, 36, 41, 95, 61, 29, 60, 44, 47, 43, 57, 52, 32, 53, 47]
vitamins = [5, 8, 6, 2, 9, 3, 4, 7, 10, 1, 5, 7, 6, 4, 8, 3, 5, 6, 8, 4, 7]
colors = [
    '#FF6347', '#FFD700', '#98FB98', '#00CED1', '#FF69B4', '#B0C4DE', 
    '#FFA07A', '#20B2AA', '#778899', '#7B68EE', '#6B8E23', '#4682B4', 
    '#D2691E', '#B22222', '#8B4513', '#DAA520', '#2E8B57', '#8A2BE2', 
    '#DEB887', '#5F9EA0', '#FF4500'
]

# Create a figure with altered width and height
fig, ax = plt.subplots(figsize=(16, 12))

# Creating a treemap
squarify.plot(sizes=calories, label=fruits, color=colors, alpha=0.8, value=vitamins, edgecolor='white', linewidth=2)

# Chart title and subtitle
plt.title('Calorie and Vitamin Distribution in Fruits', fontsize=18, color='darkgreen')
plt.suptitle('Food & Nutrition', fontsize=22)

# Remove the axes
plt.axis('off')

# Show plot
plt.show()