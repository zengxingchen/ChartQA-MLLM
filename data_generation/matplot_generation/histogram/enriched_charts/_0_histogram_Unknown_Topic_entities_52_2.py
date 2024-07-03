
import matplotlib.pyplot as plt

# Define the data
ages = [
    23, 26, 22, 27, 29, 21, 35, 37, 45, 52, 41, 38, 34, 33, 29, 30, 32, 31, 25, 24,
    39, 42, 40, 43, 46, 49, 50, 51, 55, 57, 58, 60, 62, 64, 65, 66, 67, 69, 70, 71,
    73, 75, 78, 80, 81, 82, 83, 85, 86, 87, 88, 90, 92, 93, 94, 95, 96, 97, 98, 99,
    100
]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(12, 8))

# Plot a histogram with specified color, orientation, and bin height
bin_height = 5
n, bins, patches = ax.hist(ages, bins=range(min(ages), max(ages) + bin_height, bin_height),
                           color='#3498db', edgecolor='#2980b9', alpha=0.7, rwidth=0.85, orientation='horizontal')

# Set chart title and labels
ax.set_title('Age Distribution of a Population', fontsize=20)
ax.set_xlabel('Frequency', fontsize=14)
ax.set_ylabel('Age', fontsize=14)

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)

plt.show()