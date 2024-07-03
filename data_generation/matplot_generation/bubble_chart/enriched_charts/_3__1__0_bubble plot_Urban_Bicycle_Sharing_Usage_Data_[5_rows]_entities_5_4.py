
import matplotlib.pyplot as plt

cities = ['Paris', 'London', 'Rome', 'New York', 'Tokyo', 'Bangkok', 'Sydney', 'Dubai', 'Singapore', 'Hong Kong', 'Los Angeles', 'Barcelona', 'Istanbul', 'Amsterdam', 'Berlin', 'Cape Town', 'Toronto', 'Rio de Janeiro', 'Moscow', 'Dubai']
population_density = [21300, 5600, 2200, 10800, 6400, 6200, 400, 900, 8300, 7000, 3200, 16000, 2800, 5000, 4000, 1500, 4400, 5300, 4900, 900]
avg_green_space = [10.1, 33.4, 12.7, 14.0, 7.5, 3.6, 46.0, 2.0, 47.0, 40.0, 14.0, 11.2, 1.2, 20.2, 30.0, 23.0, 12.5, 6.3, 30.7, 2.0]
quality_of_life_index = [176.2, 167.6, 151.1, 156.4, 172.3, 138.7, 190.4, 147.3, 178.1, 168.5, 170.1, 165.4, 127.3, 179.6, 182.7, 165.3, 180.1, 130.8, 155.2, 147.3]

size_factor = 50
sizes = [p * size_factor for p in quality_of_life_index]

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFD7', '#D733FF', '#FFC133', '#33FFA1', '#57FF33', '#FF3357', '#33D7FF', '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFD7', '#D733FF', '#FFC133', '#33FFA1', '#57FF33']

plt.figure(figsize=(18,14))
plt.scatter(population_density, avg_green_space, s=sizes, c=colors, alpha=0.6, edgecolors='w', linewidth=0.5)

plt.title('Population Density vs. Average Green Space with Quality of Life Index Bubble Sizes', pad=20)
plt.xlabel('Population Density (people/km²)')
plt.ylabel('Average Green Space (%)')

for i, city in enumerate(cities):
    plt.text(population_density[i], avg_green_space[i], city, ha='center', va='center', fontsize=8)

plt.tight_layout()
plt.show()