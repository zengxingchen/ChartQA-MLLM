
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
stock_prices = [150, 142, 155, 147, 160, 172, 165, 170, 160, 158, 149, 145]

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(months, stock_prices, marker='o', linestyle='-', color='#1f77b4')

# Annotate the highest and lowest stock price points
plt.annotate('Highest\n172', xy=('June', 172), xytext=('July', 175),
             arrowprops=dict(facecolor='#d62728', shrink=0.05), color='#d62728')
plt.annotate('Lowest\n142', xy=('February', 142), xytext=('March', 145),
             arrowprops=dict(facecolor='#d62728', shrink=0.05), color='#d62728')

# Title and labels
plt.title('Monthly Stock Prices of ABC Corp in 2023')
plt.xlabel('Month')
plt.ylabel('Stock Price ($)')

# Customize the grid
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Invert y-axis
plt.gca().invert_yaxis()

# Show the plot
plt.show()