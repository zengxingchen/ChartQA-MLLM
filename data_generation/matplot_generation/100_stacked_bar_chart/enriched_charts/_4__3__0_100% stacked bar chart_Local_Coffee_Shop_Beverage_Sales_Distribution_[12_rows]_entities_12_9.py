
import matplotlib.pyplot as plt
import numpy as np

categories = ['2018', '2019', '2020', '2021', '2022']
africa = [12, 14, 16, 18, 20]
asia = [20, 22, 19, 23, 25]
europe = [18, 20, 17, 22, 19]
north_america = [10, 15, 13, 17, 14]
south_america = [15, 12, 14, 11, 10]
australia = [25, 17, 21, 19, 23]

bar_width = 0.65

africa_colors = '#1f77b4'
asia_colors = '#ff7f0e'
europe_colors = '#2ca02c'
north_america_colors = '#d62728'
south_america_colors = '#9467bd'
australia_colors = '#8c564b'

fig, ax = plt.subplots(figsize=(12, 8))

ax.bar(categories, africa, color=africa_colors, edgecolor='white', width=bar_width)
ax.bar(categories, asia, bottom=np.array(africa), color=asia_colors, edgecolor='white', width=bar_width)
ax.bar(categories, europe, bottom=np.array(africa) + np.array(asia), color=europe_colors, edgecolor='white', width=bar_width)
ax.bar(categories, north_america, bottom=np.array(africa) + np.array(asia) + np.array(europe), color=north_america_colors, edgecolor='white', width=bar_width)
ax.bar(categories, south_america, bottom=np.array(africa) + np.array(asia) + np.array(europe) + np.array(north_america), color=south_america_colors, edgecolor='white', width=bar_width)
ax.bar(categories, australia, bottom=np.array(africa) + np.array(asia) + np.array(europe) + np.array(north_america) + np.array(south_america), color=australia_colors, edgecolor='white', width=bar_width)

ax.set_ylabel('Percentage')
ax.set_title('Popularity of Travel Destinations by Continent (2018-2022)')
ax.legend(['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Australia'], loc='upper right')

plt.tight_layout()
plt.show()