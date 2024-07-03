
import matplotlib.pyplot as plt

# Data points
food_types = [
    'Vegetables', 'Fruits', 'Proteins', 'Grains', 'Dairy'
]

percentages = [
    30.0, 20.0, 25.0, 15.0, 10.0
]

# Colors for each section
colors = [
    '#76b041', '#ffa500', '#ff6347', '#f4a460', '#add8e6'
]

# Resize the chart
plt.figure(figsize=(10, 7))

# Create the pie chart
plt.pie(percentages, labels=food_types, colors=colors, autopct='%1.1f%%', startangle=140)

# Set the title
plt.title('Distribution of Different Food Types in a Balanced Diet')

# Display the chart
plt.show()