
import matplotlib.pyplot as plt

# Data
sports = ['Football', 'Basketball', 'Tennis', 'Swimming', 'Running', 'Cycling', 'Boxing']
percentages = [25, 15, 10, 20, 15, 5, 10]
colors = ['#ff6666', '#66b2ff', '#99cc66', '#ffcc66', '#c266ff', '#ff66b2', '#66ff66']

# Pie chart
plt.figure(figsize=(10, 7))  # Change width and height of the chart
plt.pie(percentages, labels=sports, colors=colors, autopct='%1.1f%%', startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Title
plt.title('Popular Sports Distribution', pad=20)

# Display the chart
plt.show()