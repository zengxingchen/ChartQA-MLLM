
import matplotlib.pyplot as plt

# Your provided data
data = [
    {'Year': 2019, 'Espresso': 1250, 'Americano': 1750, 'Cappuccino': 2000, 'Latte': 2250, 'Mocha': 1500},
    {'Year': 2020, 'Espresso': 1300, 'Americano': 1800, 'Cappuccino': 1950, 'Latte': 2300, 'Mocha': 1550},
    {'Year': 2021, 'Espresso': 1350, 'Americano': 1850, 'Cappuccino': 1900, 'Latte': 2400, 'Mocha': 1600},
    {'Year': 2022, 'Espresso': 1400, 'Americano': 1900, 'Cappuccino': 1850, 'Latte': 2500, 'Mocha': 1650},
    {'Year': 2023, 'Espresso': 1450, 'Americano': 1950, 'Cappuccino': 1800, 'Latte': 2600, 'Mocha': 1700}
]

# Extract years and individual coffee sales
years = [d['Year'] for d in data]
espresso = [d['Espresso'] for d in data]
americano = [d['Americano'] for d in data]
cappuccino = [d['Cappuccino'] for d in data]
latte = [d['Latte'] for d in data]
mocha = [d['Mocha'] for d in data]

# Create the figure and axes
fig, ax = plt.subplots()

# Plot the stacked area chart
ax.stackplot(years, espresso, americano, cappuccino, latte, mocha, 
             labels=['Espresso', 'Americano', 'Cappuccino', 'Latte', 'Mocha'],
             colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'],
             alpha=0.8)

# Customize the plot with diversified visual encoding
plt.title('Coffee Sales Over Years')
plt.xlabel('Year')
plt.ylabel('Number of Drinks Sold')
plt.xticks(years)  # Set x-ticks to be the years
plt.legend(loc='upper left')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)  # Adding grid
plt.tight_layout()  # Adjust the plot to ensure everything fits without overlapping

# Show the plot
plt.show()