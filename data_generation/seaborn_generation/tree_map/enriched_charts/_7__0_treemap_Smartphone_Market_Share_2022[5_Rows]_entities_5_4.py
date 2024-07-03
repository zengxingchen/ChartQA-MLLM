
import matplotlib.pyplot as plt
import pandas as pd
import squarify  # treemap library

# Prepare the data
data = {
    'Region': ['North America', 'North America', 'North America', 'Europe', 'Europe', 
               'Europe', 'Asia', 'Asia', 'Asia', 'South America', 'South America', 'South America',
               'Africa', 'Africa', 'Africa', 'Oceania', 'Oceania', 'Oceania'],
    'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 'Strawberries', 
              'Apples', 'Oranges', 'Bananas', 'Oranges', 'Bananas', 'Mangoes', 
              'Apples', 'Oranges', 'Mangoes', 'Apples', 'Bananas', 'Mangoes'],
    'Production': [600, 500, 450, 700, 400, 350, 1000, 600, 800, 900, 850, 750, 
                   500, 700, 600, 300, 400, 350]
}

df = pd.DataFrame(data)

# Create a color list
colors = ['#FF5733', '#33FF57', '#3357FF', '#F333FF', '#33FFF3', '#FF33A1', 
          '#A1FF33', '#5733FF', '#FFA133', '#33FFA1', '#FF5733', '#33FF57', 
          '#3357FF', '#F333FF', '#33FFF3', '#FF33A1', '#A1FF33', '#5733FF']

# Create a figure with a defined size
plt.figure(figsize=(18, 10))

# Plot
squarify.plot(sizes=df['Production'], label=df['Fruit'], color=colors, alpha=0.8)
plt.title('Fruit Production Volume by Region', fontsize=24, y=1.05)

# Remove axes
plt.axis('off')

# Show the plot
plt.show()