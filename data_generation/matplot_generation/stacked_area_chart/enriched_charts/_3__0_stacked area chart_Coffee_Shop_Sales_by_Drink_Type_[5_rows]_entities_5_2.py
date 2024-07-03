
import matplotlib.pyplot as plt

# Data for each year
years = list(range(2010, 2022))
carbon_emissions = [300, 290, 280, 270, 260, 250, 245, 240, 230, 220, 210, 200]
renewable_energy = [60, 70, 80, 90, 105, 120, 135, 150, 165, 180, 200, 220]
electric_vehicles = [5, 8, 12, 18, 25, 35, 45, 60, 75, 90, 110, 130]
public_transport = [100, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160]

# Creating a stacked area chart
plt.figure(figsize=(14, 8))  # Modified chart size
plt.stackplot(years, carbon_emissions, renewable_energy, electric_vehicles, public_transport, 
              colors=['#FF5733', '#33FF57', '#3357FF', '#FFD700'])

# Adding labels and title
plt.title('Sustainable Transportation Trends (2010-2021)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Metric Tons of CO2', fontsize=14)

# Adding a legend
plt.legend(['Carbon Emissions', 'Renewable Energy', 'Electric Vehicles', 'Public Transport'], loc='upper right')

# Annotating the last data point for Electric Vehicles as an example
plt.annotate(f'{electric_vehicles[-1]} million', 
             (years[-1], sum([carbon_emissions[-1], renewable_energy[-1], electric_vehicles[-1]])), 
             textcoords="offset points", 
             xytext=(0, 10), 
             ha='center', 
             fontsize=12, 
             color='#3357FF')

plt.show()