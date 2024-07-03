import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
labels = ['2000', '2005', '2010', '2015', '2020']
solar = np.array([5, 8, 15, 25, 35])
wind = np.array([10, 12, 18, 22, 30])
hydropower = np.array([25, 24, 20, 18, 15])
geothermal = np.array([8, 10, 12, 15, 18])
biomass = np.array([12, 10, 8, 8, 7])

# Calculating percentage for stacked bar chart
total = solar + wind + hydropower + geothermal + biomass
solar_perc = solar / total * 100
wind_perc = wind / total * 100
hydropower_perc = hydropower / total * 100
geothermal_perc = geothermal / total * 100
biomass_perc = biomass / total * 100

# Plotting the data
fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.6

bar1 = ax.barh(labels, solar_perc, color='#FFA07A', edgecolor='white', height=bar_width)
bar2 = ax.barh(labels, wind_perc, left=solar_perc, color='#20B2AA', edgecolor='white', height=bar_width)
bar3 = ax.barh(labels, hydropower_perc, left=solar_perc + wind_perc, color='#778899', edgecolor='white', height=bar_width)
bar4 = ax.barh(labels, geothermal_perc, left=solar_perc + wind_perc + hydropower_perc, color='#FF6347', edgecolor='white', height=bar_width)
bar5 = ax.barh(labels, biomass_perc, left=solar_perc + wind_perc + hydropower_perc + geothermal_perc, color='#4682B4', edgecolor='white', height=bar_width)

# Adding labels and title
ax.set_xlabel('Percentage')
ax.set_title('Renewable Energy Sources Usage (2000-2020)', pad=20)

# Adding legend
ax.legend((bar1, bar2, bar3, bar4, bar5), ('Solar Energy', 'Wind Energy', 'Hydropower', 'Geothermal Energy', 'Biomass Energy'), loc='upper right')

# Display the plot
plt.tight_layout()
plt.show()