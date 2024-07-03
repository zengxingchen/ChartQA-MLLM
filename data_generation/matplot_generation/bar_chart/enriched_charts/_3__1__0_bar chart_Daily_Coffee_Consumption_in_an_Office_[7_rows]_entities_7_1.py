
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
exoplanets_discovered = [34, 27, 45, 50, 53, 60, 65, 70, 63, 55, 48, 40]

# Color codes for each bar
colors = ['#FF5733', '#FF6F33', '#FF8D33', '#FFAA33', '#FFC433', '#FFE033', '#EFFF33', '#B0FF33', '#6AFF33', '#33FF57', '#33FFB2', '#33FFD2']

# Bar width
bar_height = 0.4

# Create horizontal bar chart
plt.figure(figsize=(10, 8))
bar_container = plt.barh(months, exoplanets_discovered, color=colors, height=bar_height)

# Add data labels
for bar in bar_container:
    width = bar.get_width()
    plt.text(width + 2, bar.get_y() + bar.get_height()/2, f'{width}', ha='center', va='center')

# Title and labels
plt.title('Exoplanets Discovered Monthly in 2023')
plt.xlabel('Number of Exoplanets Discovered')
plt.ylabel('Month')

# Customize the grid
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Show plot
plt.show()