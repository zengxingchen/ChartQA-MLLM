
import matplotlib.pyplot as plt

# Sample data
data = [
    {'Book_Title': 'To Kill a Mockingbird', ' Genre': ' Classic', ' Checkouts_per_Month': 12, ' Average_Days_Borrowed': 22},
    {'Book_Title': 'The Alchemist', ' Genre': ' Novel', ' Checkouts_per_Month': 8, ' Average_Days_Borrowed': 18},
    {'Book_Title': 'Becoming', ' Genre': ' Memoir', ' Checkouts_per_Month': 9, ' Average_Days_Borrowed': 25},
    {'Book_Title': "Harry Potter: The Sorcerer's Stone", ' Genre': ' Fiction', ' Checkouts_per_Month': 14, ' Average_Days_Borrowed': 30},
    {'Book_Title': '1984', ' Genre': ' Dystopian', ' Checkouts_per_Month': 10, ' Average_Days_Borrowed': 20},
    {'Book_Title': 'Educated', ' Genre': ' Non-fiction', ' Checkouts_per_Month': 7, ' Average_Days_Borrowed': 28},
    {'Book_Title': 'The Great Gatsby', ' Genre': ' Classic', ' Checkouts_per_Month': 5, ' Average_Days_Borrowed': 24},
    {'Book_Title': 'Where the Crawdads Sing', ' Genre': ' Mystery', ' Checkouts_per_Month': 11, ' Average_Days_Borrowed': 27},
    {'Book_Title': 'The Subtle Art of Not Giving a F*ck', ' Genre': ' Self-help', ' Checkouts_per_Month': 13, ' Average_Days_Borrowed': 21}
]

# Extracting data
book_titles = [book['Book_Title'] for book in data]
checkouts = [book[' Checkouts_per_Month'] for book in data]
days_borrowed = [book[' Average_Days_Borrowed'] for book in data]
genres = [book[' Genre'].strip() for book in data]  # Removing any leading and trailing spaces

# Bubble sizes - scaled for better visualization
bubble_sizes = [checkout * 10 for checkout in checkouts]

# Create a color map for the genres
unique_genres = list(set(genres))
colors = plt.cm.rainbow(np.linspace(0, 1, len(unique_genres)))
genre_to_color = {genre: color for genre, color in zip(unique_genres, colors)}

# Plotting
plt.figure(figsize=(14, 8))

for i, book_title in enumerate(book_titles):
    plt.scatter(checkouts[i], days_borrowed[i], s=bubble_sizes[i],
                color=genre_to_color[genres[i]], alpha=0.6, label=genres[i],
                edgecolors='w', linewidth=0.5)

# Since we are repeating labels, let's clean them up
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())

# Title and labels
plt.title('Library Book Popularity and Borrowing Duration')
plt.xlabel('Checkouts per Month')
plt.ylabel('Average Days Borrowed')

# Adding book titles as annotations to each bubble
for i, book_title in enumerate(book_titles):
    plt.text(checkouts[i], days_borrowed[i], book_title, ha='center', va='center',
             fontsize=8, weight='bold', color='black')

# Show the plot
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()