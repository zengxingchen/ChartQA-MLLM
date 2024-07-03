
import matplotlib.pyplot as plt

# Data from the table
cups_sold_data = [150, 132, 165, 121, 180, 142, 159, 130, 110, 145, 102, 172, 125, 160, 138]  # Extracted the values to a list

# Create a histogram with detailed visual encoding
plt.hist(cups_sold_data, bins=8, color='skyblue', edgecolor='black')

# Adding a grid
plt.grid(axis='y', alpha=0.75)

# Adding a title and labels
plt.title('Histogram of Cups Sold')
plt.xlabel('Cups Sold')
plt.ylabel('Frequency')

# Annotate with the number of cups sold for each bin (to show the detail)
n, bins, patches = plt.hist(cups_sold_data, bins=8, color='skyblue', edgecolor='black')
for i in range(len(patches)):
    plt.text(patches[i].get_x() + patches[i].get_width() / 2, n[i] + 0.1, str(n[i]), fontsize=10, ha='center')

# Show the plot
plt.show()