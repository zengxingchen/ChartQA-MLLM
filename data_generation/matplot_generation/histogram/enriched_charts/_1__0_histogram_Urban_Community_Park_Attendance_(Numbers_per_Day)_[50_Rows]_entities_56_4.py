
import matplotlib.pyplot as plt

# Data points for average daily steps taken in a month
steps = [
    65, 70, 68, 75, 73, 72, 66, 68, 74, 76, 75, 80, 82, 85, 88, 90, 92, 93, 94, 96,
    95, 97, 98, 99, 100, 102, 101, 99, 97, 96, 94, 92, 90, 88, 85, 83, 82, 80, 78,
    75, 74, 72, 70, 68, 66, 65, 63, 62, 60, 58, 57, 55, 54, 53, 52, 51, 50, 49, 48,
    47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28,
    27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7,
    6, 5, 4, 3, 2, 1, 0
]

plt.figure(figsize=(10, 12))  # Width and height of the chart

# Creating a vertical histogram with specified color and bar width
plt.hist(steps, bins=20, orientation='vertical', color='#FF5733', edgecolor='#333333', linewidth=0.7)

# Adding the title and labels
plt.title('Average Daily Steps Taken in a Month', pad=20)
plt.xlabel('Steps')
plt.ylabel('Number of Days')

# Customize the look of the plot, adding grid
plt.grid(axis='y', color='grey', linestyle=':', linewidth=0.5)

# Show the plot
plt.show()