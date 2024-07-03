
import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2010, 2024)
asia = [20, 18, 22, 24, 26, 28, 30, 25, 27, 29, 31, 32, 30, 28]
europe = [25, 28, 20, 22, 24, 26, 20, 22, 24, 26, 28, 26, 24, 22]
north_america = [30, 25, 35, 28, 26, 24, 25, 30, 22, 20, 18, 19, 22, 24]
south_america = [15, 12, 10, 14, 12, 10, 15, 10, 14, 12, 10, 13, 11, 10]
africa = [5, 10, 8, 6, 8, 7, 6, 8, 9, 10, 8, 7, 8, 10]
oceania = [5, 7, 5, 6, 4, 5, 4, 5, 4, 3, 5, 3, 5, 6]

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FFC300', '#DAF7A6']

# Plot
fig, ax = plt.subplots(figsize=(10, 7))

ax.barh(years, asia, color=colors[0], edgecolor='white', height=0.7)
ax.barh(years, europe, left=np.array(asia), color=colors[1], edgecolor='white', height=0.7)
ax.barh(years, north_america, left=np.array(asia)+np.array(europe), color=colors[2], edgecolor='white', height=0.7)
ax.barh(years, south_america, left=np.array(asia)+np.array(europe)+np.array(north_america), color=colors[3], edgecolor='white', height=0.7)
ax.barh(years, africa, left=np.array(asia)+np.array(europe)+np.array(north_america)+np.array(south_america), color=colors[4], edgecolor='white', height=0.7)
ax.barh(years, oceania, left=np.array(asia)+np.array(europe)+np.array(north_america)+np.array(south_america)+np.array(africa), color=colors[5], edgecolor='white', height=0.7)

# Title and labels
ax.set_title('Distribution of Energy Consumption by Continent (2010-2023)', fontsize=15)
ax.set_xlabel('Percentage of Total Energy Consumption', fontsize=12)
ax.set_ylabel('Year', fontsize=12)

# Legend
ax.legend(['Asia', 'Europe', 'North America', 'South America', 'Africa', 'Oceania'], loc='upper right', bbox_to_anchor=(1.15, 1))

plt.show()