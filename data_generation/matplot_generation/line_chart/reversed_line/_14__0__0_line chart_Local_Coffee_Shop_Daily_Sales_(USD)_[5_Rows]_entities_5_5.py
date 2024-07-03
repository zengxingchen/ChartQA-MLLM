
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
books_sold = [40, 38, 45, 42, 35, 30, 25, 20, 22, 28, 35, 40]

# Plotting the line chart
plt.figure(figsize=(16, 8))  # Change width and height of the chart
plt.plot(months, books_sold, marker='o', linestyle='-', color='#3498db', linewidth=2.5)  # Modify color scheme

# Adding title and labels
plt.title('Monthly Book Sales at Store XYZ', fontsize=20, y=1.05)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Books Sold (in units)', fontsize=14)

# Adding an annotation for the lowest sales
lowest_sales_index = books_sold.index(min(books_sold))
lowest_sales_month = months[lowest_sales_index]
plt.annotate('Lowest Sales', xy=(lowest_sales_index, min(books_sold)), xytext=(lowest_sales_index, min(books_sold) + 5),
             arrowprops=dict(facecolor='#e74c3c', shrink=0.05))

# Invert y-axis
plt.gca().invert_yaxis()

# Add a grid, set axis ranges and show the plot
plt.grid(True)
plt.ylim(45, 15)
plt.show()