
import matplotlib.pyplot as plt

# Data from the provided chart table
data = [
    {'Month': 'January', 'Mystery': 450, 'Thriller': 520, 'Romance': 730, 'Science Fiction': 480, 'Non-Fiction': 610},
    {'Month': 'February', 'Mystery': 460, 'Thriller': 530, 'Romance': 740, 'Science Fiction': 490, 'Non-Fiction': 620},
    {'Month': 'March', 'Mystery': 470, 'Thriller': 540, 'Romance': 750, 'Science Fiction': 500, 'Non-Fiction': 630},
    {'Month': 'April', 'Mystery': 480, 'Thriller': 550, 'Romance': 760, 'Science Fiction': 510, 'Non-Fiction': 640},
    {'Month': 'May', 'Mystery': 490, 'Thriller': 560, 'Romance': 770, 'Science Fiction': 520, 'Non-Fiction': 650}
]

# Extracting months and sales data
months = [entry['Month'] for entry in data]
mystery_sales = [entry['Mystery'] for entry in data]
thriller_sales = [entry['Thriller'] for entry in data]
romance_sales = [entry['Romance'] for entry in data]
science_fiction_sales = [entry['Science Fiction'] for entry in data]
non_fiction_sales = [entry['Non-Fiction'] for entry in data]

# Plotting the stacked area chart
plt.figure(figsize=(10, 6))
plt.stackplot(months, mystery_sales, thriller_sales, romance_sales, science_fiction_sales, non_fiction_sales, labels=['Mystery', 'Thriller', 'Romance', 'Science Fiction', 'Non-Fiction'], alpha=0.8)

# Adding title and labels
plt.title('Book Sales by Genre Over Months')
plt.xlabel('Months')
plt.ylabel('Sales')

# Adding a legend
plt.legend(loc='upper left')

# Customizing the axes with grids, limits, and ticks
plt.grid(True)
plt.xlim(-1, len(months))
plt.xticks(rotation=45)
plt.ylim(0, max(mystery_sales + thriller_sales + romance_sales + science_fiction_sales + non_fiction_sales) + 100)

# Displaying the plot
plt.tight_layout()
plt.show()