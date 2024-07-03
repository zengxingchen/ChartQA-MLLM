
import matplotlib.pyplot as plt

# Data Points
temperatures = [
    15.2, 18.3, 20.1, 16.4, 14.6, 12.1, 25.7, 22.9, 11.9, 27.3, 28.4, 21.6,
    19.8, 24.1, 17.2, 22.3, 14.8, 10.7, 19.3, 16.1, 23.5, 18.7, 15.9, 26.8,
    23.9, 21.4, 18.0, 27.5, 12.4, 13.6, 14.3, 20.9, 17.4, 19.5, 27.9, 29.1
]

# Histogram Configuration
plt.figure(figsize=(12, 6))  # Width and height of the chart
plt.hist(temperatures, bins=15, orientation='vertical', color='#e74c3c', rwidth=0.8)  # Color and bar width
plt.title('Average Annual Temperature Distribution in Major US Cities')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.grid(axis='y', color='gray', linestyle='--', linewidth=0.5)

# Show the plot
plt.show()