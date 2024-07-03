
import matplotlib.pyplot as plt

# Data provided
table_data = [
    {'Book Genre': 'Mystery', ' Times Borrowed': 27},
    {'Book Genre': 'Science Fiction', ' Times Borrowed': 31},
    {'Book Genre': 'Horror', ' Times Borrowed': 12},
    {'Book Genre': 'Romance', ' Times Borrowed': 42},
    {'Book Genre': 'Fantasy', ' Times Borrowed': 37},
    {'Book Genre': 'Thriller', ' Times Borrowed': 29},
    {'Book Genre': 'Biography', ' Times Borrowed': 34},
    {'Book Genre': 'History', ' Times Borrowed': 25},
    {'Book Genre': 'Young Adult', ' Times Borrowed': 47},
    {'Book Genre': "Children's Books", ' Times Borrowed': 65},
    {'Book Genre': 'Self-help', ' Times Borrowed': 19},
    {'Book Genre': 'Guide', ' Times Borrowed': 23},
    {'Book Genre': 'Travel', ' Times Borrowed': 17},
    {'Book Genre': 'Cookbook', ' Times Borrowed': 22},
    {'Book Genre': 'Art', ' Times Borrowed': 14}
]

# Extracting book genres and times borrowed into separate lists
genres = [item['Book Genre'] for item in table_data]
borrow_counts = [item[' Times Borrowed'] for item in table_data]

# Creating a color map to have a unique color for each genre
colors = plt.cm.viridis(range(len(genres)))

# Creating the bar chart
plt.figure(figsize=(10, 8))
bars = plt.bar(genres, borrow_counts, color=colors)

# Adding a title and labels
plt.title('Times Borrowed by Book Genre')
plt.xlabel('Book Genres')
plt.ylabel('Times Borrowed')

# Rotating x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Adding value labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), va='bottom', ha='center')

# Show the plot
plt.tight_layout()
plt.show()