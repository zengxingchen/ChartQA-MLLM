
import matplotlib.pyplot as plt

# Data
fruits = ['Apple', 'Banana', 'Orange', 'Grapes', 'Strawberry', 'Pineapple']
percentages = [30, 25, 20, 10, 10, 5]
colors = ['#ff9999', '#ffcc99', '#66b3ff', '#99ff99', '#c2c2f0', '#ffb3e6']

# Pie chart
plt.figure(figsize=(10, 7))  # Change width and height of the chart
plt.pie(percentages, labels=fruits, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Title
plt.title('Popular Fruit Consumption', pad=30)

# Display the chart
plt.show()