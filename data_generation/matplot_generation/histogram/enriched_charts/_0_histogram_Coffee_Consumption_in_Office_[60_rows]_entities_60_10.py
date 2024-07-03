
import matplotlib.pyplot as plt

# Data points: Ages of a population sample
ages = [
    23, 26, 29, 22, 24, 35, 37, 40, 42, 38, 45, 48,
    50, 51, 43, 41, 33, 36, 28, 30, 55, 57, 59, 60,
    62, 65, 68, 71, 73, 75, 77, 80, 82, 85, 87, 89,
    91, 93, 95, 97, 99
]

# Set up the size of the figure
plt.figure(figsize=(12, 8))

# Plot a histogram with horizontal orientation, custom colors, and bar width
plt.hist(ages, bins=15, orientation='horizontal', color='#4287f5', edgecolor='black', linewidth=1.5)

# Set the title and labels
plt.title('Age Distribution of a Population Sample')
plt.xlabel('Number of Individuals')
plt.ylabel('Age')

# Customize the tick marks
plt.xticks(range(0, max(ages) // 10 * 10 + 1, 5))
plt.yticks(range(min(ages), max(ages) + 1, 5))

# Show grid
plt.grid(True)

# Display the histogram
plt.show()