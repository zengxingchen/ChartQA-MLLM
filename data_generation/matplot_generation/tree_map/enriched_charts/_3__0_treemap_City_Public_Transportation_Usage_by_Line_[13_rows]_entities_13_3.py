
import matplotlib.pyplot as plt
import squarify

# Data for the treemap
labels = ['Stocks', 'Bonds', 'Commodities', 'Real Estate', 'Cryptocurrency', 'Cash', 'Mutual Funds', 'ETFs', 'Precious Metals', 'Hedge Funds', 'Private Equity', 'Other']
sizes = [20, 15, 10, 25, 5, 8, 17, 25, 7, 6, 9, 8]
colors = ['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99', '#e31a1c', '#fdbf6f', '#ff7f00', '#cab2d6', '#6a3d9a', '#ffff99', '#b15928']

# Create a figure of specified width and height
plt.figure(figsize=(18, 9))

# Create a treemap with specified data, labels, and color
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8)

# Set the title of the chart
plt.title('Portfolio Diversification in 2021', fontsize=18, fontweight='bold', y=0.95)

# Remove the axis
plt.axis('off')

# Display the treemap
plt.show()