
import matplotlib.pyplot as plt

# Data points
book_titles = ["Pride and Prejudice", "1984", "To Kill a Mockingbird", "The Great Gatsby", "Moby Dick", "War and Peace", 
               "The Catcher in the Rye", "Crime and Punishment", "Ulysses", "Brave New World", "Animal Farm", "Jane Eyre"]
copies_sold = [1300, 850, 950, 600, 400, 700, 1100, 500, 450, 750, 800, 900]

# Modify the plot size
plt.figure(figsize=(10, 14))

# Create a vertical histogram
plt.bar(book_titles, copies_sold, color="#e74c3c", edgecolor="#c0392b", width=0.4)

# Customize the display
plt.ylabel('Number of Copies Sold', fontsize=12)
plt.xlabel('Book Title', fontsize=12)
plt.title('Number of Copies Sold for Various Books', fontsize=16)

# Show grid
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha="right")

# Display the histogram
plt.tight_layout()
plt.show()