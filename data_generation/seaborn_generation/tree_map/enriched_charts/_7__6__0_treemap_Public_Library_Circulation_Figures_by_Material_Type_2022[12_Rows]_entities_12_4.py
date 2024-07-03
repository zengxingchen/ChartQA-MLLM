
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data for the treemap
data = {
    'Category': ['Europe', 'Asia', 'North America', 'South America', 'Africa', 'Oceania', 
                 'Antarctica', 'Cultural Heritage', 'Adventure Travel', 'Eco-Tourism', 
                 'Urban Exploration', 'Culinary Trips'],
    'Percentage': [0.20, 0.18, 0.15, 0.10, 0.10, 0.07, 0.05, 0.05, 0.04, 0.03, 0.02, 0.01]
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Define color list
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', 
          '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#393b79', '#9c9ede']

# Plot the Treemap
plt.figure(figsize=(16, 12))
squarify.plot(sizes=df['Percentage'], label=df['Category'], color=colors, alpha=0.8)
plt.title('Popular Travel Destinations and Activities', fontsize=24, pad=20)
plt.axis('off')
plt.show()