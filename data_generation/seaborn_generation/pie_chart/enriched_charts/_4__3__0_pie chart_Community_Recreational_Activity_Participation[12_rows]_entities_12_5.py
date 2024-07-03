
import matplotlib.pyplot as plt

# Data points
categories = ['Fruits', 'Vegetables', 'Dairy', 'Grains', 'Proteins', 'Fats', 'Sugars']
percentages = [25.0, 20.0, 15.0, 18.0, 10.0, 7.0, 5.0]

# Colors using hexadecimal color codes
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f']

# Plotting the pie chart
plt.figure(figsize=(10, 6))  # Width and height of the chart
plt.pie(percentages, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)

# Title of the chart
plt.title('Nutritional Breakdown of a Balanced Diet', pad=20)

# Display the chart
plt.show()