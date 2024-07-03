
import matplotlib.pyplot as plt

# Data to plot
labels = ['Stars', 'Planets', 'Galaxies', 'Nebulae', 'Black Holes', 'Asteroids', 'Comets', 'Exoplanets']
sizes = [30, 20, 15, 10, 8, 7, 5, 5]
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#955251', '#B565A7', '#009B77']

# Create pie chart
plt.figure(figsize=(10, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Title
plt.title('Popular Topics in Astronomy & Space Exploration', y=1.08)

# Display the chart
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()