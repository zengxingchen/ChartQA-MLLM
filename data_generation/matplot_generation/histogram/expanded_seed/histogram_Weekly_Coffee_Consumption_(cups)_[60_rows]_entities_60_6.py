
import matplotlib.pyplot as plt

# Table data
data = [
    {'Person ID': 1, ' Coffee Cups': 20},
    {'Person ID': 2, ' Coffee Cups': 18},
    {'Person ID': 3, ' Coffee Cups': 22},
    {'Person ID': 4, ' Coffee Cups': 15},
    {'Person ID': 5, ' Coffee Cups': 17},
    {'Person ID': 6, ' Coffee Cups': 25},
    {'Person ID': 7, ' Coffee Cups': 14},
    {'Person ID': 8, ' Coffee Cups': 21},
    {'Person ID': 9, ' Coffee Cups': 19},
    {'Person ID': 10, ' Coffee Cups': 16},
    {'Person ID': 11, ' Coffee Cups': 24},
    {'Person ID': 12, ' Coffee Cups': 20},
    {'Person ID': 13, ' Coffee Cups': 14},
    {'Person ID': 14, ' Coffee Cups': 22},
    {'Person ID': 15, ' Coffee Cups': 16}
]

# Extracting 'Coffee Cups' values
coffee_cups = [person[' Coffee Cups'] for person in data]

# Creating the histogram
plt.figure(figsize=(10, 6))
n, bins, patches = plt.hist(coffee_cups, bins=range(14, 27), alpha=0.7, color='skyblue', edgecolor='black')

# Adding colors to each bin
colors = ['orange', 'green', 'blue', 'yellow', 'red']
for patch, color in zip(patches, colors):
    patch.set_facecolor(color)

# Adding labels and title
plt.xlabel('Number of Coffee Cups')
plt.ylabel('Frequency')
plt.title('Coffee Cups Distribution Among Persons')
plt.xticks(range(14, 27))  # Setting x-ticks to match the number of coffee cups

# Adding a grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Showing values on top of the bars
for i in range(len(n)):
    plt.text(bins[i]+0.5, n[i], str(int(n[i])), ha='center', va='bottom')

# Displaying the plot
plt.show()