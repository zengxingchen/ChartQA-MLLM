
import matplotlib.pyplot as plt

# Data
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
energy_sector = [4000, 4200, 4300, 4500, 4700, 4800, 5000, 5200, 5400, 5600]
industrial_production = [3000, 3200, 3300, 3500, 3600, 3700, 3800, 3900, 4000, 4100]
residential_usage = [2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900]
commercial_usage = [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900]

# Configuration for the figure size
plt.figure(figsize=(14, 8))

# Stacked horizontal bar chart
plt.barh(years, energy_sector, height=0.6, color='#ff9999', edgecolor='white', label='Energy Sector')
plt.barh(years, industrial_production, height=0.6, left=energy_sector, color='#66b3ff', edgecolor='white', label='Industrial Production')
plt.barh(years, residential_usage, height=0.6, left=[i+j for i,j in zip(energy_sector, industrial_production)], color='#99ff99', edgecolor='white', label='Residential Usage')
plt.barh(years, commercial_usage, height=0.6, left=[i+j+k for i,j,k in zip(energy_sector, industrial_production, residential_usage)], color='#ffcc99', edgecolor='white', label='Commercial Usage')

# Adding labels and title
plt.xlabel('Energy Consumption (in GWh)', fontsize=14)
plt.ylabel('Year', fontsize=14)
plt.title('Energy Consumption by Sector from 2010 to 2019', fontsize=16)

# Show legend
plt.legend()

# Display the chart
plt.show()