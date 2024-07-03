
import matplotlib.pyplot as plt
import squarify

# Data points
countries = ['India', 'Brazil', 'Australia', 'United States', 'Russia', 'China', 'Canada', 'South Africa', 'Indonesia', 
             'Peru', 'Kenya', 'Mexico', 'Thailand', 'Colombia', 'Tanzania', 'Malaysia', 'Argentina', 'Venezuela', 
             'Nepal', 'Vietnam', 'Uganda']
wildlife_reserves = [103, 73, 60, 57, 50, 45, 40, 38, 35, 33, 30, 28, 25, 23, 21, 19, 18, 17, 15, 12, 10]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#76d7c4', '#ff6666', 
          '#c2c2f0', '#ffb3e6', '#ff6666', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ff6666', 
          '#66b3ff', '#99ff99', '#ffcc99']

# Plot Dimensions
plt.figure(figsize=(16, 12))

# Create a treemap
squarify.plot(sizes=wildlife_reserves, label=countries, color=colors, alpha=0.8)

# Title
plt.title('Number of Wildlife Reserves by Country', fontsize=20, pad=20)

# Remove axes
plt.axis('off')

# Show plot
plt.show()