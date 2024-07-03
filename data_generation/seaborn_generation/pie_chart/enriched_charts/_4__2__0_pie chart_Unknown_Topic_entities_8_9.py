
import matplotlib.pyplot as plt

# Data points
categories = ['Fruits', 'Vegetables', 'Grains', 'Meat', 'Dairy', 'Sweets', 'Others']
market_share = [25.1, 20.2, 18.3, 15.6, 12.8, 5.6, 2.4]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6','#c4e17f']

# Create a pie chart
plt.figure(figsize=(14, 12))
plt.pie(market_share, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)

# Chart title
plt.title('Market Share of Different Food Categories in 2023', pad=40)

# Display the chart
plt.show()