
import matplotlib.pyplot as plt

# Data for plotting
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
stock_price = [100, 102, 105, 103, 108, 107, 110, 115, 118, 120, 122, 121, 125, 127, 130, 132, 134, 133, 135, 137, 140, 142, 141, 145, 148, 150, 152, 155, 157, 160]
trade_volume = [2000, 2500, 2200, 2700, 3000, 2900, 3200, 3100, 3400, 3600, 3800, 3700, 4000, 3900, 4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900, 5000, 5100, 5200, 5300, 5400, 5500, 5600]

# Create a scatterplot
plt.figure(figsize=(16, 12))
plt.scatter(days, stock_price, c="#1E88E5", label="Stock Price")
plt.scatter(days, trade_volume, c="#D81B60", label="Trade Volume")

# Customize the chart
plt.title("Daily Stock Prices and Trading Volumes Over a Month")
plt.xlabel("Day of the Month")
plt.ylabel("Value")
plt.legend(loc='upper right')
plt.grid(True)

# Show the scatterplot
plt.show()