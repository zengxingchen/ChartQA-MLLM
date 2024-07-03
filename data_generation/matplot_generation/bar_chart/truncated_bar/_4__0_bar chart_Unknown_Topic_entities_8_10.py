
import matplotlib.pyplot as plt

# Data
months = [
    'January', 'February', 'March', 'April', 'May', 'June', 
    'July', 'August', 'September', 'October', 'November', 'December'
]
stock_prices = [150, 160, 155, 170, 175, 165, 180, 185, 175, 190, 195, 200]

# Plotting the bar chart
plt.figure(figsize=(12, 6))  # changing width and height of the chart
plt.bar(months, stock_prices, width=0.6, color=[
    '#4B0082', '#FF4500', '#1E90FF', '#32CD32', 
    '#FFD700', '#FF6347', '#8A2BE2', '#00CED1', 
    '#DA70D6', '#FF1493', '#00FF00', '#FF00FF'
])  # change direction and color scheme of bars

# Customizing the plot
plt.ylabel('Stock Prices in USD')  # changing chart headline
plt.title('Monthly Stock Prices Data', pad=20)  # changing topic
plt.ylim(140, 210)  # adjust the limit to better spread out the bars

# Show the plot
plt.show()