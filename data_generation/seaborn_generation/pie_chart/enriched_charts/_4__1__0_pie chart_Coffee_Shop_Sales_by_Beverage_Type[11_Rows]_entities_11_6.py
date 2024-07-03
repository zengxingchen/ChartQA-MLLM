
import matplotlib.pyplot as plt

# Data
transport_modes = ['Car', 'Bicycle', 'Public Transport', 'Walking', 'Scooter', 'Motorbike', 'Other']
percentages = [40, 20, 15, 10, 5, 5, 5]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#f0e68c']

# Pie chart
plt.figure(figsize=(12, 10))  # Change width and height of the chart
plt.pie(percentages, labels=transport_modes, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Title
plt.title('Preferred Modes of Transportation for Daily Commute', pad=30)

# Display the chart
plt.show()