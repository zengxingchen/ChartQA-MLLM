
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
rainfall = [45.3, 37.8, 50.6, 62.1, 75.4, 80.2, 85.6, 78.9, 69.3, 58.7, 48.5, 40.2]
colors = ['#00429d', '#4771b2', '#73a2c6', '#a0c4df', '#cfe8f3', '#fddbc7',
          '#f4a582', '#d6604d', '#b2182b', '#67001f', '#ce1256', '#980043']

# Create a vertical bar chart
plt.figure(figsize=(12, 6))
bars = plt.bar(months, rainfall, color=colors, edgecolor='black', width=0.5)

# Customizing the plot
plt.ylabel('Average Monthly Rainfall (mm)')
plt.title('Average Monthly Rainfall in Tokyo')
plt.ylim(0, max(rainfall) + 10)
plt.tight_layout()

# Show grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.show()