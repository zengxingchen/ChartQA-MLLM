
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
stock_prices = [150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 210]

# Creating the line chart
plt.figure(figsize=(16, 8))

plt.plot(months, stock_prices, color="#1E90FF", marker='o')  # Using a specific color code

# Annotating the highest and lowest stock prices
plt.annotate('Highest\n210 USD', xy=("December", 210), xytext=("December", 215),
             arrowprops=dict(facecolor='#FF6347', shrink=0.05), ha='center')
plt.annotate('Lowest\n150 USD', xy=("January", 150), xytext=("January", 145),
             arrowprops=dict(facecolor='#32CD32', shrink=0.05), ha='center')

# Title and labels
plt.title("Monthly Stock Prices in 2024", fontsize=18, pad=20)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Stock Price (USD)", fontsize=14)

# Customizing the grid
plt.grid(True, which='major', linestyle='--', linewidth=0.6, color='grey')

# Invert y-axis
plt.gca().invert_yaxis()

# Show the plot
plt.show()