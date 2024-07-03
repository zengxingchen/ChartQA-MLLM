
import matplotlib.pyplot as plt

# Data for scatterplot
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
distance_au = [0.39, 0.72, 1, 1.52, 5.2, 9.58, 19.22, 30.05, 39.48]
orbital_period_days = [88, 225, 365, 687, 4333, 10759, 30685, 60190, 90560]
diameter_km = [4879, 12104, 12742, 6779, 139820, 116460, 50724, 49244, 2376]

# Size of each point will be proportional to the planet's diameter
sizes = [diameter / 200 for diameter in diameter_km]

# Custom color scheme
colors = ['#F9A602', '#FF69B4', '#00BFFF', '#FF4500', '#FFD700', '#DA70D6', '#9370DB', '#4682B4', '#8B0000']

# Create scatterplot
plt.figure(figsize=(16, 12))  # Increase the width and height of the chart
plt.scatter(planets, distance_au, s=sizes, c=colors, alpha=0.7)

# Chart details
plt.title('Orbital Characteristics of Planets in the Solar System')
plt.xlabel('Planet')
plt.ylabel('Distance from Sun (AU)')
plt.grid(True)

# Show the chart
plt.show()