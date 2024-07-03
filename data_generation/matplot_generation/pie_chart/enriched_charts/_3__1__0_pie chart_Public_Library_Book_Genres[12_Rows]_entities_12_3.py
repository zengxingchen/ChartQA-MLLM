
import matplotlib.pyplot as plt

# Data for the chart
fruits = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grape']
percentages = [20, 15, 10, 12, 8, 25, 10]
colors = ['#FF0000', '#FFFF00', '#8B0000', '#FFD700', '#4B0082', '#8FBC8F', '#800080']

# Create a pie chart
plt.figure(figsize=(8, 8))  # Set the width and height of the chart
plt.pie(percentages, labels=fruits, autopct='%1.1f%%', colors=colors, startangle=140)

plt.title('Distribution of Favorite Fruits in 2023', y=1.08)  # Change the headline to match the topic and adjust the position
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the chart
plt.show()