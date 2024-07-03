
import matplotlib.pyplot as plt

# Data
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 
           'Saturn', 'Uranus', 'Neptune', 'Pluto', 'Haumea', 
           'Makemake', 'Eris', 'Ceres', 'Sedna', 'Quaoar']
distance_from_sun = [57.9, 108.2, 149.6, 227.9, 778.3, 
                     1427, 2871, 4497.1, 5906.4, 6450, 
                     6879, 10190, 413.7, 13320, 6554]  # in million km
diameter = [4879, 12104, 12742, 6779, 139820, 
            116460, 50724, 49244, 2376, 2322, 
            1434, 2326, 939, 995, 1110]  # in km
moons = [0, 0, 1, 2, 79, 83, 27, 14, 5, 2, 1, 1, 0, 0, 1]  # count

# Color for each planet
colors = ['#ff5733', '#33ff57', '#3357ff', '#ff33a1', '#33a1ff', 
          '#a1ff33', '#ff8333', '#8333ff', '#ff33f6', '#33f6ff', 
          '#f63333', '#f6a133', '#33f6a1', '#a133f6', '#f6a1f6']

# Using diameter as the size of the bubble
sizes = [d / max(diameter) * 2000 for d in diameter]

# Set up the figure size
plt.figure(figsize=(16, 12))

# Scatter plot
plt.scatter(distance_from_sun, moons, s=sizes, c=colors, alpha=0.6)

# Labels and Title
plt.title('Bubble Chart of Distances, Diameters, and Moons of Planets in the Solar System', fontsize=16)
plt.xlabel('Distance from Sun (million km)', fontsize=14)
plt.ylabel('Number of Moons', fontsize=14)

# Add planet names to the bubbles
for i, planet in enumerate(planets):
    plt.annotate(planet, (distance_from_sun[i], moons[i]), fontsize=10)

# Show grid
plt.grid(True)

# Show the plot
plt.show()