
import matplotlib.pyplot as plt
import numpy as np

# Generated data points representing the temperature distribution over a year in a city
temperatures = np.array([
    14, 15, 16, 17, 17, 18, 18, 18, 19, 20, 20, 21, 22, 23, 23, 24, 25, 26, 27, 28, 
    28, 29, 30, 31, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 
    47, 48, 49, 50, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 
    66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 
    86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100
])

# Plotting the histogram
plt.figure(figsize=(15, 10))
plt.hist(temperatures, bins=20, orientation='horizontal', color='#3498db', rwidth=0.9)

# Customizing the plot
plt.title('Temperature Distribution Over a Year in a City')
plt.xlabel('Number of Days')
plt.ylabel('Temperature (°F)')
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Showing the plot
plt.show()