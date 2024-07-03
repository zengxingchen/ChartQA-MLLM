
import matplotlib.pyplot as plt
import pandas as pd

# Data points
dates = ["2024-01-01", "2024-02-01", "2024-03-01", "2024-04-01", "2024-05-01", "2024-06-01",
         "2024-07-01", "2024-08-01", "2024-09-01", "2024-10-01", "2024-11-01", "2024-12-01"]
stock_prices = [50, 55, 60, 58, 62, 65, 70, 67, 72, 75, 78, 80]

# Creating the line chart
plt.figure(figsize=(14, 10))

plt.plot(dates, stock_prices, color="#FF6347", marker='o')

# Annotating the highest and lowest stock prices
plt.annotate('Highest\n80$', xy=("2024-12-01", 80), xytext=("2024-12-01", 82),
             arrowprops=dict(facecolor='#FFD700', shrink=0.05), ha='center')
plt.annotate('Lowest\n50$', xy=("2024-01-01", 50), xytext=("2024-01-01", 48),
             arrowprops=dict(facecolor='#ADFF2F', shrink=0.05), ha='center')

# Title and labels
plt.title("Monthly Stock Prices in 2024", fontsize=20, pad=30)
plt.xlabel("Date", fontsize=16)
plt.ylabel("Stock Price ($)", fontsize=16)

# Customizing the grid and y-axis inversion
plt.grid(True, which='major', linestyle='--', linewidth=0.8, color='grey')
plt.gca().invert_yaxis()

# Show the plot
plt.show()