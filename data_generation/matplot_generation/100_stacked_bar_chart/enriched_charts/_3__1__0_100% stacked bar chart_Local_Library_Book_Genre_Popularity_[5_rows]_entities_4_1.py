
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030']
renewable_energy = np.array([35, 38, 42, 46, 50, 55, 60, 65, 70, 75, 80])
fossil_fuels = np.array([50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0])
nuclear_energy = np.array([15, 17, 18, 19, 20, 20, 20, 20, 20, 20, 20])

# Stacked Bar Chart
bar_width = 0.7
fig, ax = plt.subplots(figsize=(10, 8))

# Stacking
ax.barh(categories, renewable_energy, color='#1f77b4', edgecolor='white', height=bar_width)
ax.barh(categories, fossil_fuels, left=renewable_energy, color='#ff7f0e', edgecolor='white', height=bar_width)
ax.barh(categories, nuclear_energy, left=renewable_energy+fossil_fuels, color='#2ca02c', edgecolor='white', height=bar_width)

# Title and Labels
ax.set_title('Energy Source Distribution (2020-2030)', fontsize=16, pad=20)
ax.set_xlabel('Percentage', fontsize=12)
ax.set_ylabel('Year', fontsize=12)

# Legends
ax.legend(['Renewable Energy', 'Fossil Fuels', 'Nuclear Energy'], loc='upper right')

# Display
plt.tight_layout()
plt.show()