
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
tourists = [1200, 1350, 1500, 1600, 1750, 1800, 2000, 2100, 1900, 1850, 1700, 1600]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b',
          '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#aec7e8', '#ffbb78']

# Create a horizontal bar chart
plt.figure(figsize=(14, 8))
bars = plt.barh(months, tourists, color=colors, edgecolor='black', height=0.5)

# Customizing the plot
plt.xlabel('Number of Tourists')
plt.title('Average Monthly Number of Tourists Visiting a City')
plt.xlim(min(tourists) - 100, max(tourists) + 100)
plt.tight_layout()

# Show grid
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Display the plot
plt.show()