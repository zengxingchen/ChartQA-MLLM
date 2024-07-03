
import matplotlib.pyplot as plt
import squarify

# Data points
countries = ['China', 'United States', 'Brazil', 'India', 'Germany', 
             'Japan', 'Canada', 'Italy', 'Spain', 'France', 
             'United Kingdom', 'Australia', 'South Korea', 'Mexico', 
             'Turkey', 'Netherlands', 'Sweden', 'Norway', 'Russia', 'South Africa']
renewable_energy_capacity_gw = [895, 292, 150, 136, 132, 
                                100, 98, 55, 52, 51, 
                                40, 39, 33, 32, 28, 
                                24, 20, 16, 15, 10]
colors = ['#1f78b4', '#33a02c', '#e31a1c', '#ff7f00', '#6a3d9a', 
          '#b15928', '#a6cee3', '#b2df8a', '#fb9a99', '#fdbf6f', 
          '#cab2d6', '#ffff99', '#8dd3c7', '#ffffb3', '#bebada', 
          '#fb8072', '#80b1d3', '#fdb462', '#b3de69', '#fccde5']

# Plot Dimensions
plt.figure(figsize=(18, 14))

# Create a treemap
squarify.plot(sizes=renewable_energy_capacity_gw, label=countries, color=colors, alpha=0.8)

# Title
plt.title('Renewable Energy Capacity by Country (in Gigawatts)', fontsize=24, pad=30)

# Remove axes
plt.axis('off')

# Show plot
plt.show()