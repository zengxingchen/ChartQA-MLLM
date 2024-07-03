
import matplotlib.pyplot as plt

# Data
countries = ['United States', 'China', 'Japan', 'Germany', 'India', 
             'United Kingdom', 'France', 'Brazil', 'Italy', 'Canada', 
             'Russia', 'South Korea', 'Spain', 'Australia', 'Mexico']
gdp = [21433, 14343, 5081, 3846, 2875, 2829, 2716, 1847, 2001, 1736, 
       1699, 1641, 1430, 1393, 1263]  # in billions
population = [331, 1439, 126, 83, 1380, 67, 65, 213, 60, 38, 146, 52, 
              47, 25, 129]  # in millions
life_expectancy = [78.9, 76.7, 84.6, 81.2, 69.7, 81.2, 82.7, 75.9, 
                   83.4, 82.3, 72.7, 83.3, 83.4, 83.1, 75.1]  # in years

# Color for each country
colors = ['#d32f2f', '#1976d2', '#388e3c', '#f57c00', '#c2185b', 
          '#7b1fa2', '#00796b', '#fbc02d', '#6a1b9a', '#cddc39', 
          '#0097a7', '#e64a19', '#ffeb3b', '#7c4dff', '#4caf50']

# Using GDP as the size of the bubble
sizes = [g / max(gdp) * 2000 for g in gdp]

# Set up the figure size
plt.figure(figsize=(14, 10))

# Scatter plot
plt.scatter(population, life_expectancy, s=sizes, c=colors, alpha=0.6)

# Labels and Title
plt.title('Bubble Chart of GDP, Population, and Life Expectancy of Various Countries', fontsize=16)
plt.xlabel('Population (millions)', fontsize=14)
plt.ylabel('Life Expectancy (years)', fontsize=14)

# Add country names to the bubbles
for i, country in enumerate(countries):
    plt.annotate(country, (population[i], life_expectancy[i]), fontsize=10)

# Show grid
plt.grid(True)

# Show the plot
plt.show()