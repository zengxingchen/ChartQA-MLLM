
import matplotlib.pyplot as plt

# Data
cuisines = ['Italian', 'Chinese', 'Mexican', 'Japanese', 'Indian', 'French']
percentages = [30, 25, 20, 15, 5, 5]
colors = ['#ff6666', '#66b2ff', '#99ff99', '#ffcc66', '#c266ff', '#ff99cc']

# Pie chart
plt.figure(figsize=(10, 8))  # Change width and height of the chart
plt.pie(percentages, labels=cuisines, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Title
plt.title('Preferred Types of Cuisine', pad=20)

# Display the chart
plt.show()