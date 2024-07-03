
import matplotlib.pyplot as plt
import numpy as np

# Data from the provided table
data = [
    {'Month': 'January', "Children's Books": 320, 'Novels': 250, 'Non-Fiction': 190, 'Textbooks': 110, 'Comics': 90, 'Magazines': 40},
    {'Month': 'February', "Children's Books": 280, 'Novels': 230, 'Non-Fiction': 180, 'Textbooks': 90, 'Comics': 100, 'Magazines': 50},
    {'Month': 'March', "Children's Books": 300, 'Novels': 240, 'Non-Fiction': 200, 'Textbooks': 120, 'Comics': 110, 'Magazines': 60},
    {'Month': 'April', "Children's Books": 275, 'Novels': 300, 'Non-Fiction': 210, 'Textbooks': 130, 'Comics': 120, 'Magazines': 65},
    # ... include all provided data
    {'Month': 'December', "Children's Books": 350, 'Novels': 340, 'Non-Fiction': 260, 'Textbooks': 180, 'Comics': 130, 'Magazines': 90}
]

# Prepare the data
months = [entry['Month'] for entry in data]
children_books = [entry["Children's Books"] for entry in data]
novels = [entry['Novels'] for entry in data]
non_fiction = [entry['Non-Fiction'] for entry in data]
textbooks = [entry['Textbooks'] for entry in data]
comics = [entry['Comics'] for entry in data]
magazines = [entry['Magazines'] for entry in data]

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Define the width of the bars
bar_width = 0.5

# Define the positions of the bars
bar_positions = np.arange(len(months))

# Start the stack at 0 for the first category
previous = np.zeros(len(months))

# Plot each category
categories = [children_books, novels, non_fiction, textbooks, comics, magazines]
colors = ['skyblue', 'orange', 'lightgreen', 'pink', 'yellow', 'purple']
labels = ["Children's Books", 'Novels', 'Non-Fiction', 'Textbooks', 'Comics', 'Magazines']

# Add each category to the stack
for category, color, label in zip(categories, colors, labels):
    ax.bar(bar_positions, category, bar_width, bottom=previous, label=label, color=color)
    previous += category

# Add some text for labels, title, and custom x-axis tick labels
ax.set_xlabel('Month')
ax.set_ylabel('Number of Books Sold')
ax.set_title('Books Sold by Month and Category')
ax.set_xticks(bar_positions)
ax.set_xticklabels(months, rotation=45)

# Add a legend
ax.legend()

# Display the plot
plt.tight_layout()
plt.show()