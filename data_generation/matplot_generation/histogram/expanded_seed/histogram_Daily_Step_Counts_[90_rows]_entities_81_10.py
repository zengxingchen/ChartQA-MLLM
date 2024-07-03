
import matplotlib.pyplot as plt

# Given table data
data = [
    {'Date': '2023-01-01', 'Steps': 3248},
    {'Date': '2023-01-02', 'Steps': 5680},
    {'Date': '2023-01-03', 'Steps': 8321},
    {'Date': '2023-01-04', 'Steps': 4376},
    {'Date': '2023-01-05', 'Steps': 6592},
    {'Date': '2023-01-06', 'Steps': 2891},
    {'Date': '2023-01-07', 'Steps': 9864},
    {'Date': '2023-01-08', 'Steps': 2345},
    {'Date': '2023-01-09', 'Steps': 5432},
    {'Date': '2023-01-10', 'Steps': 6571},
    {'Date': '2023-01-11', 'Steps': 7832},
    {'Date': '2023-01-12', 'Steps': 4984},
    {'Date': '2023-01-13', 'Steps': 3204},
    {'Date': '2023-01-14', 'Steps': 10456},
    {'Date': '2023-01-15', 'Steps': 4352}
]

# Extract the 'Steps' from the data
steps = [entry['Steps'] for entry in data]

# Set up the plot
plt.figure(figsize=(10, 6))  # Set the size of the figure

# Plot histogram
n, bins, patches = plt.hist(steps, bins=5, color='skyblue', edgecolor='black')

# Add title and labels
plt.title('Histogram of Steps')
plt.xlabel('Number of Steps')
plt.ylabel('Frequency')

# Customize x-axis ticks to represent the actual range of 'Steps'
plt.xticks(bins)

# Annotate the frequency on top of each bar
for i in range(len(patches)):
    plt.text(patches[i].xy[0], patches[i].get_height() + 0.1, str(int(patches[i].get_height())), ha='left')

# Add a grid for better readability
plt.grid(axis='y', alpha=0.75)

# Display plot
plt.show()