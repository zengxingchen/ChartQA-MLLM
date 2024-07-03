
import matplotlib.pyplot as plt

# Data points for average daily temperatures in April
temperatures = [
    12, 14, 15, 16, 14, 13, 17, 19, 21, 22, 18, 16, 15, 17, 19, 20,
    21, 23, 24, 22, 24, 26, 27, 25, 24, 23, 19, 17, 14, 12
]

plt.figure(figsize=(14, 8))  # Width and height of the chart

# Creating a horizontal histogram with specified color and bar width
plt.hist(temperatures, bins=15, orientation='horizontal', color='#3498db', edgecolor='#333333', linewidth=0.5)

# Adding the title and labels
plt.title('Average Daily Temperatures in April')
plt.xlabel('Number of Days')
plt.ylabel('Temperature (°C)')

# Customize the look of the plot, adding grid
plt.grid(axis='x', color='grey', linestyle=':', linewidth=0.5)

# Show the plot
plt.show()