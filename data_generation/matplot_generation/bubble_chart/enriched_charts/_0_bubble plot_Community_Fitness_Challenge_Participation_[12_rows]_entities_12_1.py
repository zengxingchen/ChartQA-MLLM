
import matplotlib.pyplot as plt
import numpy as np

# Define the data
countries = [
    "China", "India", "United States", "Indonesia", "Pakistan", "Brazil",
    "Nigeria", "Bangladesh", "Russia", "Mexico", "Japan", "Ethiopia",
    "Philippines", "Egypt", "Vietnam", "DR Congo", "Turkey", "Iran",
    "Germany", "Thailand"
]
continents = [
    "Asia", "Asia", "North America", "Asia", "Asia", "South America",
    "Africa", "Asia", "Europe", "North America", "Asia", "Africa",
    "Asia", "Africa", "Asia", "Africa", "Europe", "Asia", "Europe", "Asia"
]
population = [
    1393, 1351, 331, 273, 220, 212, 206, 163, 146, 128, 126, 114, 109, 102,
    97, 89, 84, 83, 83, 70
] # in millions
gdp = [
    14722.73, 2875.14, 21427.23, 1158.42, 302.14, 1839.76, 429.77, 317.47,
    1699.88, 1258.26, 5081.77, 96.11, 376.80, 303.18, 340.60, 49.25, 761.43,
    610.66, 3962.56, 543.65
] # in billions
happiness = [
    5.1, 4.2, 7.2, 5.3, 5.4, 6.4, 5.0, 4.5, 5.8, 6.5, 6.0, 4.3, 5.7, 4.7,
    5.5, 4.1, 5.4, 4.8, 7.0, 6.1
]

# Assigning a color to each continent
continent_colors = {
    "Asia": "#1f77b4",
    "Europe": "#ff7f0e",
    "Africa": "#2ca02c",
    "North America": "#d62728",
    "South America": "#9467bd"
}

colors = [continent_colors[continent] for continent in continents]

# Size corresponds to the happiness index
sizes = [happiness_index * 80 for happiness_index in happiness]

# Create the plot
plt.figure(figsize=(15, 10))

for i in range(len(countries)):
    plt.scatter(gdp[i], population[i], s=sizes[i], c=colors[i], alpha=0.6, edgecolors="w", linewidth=2)

# Customizations
plt.title('Population, GDP, and Happiness Index of Various Countries')
plt.xlabel('GDP in Billions (USD)')
plt.ylabel('Population in Millions')
plt.grid(True)

# Add a legend for continents
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=continent_colors[key], label=key) for key in continent_colors]
plt.legend(handles=legend_elements, title="Continents")

plt.show()