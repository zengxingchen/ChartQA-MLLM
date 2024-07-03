
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
stock_prices = [150, 160, 155, 165, 170, 175, 180, 190, 185, 195, 200, 210]

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(months, stock_prices, marker='o', linestyle='-', color='#4CAF50')

# Annotate the highest and lowest stock price points
plt.annotate('Highest\n210$', xy=('December', 210), xytext=('November', 205),
             arrowprops=dict(facecolor='#FF0000', shrink=0.05), color='#FF0000')
plt.annotate('Lowest\n150$', xy=('January', 150), xytext=('February', 145),
             arrowprops=dict(facecolor='#FF0000', shrink=0.05), color='#FF0000')

# Title and labels
plt.title('Monthly Stock Prices of a Tech Company', pad=20)
plt.xlabel('Month')
plt.ylabel('Stock Price ($)')

# Customize the grid
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Show the plot
plt.show()