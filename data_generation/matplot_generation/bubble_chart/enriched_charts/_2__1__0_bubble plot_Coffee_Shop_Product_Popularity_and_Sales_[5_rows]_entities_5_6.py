
import matplotlib.pyplot as plt

# Data points
authors = [
    'J.K. Rowling', 'George R.R. Martin', 'J.R.R. Tolkien', 'Agatha Christie', 'Stephen King',
    'Dan Brown', 'J.D. Salinger', 'Jane Austen', 'Mark Twain', 'Charles Dickens',
    'Ernest Hemingway', 'F. Scott Fitzgerald', 'Harper Lee', 'Mary Shelley', 'Leo Tolstoy',
    'Gabriel Garcia Marquez', 'H.G. Wells', 'Isaac Asimov', 'Arthur Conan Doyle', 'Edgar Allan Poe',
    'Herman Melville', 'Virginia Woolf'
]
average_book_sales = [
    80000000, 50000000, 70000000, 100000000, 60000000, 55000000, 45000000, 40000000,
    35000000, 75000000, 30000000, 20000000, 15000000, 18000000, 17000000, 25000000,
    12000000, 35000000, 20000000, 14000000, 11000000, 16000000
]
number_of_published_works = [
    7, 30, 15, 85, 63, 7, 10, 6, 28, 20, 9, 5, 1, 8, 20, 25, 50, 40, 60, 15, 12, 9
]
popularity = [
    97, 94, 96, 93, 92, 89, 88, 90, 85, 91, 87, 80, 78, 77, 82, 83, 79, 84, 81, 76, 75, 74
]

# Bubble size is scaled by popularity
bubble_size = [pop * 10 for pop in popularity]

# Set the figure size
plt.figure(figsize=(18, 12))

# Create the scatter plot
plt.scatter(average_book_sales, number_of_published_works, s=bubble_size,
            color=['#FF5733', '#33FF57', '#3357FF', '#FFFF33', '#FF33FF', '#33FFFF', '#5733FF', '#57FF33', '#F3FF33', '#33FFF3', '#FF3357', '#33FF3F', 
                   '#FF5733', '#33FF57', '#3357FF', '#FFFF33', '#FF33FF', '#33FFFF', '#5733FF', '#57FF33', '#F3FF33', '#33FFF3'],
            alpha=0.7, edgecolors='w', linewidth=2)

# Title and labels
plt.title('Average Book Sales vs. Number of Published Works by Famous Authors', pad=20)
plt.xlabel('Average Book Sales')
plt.ylabel('Number of Published Works')

# Add author labels to the bubbles
for i, author in enumerate(authors):
    plt.text(average_book_sales[i], number_of_published_works[i], author, ha='center', va='center', fontsize=9)

# Show plot
plt.show()