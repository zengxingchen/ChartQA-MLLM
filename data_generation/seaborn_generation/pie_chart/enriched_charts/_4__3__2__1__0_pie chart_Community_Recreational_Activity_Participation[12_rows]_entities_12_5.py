
import matplotlib.pyplot as plt

# Data points
food_categories = ['Fruits', 'Vegetables', 'Meat', 'Dairy', 'Grains', 'Sweets', 'Beverages']
market_share = [25.0, 20.0, 15.0, 10.0, 15.0, 10.0, 5.0]

# Colors using hexadecimal color codes
colors = ['#ff9999', '#66c2ff', '#99ff99', '#ffcc99', '#ffcc66', '#ff66b2', '#c2c2ff']

# Plotting the pie chart
plt.figure(figsize=(10, 6))  # Width and height of the chart
plt.pie(market_share, labels=food_categories, colors=colors, autopct='%1.1f%%', startangle=140)

# Title of the chart
plt.title('Distribution of Food Categories in a Balanced Diet', pad=20)

# Display the chart
plt.show()