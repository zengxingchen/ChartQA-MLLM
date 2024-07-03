
import matplotlib.pyplot as plt

# Data points
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia',
          'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville']
average_income = [55000, 50000, 48000, 45000, 44000, 43000, 40000, 58000, 47000, 90000, 50000, 45000]
average_house_price = [650000, 570000, 225000, 200000, 210000, 180000, 175000, 630000, 245000, 1050000, 350000, 170000]
population = [8419000, 3980000, 2706000, 2300000, 1660000, 1585000,
              1500000, 1420000, 1340000, 1020000, 978000, 911000]

# Bubble size is scaled by population (This is a simplification; typically, you would want to scale these values appropriately)
bubble_size = [pop / 1000 for pop in population]

# Set the figure size
plt.figure(figsize=(14, 8))

# Create the scatter plot
plt.scatter(average_income, average_house_price, s=bubble_size,
            color=['#FF5733', '#33FF57', '#3357FF', '#FFFF33', '#FF33FF', '#33FFFF', '#5733FF', '#57FF33', '#F3FF33', '#33FFF3', '#FF3357', '#33FF3F'],
            alpha=0.7, edgecolors='w', linewidth=2)

# Title and labels
plt.title('Housing Prices vs. Income in U.S. Cities')
plt.xlabel('Average Income')
plt.ylabel('Average House Price')

# Add city labels to the bubbles
for i, city in enumerate(cities):
    plt.text(average_income[i], average_house_price[i], city, ha='center', va='center')

# Show plot
plt.show()