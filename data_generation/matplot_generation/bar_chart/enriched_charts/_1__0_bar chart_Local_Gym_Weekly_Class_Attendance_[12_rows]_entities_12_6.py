
import matplotlib.pyplot as plt

# Data
animals = ['Dogs', 'Cats', 'Cattle', 'Sheep', 'Goats',
           'Pigs', 'Horses', 'Chickens', 'Ducks', 'Turkeys',
           'Rabbits', 'Camels', 'Elephants', 'Tigers', 'Giraffes']
population = [900, 600, 1400, 1100, 900,
              770, 60, 24000, 1200, 470,
              700, 25, 0.5, 0.004, 0.1]

# Create bar chart
plt.figure(figsize=(12, 7))  # Change width and height of the chart
colors = ['#4daf4a', '#377eb8', '#ff7f00', '#984ea3', '#e41a1c',
          '#a65628', '#f781bf', '#999999', '#66c2a5', '#fc8d62',
          '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f', '#b3b3b3']

plt.bar(animals, population, color=colors, width=0.6)  # Change direction of chart and bar width

# Customizing the plot
plt.ylabel('Population (in millions)')
plt.title('Global Animal Populations (2020)', pad=20)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()