
import matplotlib.pyplot as plt

# Data
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
stock_price = [100, 102, 101, 103, 105, 107, 110, 108, 112, 115, 117, 116, 119, 118, 120, 123, 121, 125, 127, 130]
trading_volume = [1500, 1600, 1580, 1620, 1700, 1750, 1800, 1780, 1850, 1900, 1950, 1920, 1980, 1940, 2000, 2050, 2020, 2100, 2150, 2200]

# Scatter plot
plt.figure(figsize=(12, 6))  # Width:12, Height:6
plt.scatter(days, stock_price, color='#1E90FF', label='Stock Price')  # Dodger Blue
plt.scatter(days, trading_volume, color='#FF4500', label='Trading Volume')  # Orange Red

# Customize the plot
plt.title('Daily Stock Prices and Trading Volumes of XYZ Corporation Over 20 Days', pad=20)
plt.xlabel('Day')
plt.ylabel('Values')
plt.legend(loc='upper left')
plt.grid(True)

# Show the plot
plt.show()