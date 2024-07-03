
import matplotlib.pyplot as plt

# Data points representing ages
ages = [
    18, 19, 21, 23, 23, 24, 25, 25, 26, 27, 27, 28, 30, 30, 31, 32, 32, 33, 34, 35,
    35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50, 51, 53, 54, 55, 56, 58,
    60, 61, 63, 64, 66, 68, 69, 70, 72, 74, 76, 78, 78, 80, 82, 83, 85, 87, 88, 89,
    91, 93, 95, 96, 98
]

plt.figure(figsize=(10, 5))  # Change width and height of the chart

# Create histogram with modified properties
plt.hist(ages, bins=20, orientation='horizontal', color='#3498db', edgecolor='#ffffff', linewidth=1.2)

plt.title('Age Distribution in Metropolis City')  # Changed topic and title of the histogram
plt.xlabel('Number of People')  # This becomes the y-label, as the histogram is horizontal
plt.ylabel('Ages')  # This becomes the x-label

# Display the histogram
plt.show()