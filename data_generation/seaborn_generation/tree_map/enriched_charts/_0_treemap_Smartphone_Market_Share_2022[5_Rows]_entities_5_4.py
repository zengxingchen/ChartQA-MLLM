
import matplotlib.pyplot as plt
import pandas as pd
import squarify  # treemap library

# Prepare the data
data = {
    'Region': ['North America', 'North America', 'North America', 'Europe', 'Europe', 
               'Europe', 'Asia', 'Asia', 'Asia', 'South America', 'South America', 'South America',
               'Africa', 'Africa', 'Africa', 'Oceania', 'Oceania', 'Oceania'],
    'Crop': ['Wheat', 'Corn', 'Soybean', 'Wheat', 'Corn', 'Barley', 'Rice', 'Soybean',
             'Wheat', 'Corn', 'Soybean', 'Coffee', 'Cassava', 'Sorghum', 'Cocoa', 'Wheat',
             'Dairy', 'Lamb'],
    'Production': [500, 800, 450, 600, 300, 500, 900, 200, 700, 600, 800, 500, 400, 300, 200, 100, 200, 150]
}

df = pd.DataFrame(data)

# Create a color list
colors = ['#FFEDA0', '#FED976', '#FEB24C', '#FD8D3C', '#FC4E2A', 
          '#E31A1C', '#BD0026', '#800026'] * 3

# Create a figure with a defined size
plt.figure(figsize=(16, 8))

# Plot
squarify.plot(sizes=df['Production'], label=df['Crop'], color=colors, alpha=0.8)
plt.title('Crop Production Volume by Region', fontsize=24)

# Remove axes
plt.axis('off')

# Show the plot
plt.show()