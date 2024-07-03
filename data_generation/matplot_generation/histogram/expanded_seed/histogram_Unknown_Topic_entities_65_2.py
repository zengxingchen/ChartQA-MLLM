
import matplotlib.pyplot as plt

# Data from the table
data = [
    {'Individual': 'Individual 1', 'Number of Times Used': 30},
    {'Individual': 'Individual 2', 'Number of Times Used': 20},
    {'Individual': 'Individual 3', 'Number of Times Used': 44},
    {'Individual': 'Individual 4', 'Number of Times Used': 8},
    {'Individual': 'Individual 5', 'Number of Times Used': 12},
    {'Individual': 'Individual 6', 'Number of Times Used': 0},
    {'Individual': 'Individual 7', 'Number of Times Used': 9},
    {'Individual': 'Individual 8', 'Number of Times Used': 15},
    {'Individual': 'Individual 9', 'Number of Times Used': 36},
    {'Individual': 'Individual 10', 'Number of Times Used': 18},
    {'Individual': 'Individual 11', 'Number of Times Used': 50},
    {'Individual': 'Individual 12', 'Number of Times Used': 22},
    {'Individual': 'Individual 13', 'Number of Times Used': 10},
    {'Individual': 'Individual 14', 'Number of Times Used': 7},
    {'Individual': 'Individual 15', 'Number of Times Used': 26}
]

# Extracting the 'Number of Times Used' values
times_used = [entry['Number of Times Used'] for entry in data]

# Creating the histogram
plt.figure(figsize=(10, 6))  # Set the size of the plot

# Plot histogram with some customizations
n, bins, patches = plt.hist(times_used, bins=10, color='skyblue', edgecolor='black', linewidth=1.5, alpha=0.7)

# Beautify the histogram
plt.title('Distribution of Number of Times Used by Individuals', fontsize=15)  # Title of the histogram
plt.xlabel('Number of Times Used')  # X-axis label
plt.ylabel('Frequency')  # Y-axis label
plt.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)  # Adding a grid on y-axis
plt.xticks(range(0, max(times_used)+1, 5))  # Custom x-axis ticks
plt.yticks(range(0, max(n)+1, 1))  # Custom y-axis ticks

# Add a text label above each bar displaying its height
for i in range(len(n)):
    plt.text(bins[i] + (bins[1] - bins[0]) / 2, n[i] + 0.1, str(int(n[i])), ha='center', va='bottom')

# Show plot
plt.show()