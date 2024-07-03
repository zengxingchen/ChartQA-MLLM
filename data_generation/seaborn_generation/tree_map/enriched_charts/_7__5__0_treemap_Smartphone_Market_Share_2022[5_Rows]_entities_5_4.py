
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
    'Crop': ['Fruits', 'Vegetables', 'Dairy', 'Meat', 'Grains', 
             'Fruits', 'Vegetables', 'Dairy', 'Meat', 'Grains',
             'Fruits', 'Vegetables', 'Dairy', 'Meat', 'Grains',
             'Fruits', 'Vegetables', 'Dairy', 'Meat', 'Grains',
             'Fruits', 'Vegetables', 'Dairy', 'Meat', 'Grains',
             'Fruits', 'Vegetables', 'Dairy', 'Meat', 'Grains'],
    'Revenue': [1400, 1200, 1000, 1300, 1100, 
                1250, 1050, 950, 1150, 850, 
                1500, 1350, 1200, 1400, 1250, 
                950, 850, 750, 900, 700, 
                850, 750, 650, 800, 600, 
                500, 450, 400, 550, 350]
}

df = pd.DataFrame(data)

# Create a color list
colors = ['#8DD3C7', '#FFFFB3', '#BEBADA', '#FB8072', '#80B1D3', 
          '#FDB462', '#B3DE69', '#FCCDE5', '#D9D9D9', '#BC80BD', 
          '#CCEBC5', '#FFED6F', '#BC80BD', '#FB8072', '#80B1D3',
          '#FDB462', '#B3DE69', '#FCCDE5', '#D9D9D9', '#BC80BD',
          '#8DD3C7', '#FFFFB3', '#BEBADA', '#FB8072', '#80B1D3',
          '#FDB462', '#B3DE69', '#FCCDE5', '#D9D9D9', '#BC80BD']

# Create a figure with a defined size
plt.figure(figsize=(20, 12))

# Plot
squarify.plot(sizes=df['Revenue'], label=df['Crop'], color=colors, alpha=0.8)
plt.title('Revenue by Food Category and Region', fontsize=24, pad=30)

# Remove axes
plt.axis('off')

# Show the plot
plt.show()