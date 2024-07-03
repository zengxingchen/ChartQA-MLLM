
import matplotlib.pyplot as plt
import numpy as np

# Data
data = {
    'Year': ['2015', '2016', '2017', '2018', '2019', '2020'],
    'Solar': [10, 12, 14, 16, 18, 20],
    'Wind': [15, 18, 20, 22, 24, 26],
    'Hydro': [30, 28, 25, 22, 20, 18],
    'Nuclear': [20, 22, 23, 24, 25, 26],
    'Fossil': [25, 20, 18, 16, 13, 10]
}

years = data['Year']
solar = data['Solar']
wind = data['Wind']
hydro = data['Hydro']
nuclear = data['Nuclear']
fossil = data['Fossil']

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.8

solar_bar = np.array(solar)
wind_bar = np.array(wind)
hydro_bar = np.array(hydro)
nuclear_bar = np.array(nuclear)
fossil_bar = np.array(fossil)

bar_positions = np.arange(len(years))

ax.barh(bar_positions, fossil_bar, color='#A93226', edgecolor='white', height=bar_width, label='Fossil')
ax.barh(bar_positions, nuclear_bar, left=fossil_bar, color='#884EA0', edgecolor='white', height=bar_width, label='Nuclear')
ax.barh(bar_positions, hydro_bar, left=fossil_bar + nuclear_bar, color='#3498DB', edgecolor='white', height=bar_width, label='Hydro')
ax.barh(bar_positions, wind_bar, left=fossil_bar + nuclear_bar + hydro_bar, color='#28B463', edgecolor='white', height=bar_width, label='Wind')
ax.barh(bar_positions, solar_bar, left=fossil_bar + nuclear_bar + hydro_bar + wind_bar, color='#F1C40F', edgecolor='white', height=bar_width, label='Solar')

# Customizing the plot
ax.set_yticks(bar_positions)
ax.set_yticklabels(years)
ax.set_xlabel('Percentage')
ax.set_title('Energy Sources Distribution Over Years', pad=20)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=5)

plt.tight_layout()
plt.show()