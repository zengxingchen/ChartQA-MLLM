
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
stock_prices = [102, 105, 108, 110, 115, 118, 120, 125, 123, 121, 119, 117]

# Colors for each point
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF5',
    '#F5FF33', '#FF3380', '#8033FF', '#FF8033', '#3380FF', '#80FF33', '#FF3380'
]

# Change width and height of the chart
plt.figure(figsize=(14, 10))

# Scatter plot
plt.scatter(months, stock_prices, c=colors)

# Title and labels
plt.title('Monthly Stock Prices of Hypothetical Company', pad=20)
plt.xlabel('Month')
plt.ylabel('Stock Price (in $)')

# Adjust x-axis to show each month
plt.xticks(months)

# Show plot
plt.show()