
import matplotlib.pyplot as plt
import pandas as pd
import squarify  # treemap library

# Prepare the data
data = {
    'Category': ['Food & Nutrition'] * 18,
    'Item': ['Apples', 'Bananas', 'Cherries', 'Grapes', 'Oranges', 
             'Strawberries', 'Blueberries', 'Peaches', 'Watermelons', 'Pineapples', 
             'Mangoes', 'Plums', 'Pears', 'Kiwi', 'Pomegranates', 
             'Blackberries', 'Avocados', 'Coconuts'],
    'Value': [1500, 2000, 1200, 2500, 1800, 2200, 1400, 1600, 3000, 1700, 
              2100, 1300, 1900, 1100, 1000, 900, 2600, 2400]
}

df = pd.DataFrame(data)

# Create a color list with specific color codes
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#FF9633', 
          '#FF33E6', '#33FFF6', '#E6FF33', '#33FF96', '#9633FF', 
          '#F6FF33', '#33E6FF', '#5733FF', '#33FF57', '#FF5733', 
          '#5733E6', '#FF3357', '#33A6FF']

# Create a figure with a defined size
plt.figure(figsize=(20, 12))

# Plot
squarify.plot(sizes=df['Value'], label=df['Item'], color=colors, alpha=0.8)
plt.title('Popular Fruits and Their Consumption in Tons', fontsize=24, y=1.05)

# Remove axes
plt.axis('off')

# Show the plot
plt.show()