
import matplotlib.pyplot as plt

# This is the data for the number of visitors to a museum
visitors = [
    13, 15, 17, 19, 20, 21, 22, 23, 24, 25, 27, 28, 30, 31, 32, 33, 35, 37, 39, 40, 
    41, 42, 43, 44, 46, 48, 49, 50, 52, 54, 55, 57, 58, 60, 62, 63, 64, 66, 68, 70, 
    71, 73, 74, 76, 78, 79, 81, 83, 84, 85, 87, 89, 91, 93, 94, 95, 97, 99, 101, 102, 
    103, 105, 107, 109, 110, 112, 113, 115, 117, 118, 120, 122, 124, 125
]

# Set the size of the figure
plt.figure(figsize=(12, 10))

# Plot the histogram with specified bin width, and custom color
plt.hist(visitors, bins=range(10, 130, 10), alpha=0.85, orientation='vertical', color='#4682B4')

# Set chart title and labels
plt.title('Museum Visitor Distribution')
plt.xlabel('Age')
plt.ylabel('Number of Visitors')

# Tweak spacing to prevent clipping of ylabel
plt.tight_layout()

# Show the plot
plt.show()