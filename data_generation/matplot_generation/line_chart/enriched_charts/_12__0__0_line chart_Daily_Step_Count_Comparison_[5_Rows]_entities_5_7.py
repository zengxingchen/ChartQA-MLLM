
import matplotlib.pyplot as plt

# Data
months = ['2022-Jan', '2022-Feb', '2022-Mar', '2022-Apr', '2022-May', '2022-Jun', '2022-Jul', '2022-Aug', '2022-Sep', '2022-Oct', '2022-Nov', '2022-Dec']
book_sales = [150, 180, 300, 450, 500, 400, 600, 700, 750, 900, 950, 1200]

# Plotting the line chart
plt.figure(figsize=(14, 7))  # Adjusted width and height
plt.plot(months, book_sales, color='#2ca02c', marker='o', linestyle='-', linewidth=2)  # Different color and marker style

# Annotate a specific point with the label
plt.annotate('Holiday Season Boost', xy=('2022-Dec', 1200), xytext=('2022-Oct', 950),
             arrowprops=dict(facecolor='#ff7f0e', arrowstyle='->'))

# Adding a title and labels
plt.title('Monthly Book Sales in 2022', pad=20)  # Changed topic and added padding
plt.xlabel('Month')
plt.ylabel('Book Sales')

# Show the plot
plt.show()