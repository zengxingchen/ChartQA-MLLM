
import matplotlib.pyplot as plt

cities = ['New York', 'Tokyo', 'Bangkok', 'Sydney', 'Dubai', 'Singapore', 'Hong Kong', 'Los Angeles', 'Barcelona', 'Istanbul', 'Amsterdam', 'Berlin', 'Cape Town', 'Toronto', 'Rio de Janeiro', 'Moscow', 'Chicago', 'Miami', 'Mexico City', 'Shanghai']
population = [8419000, 13929000, 10539000, 5312000, 3331400, 5607300, 7409800, 3980400, 5585550, 15519267, 821752, 3644826, 433688, 2930000, 6748000, 12506468, 2675000, 467963, 9209944, 24237800]
gdp_per_capita = [70000, 62000, 22000, 65000, 45000, 62000, 45000, 67000, 40000, 15000, 52000, 55000, 20000, 55000, 15000, 32000, 60000, 50000, 10000, 20000]
number_of_museums = [100, 150, 80, 90, 50, 70, 40, 110, 70, 60, 30, 50, 40, 85, 55, 65, 75, 60, 50, 45]

size_factor = 5
sizes = [m * size_factor for m in number_of_museums]

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c2f0c2', '#ffb366', '#c2c2f0', '#ff6666', '#99ff99', '#66b3ff', '#ff9999', '#ffcc99', '#ffb3e6', '#ff6666', '#99ff99', '#66b3ff', '#ff9999', '#ffcc99']

plt.figure(figsize=(16,12))
plt.scatter(population, gdp_per_capita, s=sizes, c=colors, alpha=0.6, edgecolors='w', linewidth=0.5)

plt.title('Number of Museums vs. GDP per Capita with Population Bubble Sizes', pad=20)
plt.xlabel('Population')
plt.ylabel('GDP per Capita (USD)')

for i, city in enumerate(cities):
    plt.text(population[i], gdp_per_capita[i], city, ha='center', va='center', fontsize=8)

plt.tight_layout()
plt.show()