
import matplotlib.pyplot as plt

# Data points
days = [i for i in range(1, 31)]
stock_prices = [100, 102, 101, 103, 105, 108, 110, 109, 107, 106, 108, 110, 113, 115, 117, 120, 118, 121, 123, 125, 127, 130, 128, 126, 129, 131, 134, 136, 135, 137]

# Creating the line chart
plt.figure(figsize=(16, 10))  # Change the width and height of the chart
plt.plot(days, stock_prices, marker='o', color='#2ca02c', label='Daily Stock Prices')  # Specific color code

# Annotation for a significant day
plt.annotate('Peak', xy=(30, 137), xytext=(25, 135),
             arrowprops=dict(facecolor='#d62728', shrink=0.05))

# Adding the x-axis label, y-axis label, title, legend, and grid
plt.xlabel('Day of the Month')
plt.ylabel('Stock Price ($)')
plt.title('Daily Stock Prices of Company XYZ - June 2023', pad=20)
plt.legend(loc='upper left')
plt.grid(True)

# Display the chart
plt.show()