
import matplotlib.pyplot as plt

# Data points
products = ['Skincare', 'Makeup', 'Haircare', 'Fragrances', 'Nail Products', 'Accessories', 'Others']
market_share = [25.4, 20.7, 15.3, 12.5, 10.2, 8.1, 7.8]

# Colors using hexadecimal color codes
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f']

# Plotting the pie chart
plt.figure(figsize=(10, 7))  # Width and height of the chart
plt.pie(market_share, labels=products, colors=colors, autopct='%1.1f%%', startangle=140)

# Title of the chart
plt.title('Market Share of Different Fashion & Beauty Products in 2023', pad=20)

# Display the chart
plt.show()