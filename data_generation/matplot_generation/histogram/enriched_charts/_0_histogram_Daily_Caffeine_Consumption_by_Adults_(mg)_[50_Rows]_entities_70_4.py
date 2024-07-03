
import matplotlib.pyplot as plt

# Data points (ages)
ages = [
    23, 25, 27, 27, 28, 28, 28, 29, 30, 30, 30, 30,
    31, 31, 31, 32, 32, 32, 32, 33, 33, 33, 33, 33,
    34, 34, 35, 35, 35, 36, 37, 37, 38, 38, 39, 40,
    41, 42, 42, 43, 45, 46, 47, 48, 50, 51, 53, 55,
    56, 58, 60
]

# Creating the histogram
fig, ax = plt.subplots(figsize=(10, 6))  # Width and height of the chart
n, bins, patches = ax.hist(ages, bins=15, orientation='horizontal', color='#6a0dad', edgecolor='#333333', linewidth=1.5)

# Customize the plot
ax.set_title('Age Distribution of a Sample Population')
ax.set_xlabel('Number of People')
ax.set_ylabel('Age')
ax.set_xlim(0, 12)  # Adjusting the x-axis to fit the longest bar for clarity

# Set the color of each bar
for i, patch in enumerate(patches):
    patch.set_facecolor(plt.cm.viridis(i / len(patches)))  # Gradient color using viridis colormap

plt.tight_layout()
plt.show()