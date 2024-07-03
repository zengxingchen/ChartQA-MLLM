
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
temperatures = [5.2, 5.7, 8.7, 14.1, 18.2, 21.4, 25.0, 26.4, 22.8, 17.5, 12.1, 7.6]
colors = ['#FF5733', '#FF8D33', '#FFC733', '#FFE333', '#D7FF33', '#9BFF33',
          '#33FF57', '#33FFCE', '#33C7FF', '#338BFF', '#335BFF', '#5733FF']

# Create a horizontal bar chart
plt.figure(figsize=(10, 8))
bars = plt.barh(months, temperatures, color=colors, edgecolor='black', height=0.6)

# Customizing the plot
plt.xlabel('Average Monthly Temperature (°C)')
plt.title('Average Monthly Temperature in Tokyo')
plt.xlim(0, max(temperatures) + 5)
plt.tight_layout()

# Show grid
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Display the plot
plt.show()