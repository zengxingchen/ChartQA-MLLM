
import matplotlib.pyplot as plt

# Data extracted from the table data
data = [3, 4, 2, 5, 6, 1, 4, 3, 2, 3, 5, 2, 1, 0, 4]

# Create the histogram
plt.figure(figsize=(10, 6))  # Set the figure size
plt.hist(data, bins=range(min(data), max(data) + 2), color='skyblue', alpha=0.7, rwidth=0.85, edgecolor='black')

# Add visual details
plt.title('Histogram of Cups of Coffee Consumed')   # Title of the histogram
plt.xlabel('Cups of Coffee')                        # X-axis label
plt.ylabel('Frequency')                             # Y-axis label
plt.xticks(range(min(data), max(data) + 1))         # Set x-axis ticks to match the number of cups
plt.grid(axis='y', alpha=0.75)                      # Add a grid for the y-axis with a specified alpha transparency

# Annotate data points with the frequency
for i in range(min(data), max(data) + 1):
    plt.text(i, data.count(i) + 0.1, str(data.count(i)), ha='center')

# Optional styling
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')  # Rotate x-axis labels for better readability

# Show the plot
plt.show()