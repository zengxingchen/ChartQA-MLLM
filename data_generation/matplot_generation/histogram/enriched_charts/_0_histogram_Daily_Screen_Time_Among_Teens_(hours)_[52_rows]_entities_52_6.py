
import matplotlib.pyplot as plt

# Monthly average temperatures
temperatures = [
    2, 5, 8, 12, 16, 21, 25, 26, 28, 27, 22, 15, 9, 5, 3, 3, 6, 8, 13, 17, 20, 24, 
    25, 27, 28, 26, 21, 16, 10, 5, 3, 2, 4, 7, 11, 15, 19, 22, 24, 26, 28, 29, 30, 
    26, 20, 14, 9, 4, 2, 1, 3, 7, 10, 14, 18, 22, 25, 26, 28, 30, 31, 30, 25, 19, 
    12, 7, 3, 1
]

# Create histogram
plt.figure(figsize=(8, 6))  # Change width and height reasonably
n, bins, patches = plt.hist(
    temperatures, bins=15, color='#FF5733', orientation='horizontal', rwidth=0.9)

# Customize appearance
plt.title('Monthly Average Temperatures Distribution')
plt.xlabel('Frequency')
plt.ylabel('Temperature (degrees)')

# Show plot
plt.show()