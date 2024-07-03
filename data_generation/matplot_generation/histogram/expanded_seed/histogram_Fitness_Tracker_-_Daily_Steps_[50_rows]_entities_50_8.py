
import matplotlib.pyplot as plt
from datetime import datetime

# Given data
data = [
    {'Date': '2023-01-01', 'Steps': 5230},
    {'Date': '2023-01-02', 'Steps': 6870},
    {'Date': '2023-01-03', 'Steps': 7020},
    {'Date': '2023-01-04', 'Steps': 5670},
    {'Date': '2023-01-05', 'Steps': 6500},
    {'Date': '2023-01-06', 'Steps': 7100},
    {'Date': '2023-01-07', 'Steps': 7000},
    {'Date': '2023-01-08', 'Steps': 4800},
    {'Date': '2023-01-09', 'Steps': 5600},
    {'Date': '2023-01-10', 'Steps': 6900},
    {'Date': '2023-01-11', 'Steps': 8400},
    {'Date': '2023-01-12', 'Steps': 7300},
    {'Date': '2023-01-13', 'Steps': 5900},
    {'Date': '2023-01-14', 'Steps': 7200},
    {'Date': '2023-01-15', 'Steps': 7550}
]

# Extract steps values for histogram
steps = [entry['Steps'] for entry in data]

# Create histogram
n, bins, patches = plt.hist(steps, bins=5, color='skyblue', edgecolor='black')

# Add a title and labels
plt.title('Steps Distribution From 2023-01-01 to 2023-01-15')
plt.xlabel('Number of Steps')
plt.ylabel('Frequency')

# Annotate the histogram with the number of steps for each bin
for i in range(len(n)):
    plt.text(bins[i] + (bins[i+1]-bins[i])/2, n[i], str(int(n[i])),
             ha='center', va='bottom')

# Set the color of each bar based on its height
max_height = max(n)
colors = ['tomato', 'gold', 'lightgreen', 'lightblue', 'plum']
for bar, color in zip(patches, colors):
    bar.set_facecolor(color)

# Optionally, format x-axis with step size
plt.xticks(bins)

# Show the plot with a grid
plt.grid(axis='y', alpha=0.75)
plt.show()