
import matplotlib.pyplot as plt
import squarify

# Data points
industries = ['Information Technology', 'Healthcare', 'Financials', 'Consumer Discretionary', 'Communication Services', 
              'Industrials', 'Consumer Staples', 'Energy', 'Utilities', 'Real Estate', 'Materials', 
              'Consumer Services', 'Transportation', 'Automobiles', 'Media']
values = [5000, 4200, 3900, 3700, 3500, 3300, 3100, 2900, 2700, 2500, 2300, 2100, 1900, 1700, 1500]
colors = ['#4682B4', '#6A5ACD', '#8A2BE2', '#A52A2A', '#BDB76B', '#DC143C', '#FF4500', 
          '#32CD32', '#00CED1', '#FFD700', '#ADFF2F', '#9370DB', '#FF6347', '#7FFFD4', '#20B2AA']

# Plot Dimensions
plt.figure(figsize=(14, 10))

# Create a treemap
squarify.plot(sizes=values, label=industries, color=colors, alpha=0.8)

# Title
plt.title('Market Capitalization of Various Industries (in Billions)', fontsize=18, y=1.05)

# Remove axes
plt.axis('off')

# Show plot
plt.show()