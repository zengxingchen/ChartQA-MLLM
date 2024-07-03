
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
book_sales = [55, 45, 60, 50, 70, 75, 85, 65, 60, 55, 50, 45]

# Colors for each bar
colors = ['#3366CC', '#DC3912', '#FF9900', '#109618', '#990099', '#3B3EAC', '#0099C6', '#DD4477', '#66AA00', '#B82E2E', '#316395', '#994499']

# Create a horizontal bar chart
plt.figure(figsize=(14, 8))  # Change the figure size (width x height)
bar_height = 0.5  # Change the bar width
plt.barh(months, book_sales, color=colors, height=bar_height)

# Setting the title and labels
plt.title('Monthly Travel Book Sales', pad=20)
plt.xlabel('Book Sales (in thousands)')
plt.ylabel('Month')

# Adjust the limits
plt.xlim([40, max(book_sales) + 10])

# Display the chart
plt.tight_layout()
plt.show()