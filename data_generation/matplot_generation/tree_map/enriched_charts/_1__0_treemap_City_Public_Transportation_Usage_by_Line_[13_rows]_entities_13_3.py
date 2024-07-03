
import matplotlib.pyplot as plt
import squarify

# Data for the treemap
labels = ['Running', 'Cycling', 'Swimming', 'Weightlifting', 'Yoga', 'Boxing', 'Tennis', 'Hiking', 'Basketball', 'Soccer', 'Rowing']
sizes = [20, 15, 10, 8, 7, 6, 4, 3, 2, 2, 2]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f', '#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Create a figure of specified width and height
plt.figure(figsize=(12, 10))

# Create a treemap with specified data, labels, and color
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8)

# Set the title of the chart
plt.title('Popular Fitness Activities Distribution', fontsize=18)

# Remove the axis
plt.axis('off')

# Display the treemap
plt.show()