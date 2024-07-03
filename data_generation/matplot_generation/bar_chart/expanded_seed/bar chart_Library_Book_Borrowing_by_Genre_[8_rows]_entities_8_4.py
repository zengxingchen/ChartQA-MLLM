
import matplotlib.pyplot as plt
import numpy as np

# Data from the chart table
data = [{'Genre': 'January', 'Romance': 65, 'Thriller': 85, 'Sci-Fi': 45, 'Fantasy': 120, 'Non-Fiction': 35, "Children's Books": 90, 'History': 60},
        {'Genre': 'February', 'Romance': 75, 'Thriller': 78, 'Sci-Fi': 40, 'Fantasy': 110, 'Non-Fiction': 32, "Children's Books": 95, 'History': 58},
        {'Genre': 'March', 'Romance': 80, 'Thriller': 90, 'Sci-Fi': 42, 'Fantasy': 115, 'Non-Fiction': 40, "Children's Books": 100, 'History': 62},
        {'Genre': 'April', 'Romance': 85, 'Thriller': 88, 'Sci-Fi': 50, 'Fantasy': 130, 'Non-Fiction': 45, "Children's Books": 105, 'History': 65},
        {'Genre': 'May', 'Romance': 90, 'Thriller': 92, 'Sci-Fi': 55, 'Fantasy': 125, 'Non-Fiction': 50, "Children's Books": 110, 'History': 68},
        {'Genre': 'June', 'Romance': 95, 'Thriller': 93, 'Sci-Fi': 48, 'Fantasy': 135, 'Non-Fiction': 55, "Children's Books": 115, 'History': 70},
        {'Genre': 'July', 'Romance': 100, 'Thriller': 98, 'Sci-Fi': 53, 'Fantasy': 140, 'Non-Fiction': 60, "Children's Books": 120, 'History': 75},
        {'Genre': 'August', 'Romance': 105, 'Thriller': 95, 'Sci-Fi': 57, 'Fantasy': 145, 'Non-Fiction': 62, "Children's Books": 125, 'History': 80}]

# Get the list of genres (excluding 'Genre' key)
genres = list(data[0].keys())[1:]

# Get the list of months
months = [month_data['Genre'] for month_data in data]

# Define number of bars and width of each bar
n_bars = len(genres)
bar_width = 0.35

# X axis locations for the groups
index = np.arange(len(months))

# Set up the figure and the axes
plt.figure(figsize=(12, 8))

# Initialize the bottom position for each bar
last_bottom = np.zeros(len(months))

# Loop through each genre and layer each one on the bars
for genre in genres:
    sales = [month_data[genre] for month_data in data]
    plt.bar(index, sales, bar_width, bottom=last_bottom, label=genre)
    # Update the bottom position
    last_bottom += np.array(sales)

# Set the title and the labels
plt.title('Monthly Sales by Genre')
plt.xlabel('Month')
plt.ylabel('Total Sales')

# Set the position of the x ticks - in the center of the bars
plt.xticks(index, months)

# Rotate the x-axis' texts so that they fit nicely
plt.xticks(rotation=45)

# Create the legend
plt.legend(title='Genres', bbox_to_anchor=(1.05, 1), loc='upper left')

# Turn on the grid for better readability
plt.grid()

# Show the plot with a neatly laid out legend
plt.tight_layout()
plt.show()