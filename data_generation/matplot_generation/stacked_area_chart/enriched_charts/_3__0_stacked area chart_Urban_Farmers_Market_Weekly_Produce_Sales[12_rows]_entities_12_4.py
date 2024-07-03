
import matplotlib.pyplot as plt

# Data for stacked area chart
years = range(2012, 2023)
solar = [2000, 3000, 4000, 6000, 9000, 14000, 20000, 28000, 38000, 50000, 64000]
wind = [15000, 16000, 18000, 20000, 23000, 26000, 30000, 35000, 41000, 48000, 56000]
hydro = [50000, 52000, 54000, 56000, 58000, 60000, 62000, 64000, 66000, 68000, 70000]
geothermal = [1000, 1200, 1500, 2000, 3000, 4000, 5000, 7000, 9000, 12000, 15000]

# Plot
plt.figure(figsize=(14, 10))
plt.stackplot(years, solar, wind, hydro, geothermal, 
              colors=['#FF5733', '#33FF57', '#3357FF', '#FF33A6'])

# Customize the plot
plt.title('Renewable Energy Production by Source from 2012 to 2022', fontsize=16, pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Energy Production (GWh)', fontsize=14)
plt.legend(['Solar', 'Wind', 'Hydro', 'Geothermal'], loc='upper left')

# Annotation
for i, y in enumerate(years):
    plt.annotate(f'{solar[i]}', (y, solar[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.show()