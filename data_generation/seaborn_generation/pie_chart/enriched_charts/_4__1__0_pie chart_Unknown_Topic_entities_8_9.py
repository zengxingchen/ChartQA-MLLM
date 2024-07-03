
import matplotlib.pyplot as plt

# Data points
food_category = ['Fruits', 'Vegetables', 'Dairy Products', 'Meat', 'Grains', 'Sweets', 'Beverages']
market_share = [20.0, 15.0, 18.0, 22.0, 10.0, 8.0, 7.0]
colors = ['#ff6666', '#ffcc99', '#99ff99', '#ff9966', '#c2c2f0', '#ffb3e6', '#c4e17f']

# Create a pie chart
plt.figure(figsize=(14, 10))  # Modify the width and height of the chart
plt.pie(market_share, labels=food_category, colors=colors, autopct='%1.1f%%', startangle=140)

# Chart title
plt.title('Market Share of Popular Food Categories in 2023', pad=20)

# Display the chart
plt.show()