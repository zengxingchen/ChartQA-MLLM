
import matplotlib.pyplot as plt

# Given data
data = [
    {'Month': 'January', 'Romance': 5, 'Mystery': 7, 'Thriller': 4, 'Science Fiction': 6, 'Fantasy': 8, 'Non-Fiction': 3, 'Biography': 2},
    {'Month': 'February', 'Romance': 4, 'Mystery': 8, 'Thriller': 5, 'Science Fiction': 5, 'Fantasy': 7, 'Non-Fiction': 3, 'Biography': 3},
    # ... (remaining data)
    {'Month': 'December', 'Romance': 7, 'Mystery': 7, 'Thriller': 6, 'Science Fiction': 9, 'Fantasy': 12, 'Non-Fiction': 5, 'Biography': 4}
]

# Extracting months and genre names
months = [entry['Month'] for entry in data]
genres = list(data[0].keys())[1:]  # Assuming all dicts have the same keys

# Preparing data for stacking
values_by_genre = {genre: [entry[genre] for entry in data] for genre in genres}

# Initial bottom values for the stacking
bottoms = [0] * len(months)

# Define colors to differentiate the genres
colors = ['skyblue', 'sandybrown', 'lightgreen', 'lightcoral', 'mediumpurple', 'goldenrod', 'salmon']

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Create separate bar stacks for each genre
for i, genre in enumerate(genres):
    ax.bar(months, values_by_genre[genre], label=genre, bottom=bottoms, color=colors[i])
    # Update bottoms for next stack
    bottoms = [bottoms[j] + values_by_genre[genre][j] for j in range(len(bottoms))]

# Add some visual improvements
ax.set_title('Monthly Book Sales by Genre')
ax.set_xlabel('Month')
ax.set_ylabel('Number of Books Sold')
ax.set_xticklabels(months, rotation=45)
ax.legend(title='Genres', bbox_to_anchor=(1.05, 1), loc='upper left')
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Tight layout to fit legend
plt.tight_layout(rect=[0, 0, 0.85, 1])

# Show the plot
plt.show()