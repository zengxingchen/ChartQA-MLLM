
import matplotlib.pyplot as plt

# Data points
food_categories = ['Fruits', 'Vegetables', 'Grains', 'Protein Foods', 'Dairy', 'Sweets', 'Others']
market_share = [25.0, 20.0, 15.0, 15.0, 10.0, 8.0, 7.0]

# Colors using hexadecimal color codes
colors = ['#FFA07A', '#98FB98', '#FFD700', '#87CEFA', '#FF69B4', '#DDA0DD', '#D3D3D3']

# Plotting the pie chart
plt.figure(figsize=(10, 6))  # Width and height of the chart
plt.pie(market_share, labels=food_categories, colors=colors, autopct='%1.1f%%', startangle=140)

# Title of the chart
plt.title('Market Share of Different Food Categories in 2023', pad=20)

# Display the chart
plt.show()