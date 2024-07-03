
import matplotlib.pyplot as plt

# Data points
categories = ['Soccer', 'Basketball', 'Tennis', 'Swimming', 'Running', 'Cycling', 'Others']
percentages = [20.0, 15.0, 10.0, 8.0, 12.0, 18.0, 17.0]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f']

# Create a pie chart
plt.figure(figsize=(12, 9))  # Modify the width and height of the chart
plt.pie(percentages, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)

# Chart title
plt.title('Distribution of Popular Sports in 2023', pad=20)

# Display the chart
plt.show()