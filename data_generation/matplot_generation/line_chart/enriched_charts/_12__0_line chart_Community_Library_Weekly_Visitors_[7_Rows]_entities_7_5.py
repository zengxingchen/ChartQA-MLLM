
import matplotlib.pyplot as plt

# Define the data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
stock_prices = [150, 155, 160, 158, 162, 165, 170, 167, 175, 178, 180, 185]

# Create the line chart
plt.figure(figsize=(12, 6)) # Changed width and height of the chart
plt.plot(months, stock_prices, color='#3498DB', marker='o') # Changed color scheme and added markers

# Customize the trend of the data by simulating a sudden drop in August
stock_prices[7] = 160
plt.plot(months, stock_prices, linestyle='--', color='#E74C3C') # Overlaying the modified trend line

# Assign annotation to the chart
for i, price in enumerate(stock_prices):
    plt.annotate(f"${price}", (months[i], stock_prices[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Axes and title
plt.title('Monthly Average Stock Prices of Company XYZ (Sudden Drop in August)', pad=20)
plt.xlabel('Month')
plt.ylabel('Average Stock Price (USD)')
plt.grid(True)

# Display the plot
plt.show()