
import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.arange(2000, 2025)
renewable_energy = [20, 22, 25, 28, 30, 35, 38, 40, 42, 45, 47, 50, 53, 55, 57, 60, 62, 65, 68, 70, 72, 75, 78, 80, 82]
fossil_fuels = [70, 68, 65, 63, 60, 55, 52, 50, 48, 45, 42, 40, 37, 35, 32, 30, 27, 25, 22, 20, 18, 15, 12, 10, 8]
nuclear_energy = [10, 10, 10, 9, 10, 10, 10, 10, 10, 10, 11, 10, 10, 10, 11, 10, 11, 10, 10, 10, 10, 10, 10, 10, 10]

# Plot
fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.7

p1 = ax.barh(years, renewable_energy, color='#1f77b4', edgecolor='white', height=bar_width)
p2 = ax.barh(years, fossil_fuels, left=renewable_energy, color='#ff7f0e', edgecolor='white', height=bar_width)
p3 = ax.barh(years, nuclear_energy, left=np.array(renewable_energy) + np.array(fossil_fuels), color='#2ca02c', edgecolor='white', height=bar_width)

ax.set_xlabel('Percentage')
ax.set_title('Energy Source Distribution Over Time', pad=20)
ax.legend((p1[0], p2[0], p3[0]), ('Renewable Energy', 'Fossil Fuels', 'Nuclear Energy'), loc='upper left', bbox_to_anchor=(1, 1))

plt.show()