
import matplotlib.pyplot as plt

# Data representing distances covered in kilometers
distances = [
    5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100,
    105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180,
    185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250
]

# Frequencies of distances covered
frequencies = [
    3, 12, 18, 24, 30, 20, 15, 10, 5, 2, 1, 3, 8, 13, 17, 23, 28, 22, 16, 11,
    6, 4, 2, 1, 3, 7, 14, 19, 25, 27, 21, 16, 12, 8, 4, 2, 1, 5, 10, 15, 18, 22,
    26, 29, 20, 14, 9, 5, 2, 1
]

# Set figure size
plt.figure(figsize=(10, 6))

# Create a vertical histogram with modified color and bin width
plt.hist(distances, bins=25, color='#FF6347', weights=frequencies)

# Set the chart title and labels
plt.title('Distribution of Distances Covered in a Cycling Event')
plt.xlabel('Distance (km)')
plt.ylabel('Frequency')

# Customize the tick marks
plt.xticks(range(0, 260, 20))
plt.yticks(range(0, 35, 5))

# Display the plot
plt.show()