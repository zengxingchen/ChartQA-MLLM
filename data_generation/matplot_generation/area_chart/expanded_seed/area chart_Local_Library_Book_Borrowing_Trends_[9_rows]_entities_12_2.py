
import matplotlib.pyplot as plt

# Given data
data = [
    {'Month': 'January', ' Number of Books Borrowed': 870},
    {'Month': 'February', ' Number of Books Borrowed': 940},
    {'Month': 'March', ' Number of Books Borrowed': 1010},
    {'Month': 'April', ' Number of Books Borrowed': 1230},
    {'Month': 'May', ' Number of Books Borrowed': 1150},
    {'Month': 'June', ' Number of Books Borrowed': 960},
    {'Month': 'July', ' Number of Books Borrowed': 980},
    {'Month': 'August', ' Number of Books Borrowed': 1070},
    {'Month': 'September', ' Number of Books Borrowed': 1130},
    {'Month': 'October', ' Number of Books Borrowed': 1200},
    {'Month': 'November', ' Number of Books Borrowed': 1250},
    {'Month': 'December', ' Number of Books Borrowed': 1300}
]

# Extracting the months and the corresponding numbers of books borrowed
months = [entry['Month'] for entry in data]
books_borrowed = [entry[' Number of Books Borrowed'] for entry in data]

# Creating the area chart
plt.fill_between(months, books_borrowed, color="skyblue", alpha=0.4)
plt.plot(months, books_borrowed, color="Slateblue", alpha=0.6, linewidth=2)

# Adding a title and labels
plt.title("Number of Books Borrowed per Month")
plt.xlabel("Month")
plt.ylabel("Number of Books Borrowed")

# Enhancing the visualization
plt.xticks(rotation=45)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

# Show the plot
plt.show()