
import matplotlib.pyplot as plt

# Data
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
coffee_shops = [317, 210, 119, 85, 78, 91, 59, 63, 78, 58]
cappuccino_price = [4.5, 4.3, 4.1, 3.9, 4.2, 4.4, 3.8, 4.6, 4.0, 4.7]
city_population = [8.4, 3.9, 2.7, 2.3, 1.6, 1.6, 1.5, 1.4, 1.3, 1.0]
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF66B2', '#FF3333', '#99CCFF', '#FF9966', '#99FF66', '#6699FF']

# Bubble chart
plt.figure(figsize=(14, 10))
for idx, city in enumerate(cities):
    plt.scatter(city_population[idx], coffee_shops[idx], s=cappuccino_price[idx]*50, c=colors[idx], label=city, alpha=0.6, edgecolors='w')

# Add titles and labels
plt.title('Coffee Shop Distribution and Cappuccino Price in US Cities', fontsize=18)
plt.xlabel('City Population (Millions)', fontsize=14)
plt.ylabel('Number of Coffee Shops', fontsize=14)

# Additional settings
plt.grid(True)
plt.legend(loc='upper left', title='Cities')
plt.xlim(0.5, 9)
plt.ylim(50, 350)

# Show plot
plt.tight_layout()
plt.show()