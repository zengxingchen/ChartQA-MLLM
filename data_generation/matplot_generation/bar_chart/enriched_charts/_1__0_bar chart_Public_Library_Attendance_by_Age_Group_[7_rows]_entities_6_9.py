
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
book_sales = [55, 45, 60, 50, 65, 75, 80, 70, 65, 60, 55, 50]

# Colors for each bar
colors = ['#FF5733', '#FF8D33', '#FFC133', '#FFE333', '#E3FF33', '#A8FF33', '#63FF33', '#33FF57', '#33FFAB', '#33FFE3', '#33C8FF', '#338FFF']

# Create a vertical bar chart
plt.figure(figsize=(12, 6))  # Change the figure size (width x height)
bar_width = 0.6  # Change the bar width
plt.bar(months, book_sales, color=colors, width=bar_width)

# Setting the title and labels
plt.title('Monthly Book Sales')
plt.ylabel('Book Sales (in thousands)')
plt.xlabel('Month')

# Adjust the limits if necessary
plt.ylim([0, max(book_sales) + 10])

# Display the chart
plt.tight_layout()
plt.show()