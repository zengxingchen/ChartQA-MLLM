
import matplotlib.pyplot as plt

# Define the data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
stock_prices = [185, 180, 178, 175, 167, 170, 165, 162, 160, 158, 155, 150]

# Create the line chart
plt.figure(figsize=(14, 7))  # Changed width and height of the chart
plt.plot(months, stock_prices, color='#2ECC71', marker='o')  # Changed color scheme and added markers

# Customize the trend of the data by simulating a sudden rise in May
stock_prices[4] = 180
plt.plot(months, stock_prices, linestyle='--', color='#E74C3C')  # Overlaying the modified trend line

# Assign annotation to the chart
for i, price in enumerate(stock_prices):
    plt.annotate(f"${price}", (months[i], stock_prices[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Axes and title
plt.title('Monthly Average Stock Prices of Company XYZ (Sudden Rise in May)', pad=20)
plt.xlabel('Month')
plt.ylabel('Average Stock Price (USD)')
plt.grid(True)
plt.gca().invert_yaxis()  # Invert y-axis

# Display the plot
plt.show()