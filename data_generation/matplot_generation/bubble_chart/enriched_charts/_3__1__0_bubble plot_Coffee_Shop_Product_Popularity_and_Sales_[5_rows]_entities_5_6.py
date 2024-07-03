
import matplotlib.pyplot as plt

authors = [
    'J.K. Rowling', 'Stephen King', 'James Patterson', 'Agatha Christie', 'George R.R. Martin',
    'Dan Brown', 'J.R.R. Tolkien', 'Harper Lee', 'Ernest Hemingway', 'Jane Austen',
    'Mark Twain', 'Charles Dickens', 'F. Scott Fitzgerald', 'Leo Tolstoy', 'Arthur Conan Doyle',
    'Gabriel Garcia Marquez', 'J.D. Salinger', 'Isabel Allende', 'Toni Morrison', 'Margaret Atwood',
    'John Grisham', 'Neil Gaiman'
]
books_sold = [
    500000000, 350000000, 300000000, 2000000000, 90000000, 220000000, 150000000, 40000000,
    40000000, 100000000, 120000000, 200000000, 25000000, 80000000, 100000000, 50000000,
    65000000, 70000000, 10000000, 20000000, 275000000, 60000000
]
years_active = [
    25, 50, 45, 56, 50, 25, 45, 20, 40, 41, 47, 58, 20, 41, 40, 30, 30, 35, 48, 54, 40, 35
]
popularity = [
    95, 90, 85, 93, 80, 88, 96, 70, 85, 92, 87, 94, 83, 86, 89, 84, 79, 78, 82, 81, 86, 80
]

bubble_size = [pop * 10 for pop in popularity]

plt.figure(figsize=(18, 12))

plt.scatter(books_sold, years_active, s=bubble_size,
            color=['#FF5733', '#33FF57', '#3357FF', '#FFFF33', '#FF33FF', '#33FFFF', '#5733FF', '#57FF33', '#F3FF33', '#33FFF3', '#FF3357', '#33FF3F', 
                   '#FF5733', '#33FF57', '#3357FF', '#FFFF33', '#FF33FF', '#33FFFF', '#5733FF', '#57FF33', '#F3FF33', '#33FFF3'],
            alpha=0.7, edgecolors='w', linewidth=2)

plt.title('Books Sold vs. Years Active by Renowned Authors', pad=20)
plt.xlabel('Books Sold')
plt.ylabel('Years Active')

for i, author in enumerate(authors):
    plt.text(books_sold[i], years_active[i], author, ha='center', va='center', fontsize=9)

plt.show()