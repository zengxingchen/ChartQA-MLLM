
import matplotlib.pyplot as plt

# Data Points
temperatures = [
    -20, -10, -5, 0, 1, 2, 4, 5, 7, 8, 10, 12, 13, 15, 16, 17, 19, 20, 21, 
    22, 23, 24, 25, 26, 28, 30, 31, 33, 35, 37, 39, 41, 43, 44, -15, -17, 45
]

# Histogram Configuration
plt.figure(figsize=(10, 8))  # Width and height of the chart
plt.hist(temperatures, bins=30, orientation='horizontal', color='#3498db', rwidth=0.9)  # Color and bar width
plt.title('Average Monthly Temperature Distribution')
plt.xlabel('Frequency')
plt.ylabel('Temperature (°C)')
plt.grid(axis='x', color='gray', linestyle='--', linewidth=0.5)

# Show the plot
plt.show()