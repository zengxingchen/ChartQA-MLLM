
import matplotlib.pyplot as plt

# Data points
ages = [
    23, 25, 22, 24, 35, 37, 30, 45, 50, 55,
    60, 42, 43, 48, 49, 31, 32, 20, 21, 29,
    26, 28, 27, 33, 34, 38, 39, 40, 36, 41,
    46, 47, 44, 51, 52, 53, 54, 56, 57, 58,
    59, 61, 62, 63, 64, 65, 66, 67, 68, 69,
    70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
    80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
    90, 91, 92, 93, 94, 95, 96, 97, 98, 99,
    100
]

# Set up the figure size and resolution
plt.figure(figsize=(10, 6), dpi=80)

# Create histogram, switch to horizontal bar
plt.hist(ages, bins=15, color='#6A0DAD', orientation='horizontal')

# Customize the histogram
plt.title('Age Distribution of a Population Group')
plt.xlabel('Frequency')
plt.ylabel('Age')

# Show the histogram
plt.show()