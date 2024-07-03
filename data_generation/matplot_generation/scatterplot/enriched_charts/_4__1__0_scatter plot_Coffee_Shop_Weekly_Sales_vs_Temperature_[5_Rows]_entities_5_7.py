
import matplotlib.pyplot as plt

# Data
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
stock_prices = [100, 102, 98, 105, 107, 110, 108, 115, 120, 112, 114, 118, 116, 119, 121, 125, 123, 126, 129, 130]
trading_volumes = [1500, 1600, 1400, 1700, 1800, 2000, 1900, 2100, 2200, 2000, 2050, 1900, 1800, 1950, 2100, 2500, 2300, 2400, 2600, 2700]

# Scatter plot
plt.figure(figsize=(14, 8))  # Width:14, Height:8
plt.scatter(days, stock_prices, color='#1f77b4', label='Stock Prices')
plt.scatter(days, trading_volumes, color='#ff7f0e', label='Trading Volumes')

# Customize the plot
plt.title('Stock Prices and Daily Trading Volume Over 20 Days', pad=30)
plt.xlabel('Day')
plt.ylabel('Values')
plt.legend(loc='upper right')
plt.grid(True)

# Show the plot
plt.show()