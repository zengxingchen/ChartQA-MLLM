
import matplotlib.pyplot as plt
import numpy as np

# Data for countries: stock market returns (%), GDP growth rate (%), and population (million)
countries = [
    'United States', 'China', 'India', 'Germany', 'Japan', 'United Kingdom', 
    'Canada', 'Brazil', 'Australia', 'France', 'Russia', 'South Korea', 
    'Mexico', 'Italy', 'Spain'
]
stock_returns = np.array([7.2, 9.5, 11.8, 5.6, 4.1, 6.3, 6.8, 8.1, 6.0, 5.2, 8.7, 7.4, 7.0, 4.8, 5.4])
gdp_growth = np.array([2.3, 6.1, 7.3, 1.5, 0.7, 1.8, 1.9, 2.2, 2.0, 1.3, 1.4, 2.2, 2.1, 1.0, 1.4])
population = np.array([331, 1402, 1380, 83, 126, 67, 38, 213, 26, 65, 146, 52, 129, 60, 47])

# Bubble sizes, scaled to population
sizes = population * 10

# New color codes for each country for better visual clarity
colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', 
    '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#aec7e8', '#ffbb78', 
    '#98df8a', '#ff9896', '#c5b0d5'
]

plt.figure(figsize=(16, 9))

# Create the bubble chart
scatter = plt.scatter(gdp_growth, stock_returns, s=sizes, c=colors, alpha=0.6, edgecolors="w", linewidth=2)

# Add titles and labels
plt.title('Annual Stock Market Returns vs GDP Growth Rate by Country', pad=20)
plt.xlabel('GDP Growth Rate (%)')
plt.ylabel('Stock Market Returns (%)')

# Add annotations for country names
for i, country in enumerate(countries):
    plt.annotate(country, (gdp_growth[i], stock_returns[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.show()