
import matplotlib.pyplot as plt
import pandas as pd

# Data points
dates = pd.date_range(start="2024-01-01", end="2024-01-31")
stock_prices = [430, 420, 410, 400, 390, 380, 370, 360, 350, 340, 330, 320, 310, 300, 290, 280, 270, 260, 250, 240, 230, 220, 210, 200, 190, 180, 170, 160, 150, 140, 130]

# Create the plot
plt.figure(figsize=(14, 7))
plt.plot(dates, stock_prices, marker='s', linestyle='-', color='#1E90FF')

# Annotate the highest and lowest stock prices points
plt.annotate('Highest\n430 USD', xy=(dates[0], 430), xytext=(dates[5], 450),
             arrowprops=dict(facecolor='#FF1493', shrink=0.05), color='#FF1493')
plt.annotate('Lowest\n130 USD', xy=(dates[-1], 130), xytext=(dates[-5], 150),
             arrowprops=dict(facecolor='#FF1493', shrink=0.05), color='#FF1493')

# Title and labels
plt.title('Stock Prices in January 2024')
plt.xlabel('Date')
plt.ylabel('Stock Prices (USD)')
plt.gca().invert_yaxis()

# Customize the grid
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Show the plot
plt.show()