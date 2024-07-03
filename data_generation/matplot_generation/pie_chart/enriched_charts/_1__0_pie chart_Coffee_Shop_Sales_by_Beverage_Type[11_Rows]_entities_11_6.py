
import matplotlib.pyplot as plt

# Data
food_types = ['Fruits', 'Vegetables', 'Proteins', 'Grains', 'Dairy', 'Sweets']
percentages = [25, 30, 20, 15, 5, 5]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Pie chart
plt.figure(figsize=(10, 8))  # Change width and height of the chart
plt.pie(percentages, labels=food_types, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Title
plt.title('Daily Food Consumption Distribution', pad=20)

# Display the chart
plt.show()