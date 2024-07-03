
import matplotlib.pyplot as plt

# Table data provided
data = [
    {'Day': 'Monday', 'Book Sales': 150, 'Magazine Sales': 200, 'Newspaper Sales': 120, 'E-book Sales': 180, 'Audio Book Sales': 90},
    {'Day': 'Tuesday', 'Book Sales': 160, 'Magazine Sales': 210, 'Newspaper Sales': 130, 'E-book Sales': 170, 'Audio Book Sales': 85},
    {'Day': 'Wednesday', 'Book Sales': 140, 'Magazine Sales': 190, 'Newspaper Sales': 110, 'E-book Sales': 160, 'Audio Book Sales': 95},
    {'Day': 'Thursday', 'Book Sales': 170, 'Magazine Sales': 220, 'Newspaper Sales': 140, 'E-book Sales': 200, 'Audio Book Sales': 100},
    {'Day': 'Friday', 'Book Sales': 180, 'Magazine Sales': 230, 'Newspaper Sales': 150, 'E-book Sales': 210, 'Audio Book Sales': 105},
    {'Day': 'Saturday', 'Book Sales': 190, 'Magazine Sales': 240, 'Newspaper Sales': 160, 'E-book Sales': 220, 'Audio Book Sales': 110},
    {'Day': 'Sunday', 'Book Sales': 185, 'Magazine Sales': 235, 'Newspaper Sales': 155, 'E-book Sales': 215, 'Audio Book Sales': 115}
]

# Extracting data for plotting
days = [item['Day'] for item in data]
book_sales = [item['Book Sales'] for item in data]
magazine_sales = [item['Magazine Sales'] for item in data]
newspaper_sales = [item['Newspaper Sales'] for item in data]
ebook_sales = [item['E-book Sales'] for item in data]
audiobook_sales = [item['Audio Book Sales'] for item in data]

# Creating a line chart with a different line style and marker for each type
plt.figure(figsize=(14, 10))
plt.plot(days, book_sales, label='Book Sales', linestyle='-', marker='o', color='#1f77b4')
plt.plot(days, magazine_sales, label='Magazine Sales', linestyle='--', marker='s', color='#ff7f0e')
plt.plot(days, newspaper_sales, label='Newspaper Sales', linestyle='-.', marker='^', color='#2ca02c')
plt.plot(days, ebook_sales, label='E-book Sales', linestyle=':', marker='D', color='#d62728')
plt.plot(days, audiobook_sales, label='Audio Book Sales', linestyle='-', marker='*', color='#9467bd')

# Adding relevant titles and labels
plt.title('Weekly Media Sales', pad=20)
plt.xlabel('Day of the Week')
plt.ylabel('Number of Items Sold')
plt.legend(loc='upper left')

# Customizing the grid
plt.grid(True, linestyle='--', linewidth=0.5, color='gray')

# Adding annotations for E-book Sales
for i, txt in enumerate(ebook_sales):
    plt.annotate(txt, (days[i], ebook_sales[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Displaying the chart
plt.tight_layout()
plt.show()