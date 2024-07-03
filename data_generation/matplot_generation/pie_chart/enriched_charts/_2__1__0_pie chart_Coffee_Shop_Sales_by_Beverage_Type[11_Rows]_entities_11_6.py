
import matplotlib.pyplot as plt

# Data
destinations = ['Beach', 'Mountains', 'City', 'Countryside', 'Desert', 'Forest']
percentages = [35, 25, 20, 10, 5, 5]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Pie chart
plt.figure(figsize=(12, 9))  # Change width and height of the chart
plt.pie(percentages, labels=destinations, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Title
plt.title('Preferred Travel Destinations', pad=30)

# Display the chart
plt.show()