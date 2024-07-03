
import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
          'August', 'September', 'October', 'November', 'December']
solar = np.array([120, 130, 150, 160, 170, 175, 180, 170, 160, 150, 140, 130])
wind = np.array([150, 160, 175, 180, 190, 195, 200, 195, 185, 170, 160, 150])
hydro = np.array([130, 125, 140, 145, 150, 155, 160, 155, 150, 145, 140, 135])
nuclear = np.array([200, 210, 220, 225, 230, 240, 245, 240, 230, 220, 210, 200])
coal = np.array([145, 140, 130, 120, 110, 100, 90, 95, 110, 120, 130, 140])

# Stacking the data
energy_sources = np.vstack([solar, wind, hydro, nuclear, coal])

# Plot
fig, ax = plt.subplots(figsize=(12, 6))  # Modified chart size
ax.stackplot(months, energy_sources, colors=['#ffac81', '#ff928b', '#fec3a6', '#efe9ae', '#cdeac0'])
ax.set_title('Monthly Energy Consumption by Source in 2023', fontsize=16, fontweight='bold')  # Changed title
ax.set_ylabel('Energy Consumption (GWh)')

# Adding annotation on the chart for the maximum solar energy consumption
max_solar_index = np.argmax(solar)
ax.annotate('Max Solar', xy=(max_solar_index, solar[max_solar_index]), xytext=(max_solar_index, solar[max_solar_index] + 50),
            arrowprops=dict(facecolor='black', arrowstyle='->'), ha='center')

plt.tight_layout()
plt.show()