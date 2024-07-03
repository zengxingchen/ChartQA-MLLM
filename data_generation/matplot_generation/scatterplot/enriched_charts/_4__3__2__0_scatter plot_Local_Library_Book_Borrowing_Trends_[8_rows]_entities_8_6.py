
import matplotlib.pyplot as plt

# Data for scatterplot
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
temperature_c = [15.1, 15.6, 14.8, 15.3, 15.7, 15.2, 16.1, 15.4, 15.9, 16.3, 16.0, 15.5, 16.2, 15.8]
sunshine_hours = [1800, 1850, 1700, 1900, 1950, 1800, 2000, 1850, 1900, 1950, 2000, 1800, 2050, 1900]
precipitation_mm = [650, 620, 700, 590, 580, 650, 540, 610, 600, 560, 530, 640, 520, 600]

# Size of each point will be proportional to the precipitation level
sizes = [precip * 0.5 for precip in precipitation_mm]

# Different colors for different temperature levels
colors = ['#FF5733', '#FFBD33', '#FF8D33', '#FFC733', '#FF5733', '#FFBD33', 
          '#FF8D33', '#FFC733', '#FF5733', '#FFBD33', '#FF8D33', '#FFC733', '#FF5733', '#FFBD33']

# Create scatterplot
plt.figure(figsize=(18, 10))  # increase the width and height of the chart
plt.scatter(years, temperature_c, s=sizes, c=colors, alpha=0.7)

# Chart details
plt.title('Annual Climate Overview', fontsize=20, pad=30)
plt.xlabel('Year', fontsize=16)
plt.ylabel('Average Temperature (°C)', fontsize=16)
plt.grid(True)

# Show the chart
plt.show()