
import matplotlib.pyplot as plt

# Data
categories = ['Fruits', 'Vegetables', 'Grains', 'Proteins', 'Dairy', 'Sweets', 'Beverages']
percentages = [30, 20, 15, 10, 10, 5, 10]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c2f0c2']

# Pie chart
plt.figure(figsize=(12, 8))  # Change width and height of the chart
plt.pie(percentages, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Title
plt.title('Dietary Composition Distribution', pad=30)

# Display the chart
plt.show()