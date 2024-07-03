
import matplotlib.pyplot as plt
import numpy as np

countries = [
    "United States", "United Kingdom", "Germany", "France", "China", "India",
    "Japan", "Brazil", "Russia", "Canada", "Australia", "South Korea",
    "Italy", "Spain", "Mexico", "South Africa", "Argentina", "Saudi Arabia",
    "Netherlands", "Sweden"
]
continents = [
    "North America", "Europe", "Europe", "Europe", "Asia", "Asia", "Asia",
    "South America", "Europe", "North America", "Oceania", "Asia",
    "Europe", "Europe", "North America", "Africa", "South America", "Asia",
    "Europe", "Europe"
]
number_of_universities = [
    3982, 1334, 1077, 736, 2922, 642, 779, 1015, 950, 317, 141, 366, 484,
    487, 382, 192, 126, 35, 246, 151
] # number of universities
education_spending = [
    6.1, 5.5, 4.9, 5.4, 4.0, 3.1, 3.5, 5.2, 3.8, 6.0, 5.8, 5.0, 4.1, 4.2,
    4.9, 5.4, 6.0, 6.4, 5.8, 7.0
] # education spending as percentage of GDP
gdp_per_capita = [
    65112, 42980, 47459, 40493, 10403, 2190, 40715, 8919, 11289, 46233,
    55194, 31346, 35451, 31571, 9831, 6441, 9955, 23208, 53083, 54915
] # GDP per capita in USD

# Assigning a color to each continent
continent_colors = {
    "Asia": "#4e79a7",
    "Europe": "#f28e2c",
    "Africa": "#e15759",
    "North America": "#76b7b2",
    "South America": "#59a14f",
    "Oceania": "#edc949"
}

colors = [continent_colors[continent] for continent in continents]

# Size corresponds to the education spending index
sizes = [spending * 50 for spending in education_spending]

# Create the plot
plt.figure(figsize=(18, 12))

for i in range(len(countries)):
    plt.scatter(gdp_per_capita[i], number_of_universities[i], s=sizes[i], c=colors[i], alpha=0.6, edgecolors="w", linewidth=2)

# Customizations
plt.title('Number of Universities, GDP per Capita, and Education Spending')
plt.xlabel('GDP per Capita (USD)')
plt.ylabel('Number of Universities')
plt.grid(True)

# Add a legend for continents
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=continent_colors[key], label=key) for key in continent_colors]
plt.legend(handles=legend_elements, title="Continents", loc='upper left')

plt.show()