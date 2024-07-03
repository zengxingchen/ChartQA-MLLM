
import matplotlib.pyplot as plt

# Data to plot
labels = 'Drawing', 'Painting', 'Sculpting', 'Digital Art', 'Photography', 'Crafting', 'Graphic Design', 'Illustration', 'Art History Study'
sizes = [20, 18, 15, 12, 10, 8, 7, 5, 5]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#ff6666', '#ffb347']

# Plot
plt.figure(figsize=[10, 6])  # Set the width and height of the chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Distribution of Art Activities', pad=20)
plt.show()