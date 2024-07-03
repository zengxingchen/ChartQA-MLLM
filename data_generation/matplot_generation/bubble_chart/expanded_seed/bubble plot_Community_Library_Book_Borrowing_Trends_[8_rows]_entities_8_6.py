
import matplotlib.pyplot as plt

# Your provided dataset
books = [
    {'Title': 'To Kill a Mockingbird', 'Author': 'Harper Lee', 'Genre': 'Classic Fiction', 'Monthly Checkouts': 120, 'Average Borrowing Duration (days)': 15, 'Reader Satisfaction (1-5)': 4.7},
    {'Title': '1984', 'Author': 'George Orwell', 'Genre': 'Dystopian', 'Monthly Checkouts': 95, 'Average Borrowing Duration (days)': 12, 'Reader Satisfaction (1-5)': 4.5},
    {'Title': 'The Great Gatsby', 'Author': 'F. Scott Fitzgerald', 'Genre': 'Classic Fiction', 'Monthly Checkouts': 70, 'Average Borrowing Duration (days)': 10, 'Reader Satisfaction (1-5)': 4.6},
    {'Title': 'Becoming', 'Author': 'Michelle Obama', 'Genre': 'Memoir', 'Monthly Checkouts': 80, 'Average Borrowing Duration (days)': 18, 'Reader Satisfaction (1-5)': 4.8},
    {'Title': 'Educated', 'Author': 'Tara Westover', 'Genre': 'Memoir', 'Monthly Checkouts': 90, 'Average Borrowing Duration (days)': 16, 'Reader Satisfaction (1-5)': 4.9},
    {'Title': 'The Subtle Art of Not Giving a F*ck', 'Author': 'Mark Manson', 'Genre': 'Self-help', 'Monthly Checkouts': 110, 'Average Borrowing Duration (days)': 20, 'Reader Satisfaction (1-5)': 4.3},
    {'Title': 'Sapiens', 'Author': 'Yuval Noah Harari', 'Genre': 'Non-fiction', 'Monthly Checkouts': 100, 'Average Borrowing Duration (days)': 25, 'Reader Satisfaction (1-5)': 4.7},
    {'Title': 'Where the Crawdads Sing', 'Author': 'Delia Owens', 'Genre': 'Fiction', 'Monthly Checkouts': 130, 'Average Borrowing Duration (days)': 17, 'Reader Satisfaction (1-5)': 4.8}
]

# Bubble chart parameters
x = [book['Monthly Checkouts'] for book in books]  # x-axis data
y = [book['Average Borrowing Duration (days)'] for book in books]  # y-axis data
sizes = [book['Reader Satisfaction (1-5)'] * 100 for book in books]  # Bubble sizes
colors = [book['Genre'] for book in books]  # Bubble colors

# Convert genres to unique numbers for color mapping
unique_genres = list(set(colors))
color_map = {genre: i for i, genre in enumerate(unique_genres)}
bubble_colors = [color_map[genre] for genre in colors]

# Create the plot
plt.figure(figsize=(14, 8))
bubble = plt.scatter(x, y, s=sizes, c=bubble_colors, alpha=0.5)

# Create a legend for genres
legend_labels = {i: genre for genre, i in color_map.items()}
handles = [plt.Line2D([0], [0], marker='o', color='w', label=genre, 
             markerfacecolor=plt.cm.viridis(color_map[genre]/len(unique_genres)), markersize=10) 
             for genre in unique_genres]
plt.legend(handles=handles, title="Genre")

# Title and labels
plt.title('Library Book Borrowing Patterns')
plt.xlabel('Monthly Checkouts')
plt.ylabel('Average Borrowing Duration (days)')

# Adding titles to the bubbles (optional)
for i, book in enumerate(books):
    plt.text(x[i], y[i], book['Title'], ha='center', va='center', fontsize=8)

# Show plot
plt.tight_layout()
plt.show()