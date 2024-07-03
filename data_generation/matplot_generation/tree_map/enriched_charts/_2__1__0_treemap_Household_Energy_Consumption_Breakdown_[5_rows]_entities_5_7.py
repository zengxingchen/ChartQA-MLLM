
import matplotlib.pyplot as plt
import squarify

# Data points
fruit_items = ['Apple', 'Banana', 'Orange', 'Mango', 'Grapes', 'Pineapple', 
               'Strawberry', 'Blueberry', 'Watermelon', 'Peach', 'Pear', 'Cherry']
prices = [1.2, 0.5, 0.8, 1.5, 2.0, 3.0, 0.2, 1.8, 0.9, 1.1, 1.3, 2.5]
quantity = [50, 100, 80, 60, 40, 20, 150, 30, 90, 70, 55, 35]

# Color scheme using specific color codes
colors = [
    '#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', 
    '#955251', '#B565A7', '#009B77', '#DD4124', '#45B8AC',
    '#EFC050', '#5B5EA6'
]

# Create a figure with altered width and height
fig, ax = plt.subplots(figsize=(16, 12))

# Creating a treemap
squarify.plot(sizes=quantity, label=fruit_items, color=colors, alpha=0.8, value=prices, edgecolor='white', linewidth=2)

# Chart title and subtitle
plt.title('Market Prices of Different Fruits', fontsize=18, color='darkblue')
plt.suptitle('Price per Unit and Available Quantity', fontsize=22)

# Remove the axes
plt.axis('off')

# Show plot
plt.show()