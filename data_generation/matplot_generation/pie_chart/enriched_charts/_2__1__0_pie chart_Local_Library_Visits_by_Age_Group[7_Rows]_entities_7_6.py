
import matplotlib.pyplot as plt

# Data to plot
labels = ['Reading', 'Writing', 'Painting', 'Sculpting', 'Photography', 'Calligraphy', 'Pottery', 'Origami']
sizes = [25, 20, 15, 10, 12, 8, 5, 5]
colors = ['#FF5733', '#33FF57', '#3357FF', '#F333FF', '#FF33A8', '#33FFA8', '#FF8C33', '#A833FF']

# Create pie chart
plt.figure(figsize=(12, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Title
plt.title('Popular Artistic Activities', y=1.05)

# Display the chart
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()