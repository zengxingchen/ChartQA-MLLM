
import matplotlib.pyplot as plt
import squarify

# Data
genres = [
    'Fantasy', 'Romance', 'Thriller', 'Science Fiction', 'Mystery', 
    'Biography', 'Self-Help', 'Historical Fiction', 'Non-Fiction', 'Graphic Novels', 
    'Classics', "Children's Books", 'Horror', 'Poetry', 'Drama', 
    'Young Adult', 'Adventure', 'Humor', 'Philosophy'
]
books_sold = [
    3500, 2800, 2300, 2000, 1700, 
    1500, 1400, 1300, 1200, 1000, 
    800, 750, 600, 500, 400, 
    300, 200, 150, 100
]
colors = [
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', 
    '#ffb3e6', '#ff6666', '#c2f0c2', '#6666ff', '#ffb3b3', 
    '#99c2ff', '#c2e6ff', '#ffcccc', '#f0c2c2', '#ccffcc', 
    '#e6c2ff', '#f2ffb3', '#e6f0ff', '#ffccff'
]

# Plot
plt.figure(figsize=(14, 10))
squarify.plot(sizes=books_sold, label=genres, color=colors, alpha=0.8)
plt.title('Popular Book Genres by Estimated Number of Books Sold (in Millions)', fontsize=18, pad=20)
plt.axis('off')
plt.show()