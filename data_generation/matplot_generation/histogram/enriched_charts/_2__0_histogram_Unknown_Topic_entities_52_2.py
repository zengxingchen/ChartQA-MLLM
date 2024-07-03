
import matplotlib.pyplot as plt

# Define the data
data = [
    78, 82, 79, 83, 84, 85, 86, 88, 90, 92, 93, 95, 96, 97, 98, 99, 100, 60, 65, 63, 62, 61, 66, 67, 68, 69, 70, 72, 74, 75, 76, 77, 
    58, 55, 54, 53, 52, 50, 51, 49, 48, 47, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 33, 32, 30, 29, 28, 26, 24, 23, 22, 21, 20, 
    19, 18, 17, 16, 15, 14, 12, 11, 10, 8, 6, 5, 3, 2, 1, 80, 81, 87, 89, 91, 94, 73, 25, 13, 7, 4
]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(14, 10))

# Plot a histogram with specified color, orientation, and bin width
bin_width = 5
n, bins, patches = ax.hist(data, bins=range(min(data), max(data) + bin_width, bin_width),
                           color='#8e44ad', edgecolor='#5e3370', alpha=0.8, rwidth=0.9)

# Set chart title and labels
ax.set_title('Distribution of Test Scores in a Class', fontsize=24, pad=20)
ax.set_xlabel('Score', fontsize=16)
ax.set_ylabel('Frequency', fontsize=16)

# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(bottom=0.15)

plt.show()