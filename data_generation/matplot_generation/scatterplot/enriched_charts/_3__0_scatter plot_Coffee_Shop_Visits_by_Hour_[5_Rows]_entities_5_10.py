
import matplotlib.pyplot as plt

# Data for scatterplot
cities = ["Bangkok", "London", "Paris", "Dubai", "New York", 
          "Singapore", "Kuala Lumpur", "Istanbul", "Tokyo", 
          "Barcelona", "Sydney", "Rome", "Los Angeles", "Amsterdam",
          "Shanghai", "Rio de Janeiro", "Cairo", "Cape Town", 
          "Auckland", "Moscow"]
rainfall = [1500, 600, 650, 100, 1200, 2200, 2500, 800, 1600, 650, 
            1200, 750, 400, 850, 1100, 2000, 20, 600, 1200, 700]
bird_species = [200, 150, 130, 75, 180, 250, 300, 140, 190, 125, 
                210, 160, 100, 140, 170, 280, 60, 150, 220, 130]

# Create scatterplot
plt.figure(figsize=(12, 8))
plt.scatter(rainfall, bird_species, c=[
    '#FF6347','#4682B4','#8A2BE2','#5F9EA0','#D2691E',
    '#FF7F50','#6495ED','#DC143C','#00FFFF','#008B8B',
    '#B8860B','#A9A9A9','#006400','#BDB76B','#8B008B',
    '#556B2F','#FF8C00','#9932CC','#8B0000','#E9967A'], s=100)

# Customize plot
plt.title('Correlation between Average Annual Rainfall and Number of Bird Species in Different Cities', fontsize=16)
plt.xlabel('Average Annual Rainfall (mm)', fontsize=12)
plt.ylabel('Number of Bird Species (count)', fontsize=12)

# Annotate data points
for i, city in enumerate(cities):
    plt.annotate(city, (rainfall[i], bird_species[i]), 
                 textcoords="offset points", xytext=(0,10), ha='center')

# Show plot
plt.show()