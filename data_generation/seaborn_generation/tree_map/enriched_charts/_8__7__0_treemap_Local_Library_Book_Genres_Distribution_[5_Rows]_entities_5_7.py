
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Prepare the data
data = {
    'City': ['Tokyo', 'New York', 'Paris', 'Sydney', 'London', 'Dubai', 'Rome', 'Bangkok', 
             'Istanbul', 'Moscow', 'Cape Town', 'Rio de Janeiro', 'Hong Kong', 'Toronto', 
             'Singapore', 'Los Angeles', 'Berlin', 'Barcelona', 'Mumbai', 'Seoul'],
    'Average Travel Cost per Day': [200, 250, 220, 180, 230, 210, 160, 100, 140, 170, 
                                    150, 130, 190, 240, 210, 260, 180, 170, 120, 200]
}
df = pd.DataFrame(data)

# Create a color palette, mapped to these values
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', 
          '#7f7f7f', '#bcbd22', '#17becf', '#1f78b4', '#33a02c', '#fb9a99', '#e31a1c', 
          '#fdbf6f', '#ff7f00', '#cab2d6', '#6a3d9a', '#b15928', '#a6cee3']

# Plot
plt.figure(figsize=(20, 14))
squarify.plot(sizes=df['Average Travel Cost per Day'], label=df['City'], color=colors, alpha=0.8)
plt.title('Average Travel Costs per Day in Different Cities', fontsize=24, fontweight='bold', y=1.05)
plt.axis('off')
plt.show()