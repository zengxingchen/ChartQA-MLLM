
import matplotlib.pyplot as plt

# Data
categories = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
book_sales = [55, 48, 60, 52, 70, 75, 82, 65, 67, 64, 58, 55]

# Colors for each bar
colors = ['#FF5733', '#FF8D33', '#FFC133', '#FFE333', '#E3FF33', '#A8FF33', '#63FF33', '#33FF57', '#33FFAB', '#33FFE3', '#33C8FF', '#338FFF']

# Create a horizontal bar chart
plt.figure(figsize=(14, 8))  # Change the figure size (width x height)
bar_height = 0.7  # Change the bar height
plt.barh(categories, book_sales, color=colors, height=bar_height)

# Setting the title and labels
plt.title('Monthly Book Sales', pad=20)
plt.xlabel('Book Sales (in thousands)')
plt.ylabel('Month')

# Adjust the limits if necessary
plt.xlim([45, max(book_sales) + 5])

# Display the chart
plt.tight_layout()
plt.show()