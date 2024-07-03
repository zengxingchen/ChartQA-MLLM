
import matplotlib.pyplot as plt

# Data provided in the table
data = [
    {'Month': 'January', 'Book Sales (thousands)': 50, 'Location': 'Bookstore A'},
    {'Month': 'February', 'Book Sales (thousands)': 45, 'Location': 'Bookstore A'},
    {'Month': 'March', 'Book Sales (thousands)': 40, 'Location': 'Bookstore A'},
    {'Month': 'April', 'Book Sales (thousands)': 55, 'Location': 'Bookstore A'},
    {'Month': 'May', 'Book Sales (thousands)': 65, 'Location': 'Bookstore A'},
    {'Month': 'June', 'Book Sales (thousands)': 60, 'Location': 'Bookstore A'},
    {'Month': 'July', 'Book Sales (thousands)': 70, 'Location': 'Bookstore A'},
    {'Month': 'August', 'Book Sales (thousands)': 80, 'Location': 'Bookstore A'},
    {'Month': 'September', 'Book Sales (thousands)': 75, 'Location': 'Bookstore A'},
    {'Month': 'October', 'Book Sales (thousands)': 85, 'Location': 'Bookstore A'},
    {'Month': 'November', 'Book Sales (thousands)': 90, 'Location': 'Bookstore A'},
    {'Month': 'December', 'Book Sales (thousands)': 95, 'Location': 'Bookstore A'}
]

# Extracting the months and the book sales
months = [entry['Month'] for entry in data]
book_sales = [entry['Book Sales (thousands)'] for entry in data]

# Creating the line chart
plt.figure(figsize=(14, 8))  # Setting the figure size

# Plotting the data with various visual encodings
plt.plot(months, book_sales, color='#4b0082', linestyle='--', linewidth=2, 
         marker='s', markersize=8, markerfacecolor='#32cd32', markeredgewidth=2, 
         markeredgecolor='#8b0000', label='Book Sales at Bookstore A')

# Adding titles and labels
plt.title('Monthly Book Sales at Bookstore A', fontsize=18, loc='right')
plt.xlabel('Month', fontsize=14)
plt.ylabel('Book Sales (thousands)', fontsize=14)

# Adding a legend
plt.legend(loc='upper left')

# Adding a grid
plt.grid(True)

# Adding customization with font size and style for x and y ticks
plt.xticks(fontsize=12, fontweight='bold', rotation=30)
plt.yticks(fontsize=12, fontweight='bold')

# Adding annotations for specific points
plt.annotate('Highest Sales', xy=('December', 95), xytext=('October', 95),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, color='blue')

# Show plot
plt.show()