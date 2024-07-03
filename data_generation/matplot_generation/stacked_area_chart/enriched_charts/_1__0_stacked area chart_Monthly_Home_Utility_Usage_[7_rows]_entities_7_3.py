
import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
          'August', 'September', 'October', 'November', 'December']
solar = np.array([130, 140, 160, 170, 180, 185, 190, 180, 170, 160, 150, 140])
wind = np.array([160, 170, 180, 185, 195, 200, 205, 200, 190, 180, 170, 160])
hydro = np.array([135, 130, 145, 150, 155, 160, 165, 160, 155, 150, 145, 140])
nuclear = np.array([210, 220, 230, 235, 240, 250, 255, 250, 240, 230, 220, 210])
coal = np.array([140, 135, 125, 115, 105, 95, 85, 90, 105, 115, 130, 145])

# Stacking the data
energy_sources = np.vstack([solar, wind, hydro, nuclear, coal])

# Plot
fig, ax = plt.subplots(figsize=(14, 7))
ax.stackplot(months, energy_sources, colors=['#ff6347', '#4682b4', '#32cd32', '#ff69b4', '#8a2be2'])
ax.set_title('Monthly Energy Generation by Source in 2023', fontsize=18, fontweight='bold', loc='left')
ax.set_ylabel('Energy Generation (GWh)')

# Adding annotation on the chart for the maximum nuclear energy generation
max_nuclear_index = np.argmax(nuclear)
ax.annotate('Max Nuclear', xy=(max_nuclear_index, nuclear[max_nuclear_index]), xytext=(max_nuclear_index, nuclear[max_nuclear_index] + 50),
            arrowprops=dict(facecolor='black', arrowstyle='->'), ha='center')

plt.tight_layout()
plt.show()