
import matplotlib.pyplot as plt
import numpy as np

# Given data
data = [
    {'Genre': 'Jan', "Children's Literature": 120, 'Fiction': 310, 'Non-Fiction': 135, 'Young Adult': 180, 'Science Fiction': 95, 'Self-Help': 85, 'Biographies': 60, 'Cookbooks': 45},
    {'Genre': 'Feb', "Children's Literature": 110, 'Fiction': 280, 'Non-Fiction': 100, 'Young Adult': 160, 'Science Fiction': 75, 'Self-Help': 80, 'Biographies': 40, 'Cookbooks': 55},
    {'Genre': 'Mar', "Children's Literature": 130, 'Fiction': 305, 'Non-Fiction': 110, 'Young Adult': 170, 'Science Fiction': 90, 'Self-Help': 70, 'Biographies': 50, 'Cookbooks': 60},
    {'Genre': 'Apr', "Children's Literature": 100, 'Fiction': 320, 'Non-Fiction': 120, 'Young Adult': 160, 'Science Fiction': 85, 'Self-Help': 75, 'Biographies': 55, 'Cookbooks': 65},
    {'Genre': 'May', "Children's Literature": 115, 'Fiction': 300, 'Non-Fiction': 115, 'Young Adult': 175, 'Science Fiction': 80, 'Self-Help': 85, 'Biographies': 65, 'Cookbooks': 40},
    {'Genre': 'Jun', "Children's Literature": 95, 'Fiction': 310, 'Non-Fiction': 105, 'Young Adult': 165, 'Science Fiction': 76, 'Self-Help': 80, 'Biographies': 60, 'Cookbooks': 50},
    {'Genre': 'Jul', "Children's Literature": 105, 'Fiction': 295, 'Non-Fiction': 100, 'Young Adult': 180, 'Science Fiction': 89, 'Self-Help': 90, 'Biographies': 62, 'Cookbooks': 49},
    {'Genre': 'Aug', "Children's Literature": 85, 'Fiction': 280, 'Non-Fiction': 90, 'Young Adult': 190, 'Science Fiction': 85, 'Self-Help': 88, 'Biographies': 60, 'Cookbooks': 55},
    {'Genre': 'Sep', "Children's Literature": 110, 'Fiction': 305, 'Non-Fiction': 115, 'Young Adult': 185, 'Science Fiction': 80, 'Self-Help': 95, 'Biographies': 70, 'Cookbooks': 45}
]

# Extracting genres except for 'Genre'
genres = list(data[0].keys())[1:]

# Months will be on the x-axis
months = [entry['Genre'] for entry in data]

# Setting up the figure and axes
fig, ax = plt.subplots(figsize=(14, 8))

# The width of each bar
bar_width = 0.1

# Colors for each genre
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange']

# Position of each bar on the x-axis
positions = np.arange(len(months))

# Loop over each genre to plot
for i, genre in enumerate(genres):
    # Values for each month for the current genre
    values = [entry[genre] for entry in data]
    
    # Plotting the bar chart. np.arange(len(months)) gives us the positions, and i * bar_width offsets each genre
    ax.bar(positions + i * bar_width, values, width=bar_width, label=genre, color=colors[i % len(colors)])

# Setting the x-axis tick positions and labels to be the center of the grouped bars
ax.set_xticks(positions + (bar_width * (len(genres)-1)) / 2)
ax.set_xticklabels(months)

# Adding some labels and a title
ax.set_xlabel('Month')
ax.set_ylabel('Number of Books Sold')
ax.set_title('Number of Books Sold by Genre per Month')

# Adding a legend to the plot
ax.legend(title='Genres', bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust the layout to make room for the legend
plt.tight_layout()

# Show the plot
plt.show()