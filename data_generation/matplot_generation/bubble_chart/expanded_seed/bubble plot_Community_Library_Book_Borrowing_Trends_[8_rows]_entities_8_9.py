
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Month': 'January', 'Book Genre': 'Fiction', 'Borrowed Count': 320, 'Overdue Returns': 15, 'Average Borrowing Duration (days)': 18},
    {'Month': 'February', 'Book Genre': 'Science Fiction', 'Borrowed Count': 280, 'Overdue Returns': 10, 'Average Borrowing Duration (days)': 22},
    {'Month': 'March', 'Book Genre': 'Thriller', 'Borrowed Count': 310, 'Overdue Returns': 7, 'Average Borrowing Duration (days)': 17},
    {'Month': 'April', 'Book Genre': 'Romance', 'Borrowed Count': 270, 'Overdue Returns': 13, 'Average Borrowing Duration (days)': 15},
    {'Month': 'May', 'Book Genre': 'Biographies', 'Borrowed Count': 300, 'Overdue Returns': 8, 'Average Borrowing Duration (days)': 20},
    {'Month': 'June', 'Book Genre': "Children's Literature", 'Borrowed Count': 350, 'Overdue Returns': 9, 'Average Borrowing Duration (days)': 10},
    {'Month': 'July', 'Book Genre': 'History', 'Borrowed Count': 230, 'Overdue Returns': 14, 'Average Borrowing Duration (days)': 25},
    {'Month': 'August', 'Book Genre': 'Self-help', 'Borrowed Count': 200, 'Overdue Returns': 5, 'Average Borrowing Duration (days)': 30}
]

# Preparing the data for plotting
months = [entry['Month'] for entry in data]
borrowed_counts = [entry['Borrowed Count'] for entry in data]
overdue_returns = [entry['Overdue Returns'] for entry in data]
borrowing_duration = [entry['Average Borrowing Duration (days)'] for entry in data]
genres = [entry['Book Genre'] for entry in data]

# Create the figure and axis objects
fig, ax = plt.subplots(figsize=(10, 8))

# Map Borrowing Duration to a color
colors = borrowing_duration
# Use a colormap to map numerical values to colors
scatter = ax.scatter(months, borrowed_counts, s=[count*10 for count in overdue_returns], c=colors, cmap='viridis', alpha=0.6, edgecolors='w', linewidth=0.5)

# Label the bubbles with the book genre
for i, genre in enumerate(genres):
    ax.text(months[i], borrowed_counts[i], genre, ha='center', va='center', size=8)

# Add a color bar to show the Average Borrowing Duration
cbar = plt.colorbar(scatter)
cbar.set_label('Average Borrowing Duration (days)')

# Set labels and title
ax.set_xlabel('Month')
ax.set_ylabel('Borrowed Count')
ax.set_title('Library Genre Popularity and Overdue Returns by Month')

# Display the plot
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
plt.tight_layout()  # Adjust the padding between and around subplots
plt.show()