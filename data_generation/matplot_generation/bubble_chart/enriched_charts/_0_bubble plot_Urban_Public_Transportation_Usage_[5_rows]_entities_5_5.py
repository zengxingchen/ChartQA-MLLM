
import matplotlib.pyplot as plt
import numpy as np

# Data for countries: emissions (million tonnes), GDP (billion USD), and population (million)
countries = ['United States', 'China', 'India', 'Russia', 'Japan', 'Germany', 
             'Canada', 'Brazil', 'Australia', 'France']
emissions = np.array([5000, 10000, 2400, 1600, 1200, 700, 650, 500, 400, 350])
gdp = np.array([21429, 14342, 2875, 1689, 5082, 3846, 1736, 1839, 1390, 2715])
population = np.array([331, 1402, 1380, 146, 126, 83, 38, 213, 26, 65])

# Bubble sizes, scaled to population
sizes = population * 10

# Color codes for each country
colors = ['#FF5733', '#33FF57', '#3357FF', '#57FFF3', '#F3FF57', '#FF33FA', 
          '#8D33FF', '#FF8E33', '#71FF33', '#3375FF']

plt.figure(figsize=(14, 8))

# Create the bubble chart
scatter = plt.scatter(gdp, emissions, s=sizes, c=colors, alpha=0.6, edgecolors="w", linewidth=2)

# Add titles and labels
plt.title('Annual Carbon Dioxide Emissions vs GDP by Country')
plt.xlabel('GDP (in billions USD)')
plt.ylabel('CO2 Emissions (in million tonnes)')

# Add annotations for country names
for i, country in enumerate(countries):
    plt.annotate(country, (gdp[i], emissions[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.show()