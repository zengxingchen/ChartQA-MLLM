
import matplotlib.pyplot as plt

# Data: ages of individuals
ages = [
    22, 23, 25, 25, 26, 27, 27, 27, 28, 28, 29, 30, 30, 30, 31, 31, 32, 32, 33, 33, 33,
    34, 34, 35, 35, 35, 35, 36, 36, 37, 38, 38, 39, 40, 40, 41, 41, 42, 43, 44, 44, 45,
    45, 46, 47, 47, 48, 49, 50, 50, 50, 51, 51, 52, 53, 54, 55, 55, 56, 57, 58, 59, 60,
    60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80
]

# Set the size of the histogram
plt.figure(figsize=(10, 6))

# Create a histogram with horizontal orientation, modify colors and change bandwidth
plt.hist(ages, bins=30, orientation='horizontal', color='#32a852', rwidth=0.9)

# Add title and labels to xaxis and yaxis
plt.title('Age Distribution of a Population')
plt.xlabel('Number of individuals')
plt.ylabel('Age')

# Show the plot
plt.show()