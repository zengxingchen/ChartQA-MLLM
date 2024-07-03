
import matplotlib.pyplot as plt

# Data
food_items = ['Vegetables', 'Fruits', 'Grains', 'Proteins', 'Dairy', 'Fats', 'Sugars', 'Beverages']
market_share = [25, 20, 18, 15, 10, 7, 3, 2]
colors = ['#4CAF50', '#FFEB3B', '#FFC107', '#FF5722', '#3F51B5', '#795548', '#9C27B0', '#009688']

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(12, 8))  # Change width and height
ax.pie(market_share, labels=food_items, autopct='%1.1f%%', startangle=90, colors=colors)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Setting the title
plt.title("Food Group Distribution in a Balanced Diet - 2023", pad=20)

# Display the chart
plt.show()