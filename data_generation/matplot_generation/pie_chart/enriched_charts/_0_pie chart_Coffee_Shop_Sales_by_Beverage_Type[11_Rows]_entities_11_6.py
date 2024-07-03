
import matplotlib.pyplot as plt

# Data
transport_modes = ['Bicycling', 'Public Transit', 'Driving', 'Walking', 'Motorcycle', 'Car Sharing', 'Electric Scooters']
percentages = [5, 20, 50, 10, 3, 7, 5]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6', '#c4e17f']

# Pie chart
plt.figure(figsize=(8, 6))  # Change width and height of the chart
plt.pie(percentages, labels=transport_modes, colors=colors, autopct='%1.1f%%', startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Title
plt.title('City Transportation Modes Distribution')

# Display the chart
plt.show()