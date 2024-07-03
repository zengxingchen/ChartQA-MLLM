
import matplotlib.pyplot as plt

# Data for each year
years = list(range(2010, 2021))
solar = [50, 65, 78, 90, 105, 120, 135, 150, 165, 180, 200]
wind = [80, 95, 110, 125, 140, 155, 170, 185, 200, 215, 230]
hydro = [150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200]
geothermal = [30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]

# Creating a stacked area chart
plt.figure(figsize=(14, 8))  # Modified chart size
plt.stackplot(years, solar, wind, hydro, geothermal, colors=['#FFA07A', '#20B2AA', '#9370DB', '#FFD700'])

# Adding labels and title
plt.title('Renewable Energy Production by Source (2010-2020)', fontsize=16, loc='center')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Energy Production (TWh)', fontsize=12)

# Adding a legend
plt.legend(['Solar', 'Wind', 'Hydro', 'Geothermal'], loc='upper left')

# Annotating the last data point for Solar energy as an example
plt.annotate(f'{solar[-1]} TWh', # Text with the value
             (years[-1], sum([solar[-1], wind[-1], hydro[-1]])), # Position at the end of the Solar series
             textcoords="offset points", # How to interpret the position
             xytext=(0,10), # Text offset 
             ha='center', # Horizontal alignment
             fontsize=10,
             color='#FFA07A') # Color matching the Solar series

plt.show()