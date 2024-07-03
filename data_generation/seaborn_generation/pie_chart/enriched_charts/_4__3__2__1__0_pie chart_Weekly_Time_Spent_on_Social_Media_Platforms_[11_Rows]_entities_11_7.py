
import matplotlib.pyplot as plt

# Data
categories = ['Vegetables', 'Fruits', 'Grains', 'Proteins', 'Dairy', 'Sweets', 'Beverages', 'Oils']
percentages = [30, 25, 15, 10, 8, 7, 5, 5]
colors = ['#ff9999', '#66b2ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#ffccff']

# Plotting the pie chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.pie(percentages, labels=categories, autopct='%1.1f%%', startangle=140, colors=colors)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Setting the title
plt.title("Distribution of Food Categories in 2022", pad=20)

# Display the chart
plt.show()