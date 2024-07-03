
import matplotlib.pyplot as plt

# Data
countries = ['USA', 'Canada', 'Germany', 'France', 'Japan', 'China', 'India', 'Brazil', 'Australia', 'South Africa', 'UK', 'Italy', 'Spain', 'Russia', 'Mexico']
solar_energy = [200, 180, 190, 170, 160, 220, 210, 175, 185, 165, 195, 180, 175, 160, 170]
wind_energy = [150, 160, 140, 130, 120, 180, 170, 145, 155, 135, 150, 140, 135, 120, 130]
hydro_energy = [100, 110, 120, 105, 100, 130, 125, 115, 110, 105, 120, 115, 110, 105, 115]
geothermal_energy = [50, 60, 55, 52, 45, 70, 65, 58, 60, 55, 50, 60, 55, 50, 55]

# Colors for each energy type
colors = ['#FF5733','#33FF57','#3357FF','#FF33A6']

# Figure size
plt.figure(figsize=(10, 14))

# Bar heights
bar_height = 0.5

# Plotting
plt.barh(countries, solar_energy, color=colors[0], edgecolor='white', height=bar_height, label='Solar Energy')
plt.barh(countries, wind_energy, left=solar_energy, color=colors[1], edgecolor='white', height=bar_height, label='Wind Energy')
plt.barh(countries, hydro_energy, left=[solar_energy[i] + wind_energy[i] for i in range(len(hydro_energy))], color=colors[2], edgecolor='white', height=bar_height, label='Hydro Energy')
plt.barh(countries, geothermal_energy, left=[solar_energy[i] + wind_energy[i] + hydro_energy[i] for i in range(len(geothermal_energy))], color=colors[3], edgecolor='white', height=bar_height, label='Geothermal Energy')

# Adding numerical labels
for i in range(len(countries)):
    plt.text(solar_energy[i] / 2, i, str(solar_energy[i]), ha='center', va='center', color='white', fontsize=9)
    plt.text(solar_energy[i] + wind_energy[i] / 2, i, str(wind_energy[i]), ha='center', va='center', color='white', fontsize=9)
    plt.text(solar_energy[i] + wind_energy[i] + hydro_energy[i] / 2, i, str(hydro_energy[i]), ha='center', va='center', color='white', fontsize=9)
    plt.text(solar_energy[i] + wind_energy[i] + hydro_energy[i] + geothermal_energy[i] / 2, i, str(geothermal_energy[i]), ha='center', va='center', color='white', fontsize=9)

# Labels and Title
plt.xlabel('Energy Production (GWh)')
plt.title('Renewable Energy Production by Country')
plt.legend(loc='lower right')

# Display the plot
plt.tight_layout()
plt.show()