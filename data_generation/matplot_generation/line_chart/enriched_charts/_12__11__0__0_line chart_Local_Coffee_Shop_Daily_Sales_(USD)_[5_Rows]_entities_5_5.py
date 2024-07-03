
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
book_sales = [500, 480, 520, 610, 700, 850, 900, 870, 720, 680, 620, 580]

# Plotting the line chart
plt.figure(figsize=(14, 7))  # Change width and height of the chart
plt.plot(months, book_sales, marker='o', linestyle='-', color='#FF6347', linewidth=2.5)  # Modify color scheme

# Adding title and labels
plt.title('Monthly Book Sales in 2023', fontsize=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Book Sales', fontsize=14)

# Adding an annotation for the highest book sales
highest_sales_index = book_sales.index(max(book_sales))
highest_sales_month = months[highest_sales_index]
plt.annotate('Peak Sales', xy=(highest_sales_index, max(book_sales)), xytext=(highest_sales_index, max(book_sales) + 50),
             arrowprops=dict(facecolor='#32CD32', shrink=0.05))

# Add a grid, set axis ranges and show the plot
plt.grid(True)
plt.ylim(400, 950)
plt.show()