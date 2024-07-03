
import matplotlib.pyplot as plt

# Data
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
stock_price = [120.5, 121.8, 119.3, 123.4, 124.2, 126.5, 125.0, 127.3, 128.8, 130.2, 129.5, 131.0, 132.4, 133.8, 134.5, 136.0, 137.5, 138.8, 140.2, 141.5]
trading_volume = [1500, 1600, 1400, 1700, 1650, 1800, 1750, 1900, 2000, 2100, 2050, 2150, 2200, 2250, 2300, 2400, 2450, 2500, 2600, 2700]

# Scatter plot
plt.figure(figsize=(14, 10))  # Width:14, Height:10
plt.scatter(days, stock_price, color='#1f77b4', label='Stock Price')  # Blue
plt.scatter(days, trading_volume, color='#ff7f0e', label='Trading Volume')  # Orange

# Customize the plot
plt.title('Stock Prices and Trading Volume Over 20 Days', pad=20)
plt.xlabel('Day')
plt.ylabel('Measurements')
plt.legend(loc='upper right')
plt.grid(True)

# Show the plot
plt.show()