
import matplotlib.pyplot as plt

# Data points
cryptocurrencies = ['Bitcoin', 'Ethereum', 'Tether', 'BNB', 'USD Coin', 'XRP', 'Others']
market_share = [42.3, 18.1, 7.2, 3.8, 3.7, 2.1, 22.8]

# Colors using hexadecimal color codes
colors = ['#ffcc00', '#3366cc', '#ff6600', '#009999', '#cc0000', '#9933cc', '#999999']

# Plotting the pie chart
plt.figure(figsize=(12, 8))  # Width and height of the chart
plt.pie(market_share, labels=cryptocurrencies, colors=colors, autopct='%1.1f%%', startangle=140)

# Title of the chart
plt.title('Market Share of Different Cryptocurrencies in 2023', pad=20)

# Display the chart
plt.show()