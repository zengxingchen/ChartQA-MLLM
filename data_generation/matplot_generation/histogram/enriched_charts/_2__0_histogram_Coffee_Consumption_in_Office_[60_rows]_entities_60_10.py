import matplotlib.pyplot as plt

# Data points: Steps taken per day by individuals in a fitness study
steps_per_day = [
    5678, 8765, 4532, 6789, 5634, 7890, 8976, 3467, 6578, 8765, 5678, 9834, 
    2345, 8765, 4356, 6789, 8765, 1234, 7654, 6789, 4567, 8976, 3456, 2345, 
    6789, 8765, 8765, 4567, 3456, 7890, 5432, 8765, 1234, 5678, 4321, 8765, 
    5678, 6789, 8765, 9876, 3456, 2345, 8765, 7890, 5678, 8765, 5678, 6789, 
    8765, 7890
]

# Set up the size of the figure
plt.figure(figsize=(10, 6))

# Plot a histogram with vertical orientation, custom colors, and bar width
plt.hist(steps_per_day, bins=10, orientation='vertical', color='#34a853', edgecolor='#000000', linewidth=1.2)

# Set the title and labels
plt.title('Daily Steps Distribution in a Fitness Study')
plt.ylabel('Number of Individuals')
plt.xlabel('Steps per Day')

# Customize the tick marks
plt.xticks(range(min(steps_per_day), max(steps_per_day) + 1, 1000))
plt.yticks(range(0, 15, 1))

# Show grid
plt.grid(True)

# Display the histogram
plt.show()