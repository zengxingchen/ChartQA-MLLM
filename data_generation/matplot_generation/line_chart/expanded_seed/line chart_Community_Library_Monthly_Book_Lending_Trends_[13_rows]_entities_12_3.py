
import matplotlib.pyplot as plt

# Chart table data provided
data = [
    {'Month': 'January', "Children's Books": 450, 'Cookbooks': 270, 'Fiction': 700, 'Non-Fiction': 500, 'Travel Guides': 320},
    {'Month': 'February', "Children's Books": 420, 'Cookbooks': 220, 'Fiction': 670, 'Non-Fiction': 470, 'Travel Guides': 300},
    {'Month': 'March', "Children's Books": 460, 'Cookbooks': 240, 'Fiction': 710, 'Non-Fiction': 520, 'Travel Guides': 310},
    {'Month': 'April', "Children's Books": 480, 'Cookbooks': 260, 'Fiction': 730, 'Non-Fiction': 540, 'Travel Guides': 330},
    {'Month': 'May', "Children's Books": 500, 'Cookbooks': 280, 'Fiction': 750, 'Non-Fiction': 560, 'Travel Guides': 350},
    {'Month': 'June', "Children's Books": 550, 'Cookbooks': 300, 'Fiction': 800, 'Non-Fiction': 600, 'Travel Guides': 400},
    {'Month': 'July', "Children's Books": 530, 'Cookbooks': 290, 'Fiction': 820, 'Non-Fiction': 610, 'Travel Guides': 370},
    {'Month': 'August', "Children's Books": 540, 'Cookbooks': 310, 'Fiction': 810, 'Non-Fiction': 620, 'Travel Guides': 360},
    {'Month': 'September', "Children's Books": 510, 'Cookbooks': 280, 'Fiction': 790, 'Non-Fiction': 580, 'Travel Guides': 340},
    {'Month': 'October', "Children's Books": 470, 'Cookbooks': 260, 'Fiction': 760, 'Non-Fiction': 540, 'Travel Guides': 330},
    {'Month': 'November', "Children's Books": 460, 'Cookbooks': 250, 'Fiction': 720, 'Non-Fiction': 510, 'Travel Guides': 320},
    {'Month': 'December', "Children's Books": 480, 'Cookbooks': 300, 'Fiction': 740, 'Non-Fiction': 550, 'Travel Guides': 350}
]

# Extracting Months for the x-axis
months = [entry['Month'] for entry in data]

# Extracting values for each category to create multiple series
childrens_books = [entry["Children's Books"] for entry in data]
cookbooks = [entry['Cookbooks'] for entry in data]
fiction = [entry['Fiction'] for entry in data]
non_fiction = [entry['Non-Fiction'] for entry in data]
travel_guides = [entry['Travel Guides'] for entry in data]

# Plotting the lines with different styles and markers
plt.plot(months, childrens_books, marker='o', linestyle='-', color='blue', label="Children's Books")
plt.plot(months, cookbooks, marker='s', linestyle='--', color='red', label='Cookbooks')
plt.plot(months, fiction, marker='^', linestyle='-.', color='green', label='Fiction')
plt.plot(months, non_fiction, marker='x', linestyle=':', color='purple', label='Non-Fiction')
plt.plot(months, travel_guides, marker='d', linestyle='-', color='orange', label='Travel Guides')

# Adding title and labels
plt.title('Monthly Sales by Book Type')
plt.xlabel('Month')
plt.ylabel('Sales (Units)')

# Rotating the x-axis labels for better readability
plt.xticks(rotation=45)

# Adding the legend
plt.legend()

# Optionally, you could use `plt.grid()` to add a grid
plt.grid(True)

# Showing the plot
plt.tight_layout() # To ensure everything fits without overlap
plt.show()