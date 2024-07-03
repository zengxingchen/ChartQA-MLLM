
import matplotlib.pyplot as plt

# Data for each year
years = list(range(2010, 2021))
solar = [50, 60, 70, 85, 100, 120, 135, 150, 170, 190, 215]
wind = [80, 92, 105, 117, 130, 145, 160, 175, 190, 210, 230]
nuclear = [120, 130, 140, 150, 155, 160, 165, 170, 180, 190, 200]
fossil = [450, 440, 430, 420, 415, 405, 390, 370, 350, 330, 310]

# Creating a stacked area chart
plt.figure(figsize=(12, 6))  # Modified chart size
plt.stackplot(years, solar, wind, nuclear, fossil, colors=['#FFD700', '#7FFF00', '#1E90FF', '#DC143C'])

# Adding labels and title
plt.title('Energy Consumption by Source (2010-2020)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Energy Consumption (TWh)', fontsize=12)

# Adding a legend
plt.legend(['Solar', 'Wind', 'Nuclear', 'Fossil'], loc='upper left')

# Annotating the last data point for Solar energy as an example
plt.annotate(f'{solar[-1]} TWh', # Text with the value
             (years[-1], sum([solar[-1], wind[-1], nuclear[-1]])), # Position at the end of the Solar series
             textcoords="offset points", # How to interpret the position
             xytext=(0,10), # Text offset 
             ha='center', # Horizontal alignment
             fontsize=10,
             color='#FFD700') # Color matching the Solar series

plt.show()