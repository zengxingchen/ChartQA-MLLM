
import matplotlib.pyplot as plt
import pandas as pd
import squarify  # treemap library

# Prepare the data
data = {
    'Region': ['North America', 'North America', 'North America', 'North America', 'North America', 
               'Europe', 'Europe', 'Europe', 'Europe', 'Europe', 
               'Asia', 'Asia', 'Asia', 'Asia', 'Asia', 
               'South America', 'South America', 'South America', 'South America', 'South America',
               'Africa', 'Africa', 'Africa', 'Africa', 'Africa',
               'Oceania', 'Oceania', 'Oceania', 'Oceania', 'Oceania'],
    'Genre': ['Fiction', 'Non-Fiction', 'Romance', 'Science Fiction', 'Fantasy', 
             'Fiction', 'Non-Fiction', 'Romance', 'Science Fiction', 'Fantasy',
             'Fiction', 'Non-Fiction', 'Romance', 'Science Fiction', 'Fantasy',
             'Fiction', 'Non-Fiction', 'Romance', 'Science Fiction', 'Fantasy',
             'Fiction', 'Non-Fiction', 'Romance', 'Science Fiction', 'Fantasy',
             'Fiction', 'Non-Fiction', 'Romance', 'Science Fiction', 'Fantasy'],
    'Sales': [1500, 1300, 1100, 900, 1200, 
              1400, 1100, 1000, 850, 900, 
              1600, 1450, 1350, 1200, 1300, 
              900, 850, 800, 700, 750, 
              850, 750, 700, 650, 600, 
              550, 500, 450, 400, 350]
}

df = pd.DataFrame(data)

# Create a color list
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1', 
          '#A133FF', '#FF5733', '#33FF57', '#3357FF', '#FF33A1', 
          '#33FFA1', '#A133FF', '#FF5733', '#33FF57', '#3357FF',
          '#FF33A1', '#33FFA1', '#A133FF', '#FF5733', '#33FF57',
          '#3357FF', '#FF33A1', '#33FFA1', '#A133FF', '#FF5733',
          '#33FF57', '#3357FF', '#FF33A1', '#33FFA1', '#A133FF']

# Create a figure with a defined size
plt.figure(figsize=(24, 14))

# Plot
squarify.plot(sizes=df['Sales'], label=df['Genre'], color=colors, alpha=0.8)
plt.title('Global Literature Sales by Genre and Region', fontsize=26, pad=40)

# Remove axes
plt.axis('off')

# Show the plot
plt.show()