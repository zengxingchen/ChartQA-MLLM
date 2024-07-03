
import matplotlib.pyplot as plt

# Data points
services = ['Netflix', 'Amazon Prime', 'Disney+', 'HBO Max', 'Hulu', 'Apple TV+', 'Others']
market_share = [32.3, 16.1, 14.2, 12.5, 8.4, 6.5, 10.0]

# Colors using hexadecimal color codes
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f']

# Plotting the pie chart
plt.figure(figsize=(12, 8))  # Width and height of the chart
plt.pie(market_share, labels=services, colors=colors, autopct='%1.1f%%', startangle=140)

# Title of the chart
plt.title('Streaming Services Market Share in 2023')

# Display the chart
plt.show()