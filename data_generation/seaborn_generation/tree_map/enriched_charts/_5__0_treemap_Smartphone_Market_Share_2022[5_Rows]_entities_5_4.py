
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
    'Crop': ['Tech', 'Retail', 'Finance', 'Energy', 'Healthcare', 
             'Tech', 'Retail', 'Finance', 'Energy', 'Healthcare',
             'Tech', 'Retail', 'Finance', 'Energy', 'Healthcare',
             'Tech', 'Retail', 'Finance', 'Energy', 'Healthcare',
             'Tech', 'Retail', 'Finance', 'Energy', 'Healthcare',
             'Tech', 'Retail', 'Finance', 'Energy', 'Healthcare'],
    'Revenue': [1200, 950, 850, 1150, 700, 
                1000, 800, 650, 750, 600, 
                1300, 1100, 1000, 1050, 900, 
                700, 600, 550, 650, 500, 
                600, 500, 450, 550, 400, 
                300, 250, 200, 350, 150]
}

df = pd.DataFrame(data)

# Create a color list
colors = ['#4B8E8D', '#91C4C4', '#2E7D32', '#66BB6A', '#FF7043', 
          '#FF8A65', '#AB47BC', '#CE93D8', '#FFEB3B', '#FFF176', 
          '#9C27B0', '#BA68C8', '#8E24AA', '#D81B60', '#E57373',
          '#1976D2', '#64B5F6', '#0288D1', '#4FC3F7', '#0277BD',
          '#1E88E5', '#42A5F5', '#1565C0', '#81D4FA', '#01579B',
          '#009688', '#4DB6AC', '#00897B', '#B2DFDB', '#00796B']

# Create a figure with a defined size
plt.figure(figsize=(18, 10))

# Plot
squarify.plot(sizes=df['Revenue'], label=df['Crop'], color=colors, alpha=0.8)
plt.title('Revenue by Industry and Region', fontsize=24, pad=20)

# Remove axes
plt.axis('off')

# Show the plot
plt.show()