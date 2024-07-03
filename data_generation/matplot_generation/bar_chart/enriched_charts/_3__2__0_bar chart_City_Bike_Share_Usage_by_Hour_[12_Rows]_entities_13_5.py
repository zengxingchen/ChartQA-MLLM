
import matplotlib.pyplot as plt

# Data
books = ['To Kill a Mockingbird', '1984', 'Pride and Prejudice', 'The Great Gatsby', 'Moby Dick', 'War and Peace', 'Crime and Punishment', 'The Catcher in the Rye', 'The Hobbit', 'The Odyssey', 'Jane Eyre', 'The Brothers Karamazov']
copies_sold = [380, 420, 350, 500, 280, 310, 330, 410, 450, 370, 390, 360]

# Colors for each bar
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', '#33FFA1', '#FF8333', '#33A1FF', '#FF33FF', '#33FF83', '#8333FF', '#A1FF33']

# Plotting the bar chart horizontally
plt.figure(figsize=(12, 8))   # Change width and height of the chart
plt.barh(books, copies_sold, color=colors, edgecolor='black', height=0.7)  # Change height for bars and apply color scheme

# Chart title and labels
plt.title('Number of Copies Sold of Classic Books', fontsize=18)
plt.xlabel('Number of Copies Sold', fontsize=14)

# Setting the xlim to provide better clarity for copies sold values
plt.xlim(0, max(copies_sold) + 100)

# Display the chart
plt.tight_layout()
plt.show()