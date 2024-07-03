
import matplotlib.pyplot as plt

# Data for scatterplot
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
distance = [0.39, 0.72, 1.00, 1.52, 5.20, 9.58, 19.22, 30.05, 39.48]
brightness = [4.8, -4.6, -3.99, -2.0, -1.6, 0.46, 5.52, 7.78, 13.65]
size = [0.382, 0.949, 1.000, 0.532, 11.209, 9.449, 4.007, 3.883, 0.186]

# Size of each point will be proportional to the relative size of the planet
sizes = [s * 100 for s in size]

# Different colors for different categories
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF', '#33A6FF', '#FF33FF', '#57FF33', '#5733FF']

# Create scatterplot
plt.figure(figsize=(16, 12))  # increase the width and height of the chart
plt.scatter(planets, distance, s=sizes, c=colors, alpha=0.7)

# Chart details
plt.title('Relative Distance, Brightness, and Size of Planets in the Solar System')
plt.xlabel('Planet')
plt.ylabel('Distance (Light Years)')
plt.grid(True)

# Show the chart
plt.show()