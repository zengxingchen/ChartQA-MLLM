
import matplotlib.pyplot as plt

# Data
countries = ['United States', 'China', 'Japan', 'Germany', 'India', 
             'United Kingdom', 'France', 'Brazil', 'Italy', 'Canada', 
             'Russia', 'South Korea', 'Spain', 'Australia', 'Mexico', 
             'Netherlands', 'Switzerland', 'Sweden', 'Singapore']
gdp = [21.4, 14.3, 5.1, 4.2, 2.9, 2.7, 2.6, 2.1, 2.0, 1.8, 1.7, 1.6, 1.4, 1.4, 1.3, 1.0, 0.8, 0.6, 0.5]  # Trillions USD
startup_density = [1.5, 0.3, 0.9, 1.1, 0.2, 1.3, 1.0, 0.4, 0.7, 1.2, 0.5, 1.1, 0.6, 1.0, 0.3, 1.4, 1.2, 1.3, 1.5]  # Startups per 1000 people
innovation_index = [85.7, 75.5, 78.6, 80.2, 60.1, 82.9, 79.0, 60.5, 70.0, 81.3, 65.8, 83.4, 71.2, 80.7, 58.9, 84.0, 87.6, 86.2, 89.4]  # Innovation Index Score

# Color for each country
colors = ['#ff6f61', '#6a0dad', '#ffdd57', '#ff7f50', '#4682b4', 
          '#d2691e', '#6495ed', '#dda0dd', '#9acd32', '#ee82ee', 
          '#40e0d0', '#ff4500', '#32cd32', '#ff69b4', '#8a2be2',
          '#ff1493', '#00ced1', '#ffd700', '#00fa9a']

# Using GDP as the size of the bubble
sizes = [g / max(gdp) * 2000 for g in gdp]

# Set up the figure size
plt.figure(figsize=(18, 10))

# Scatter plot
plt.scatter(innovation_index, startup_density, s=sizes, c=colors, alpha=0.7)

# Labels and Title
plt.title('GDP vs Startup Density and Innovation Index', fontsize=18, pad=20)
plt.xlabel('Innovation Index Score', fontsize=14)
plt.ylabel('Startup Density (Startups per 1000 people)', fontsize=14)

# Add country names to the bubbles
for i, country in enumerate(countries):
    plt.annotate(country, (innovation_index[i], startup_density[i]), fontsize=10, ha='center')

# Show grid
plt.grid(True)

# Show the plot
plt.show()