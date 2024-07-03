
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
electricCars = [100, 150, 180, 220, 300, 370, 450]
hybridCars = [120, 130, 160, 190, 230, 250, 270]
dieselCars = [60, 80, 90, 100, 110, 120, 130]

# Plot
fig, ax = plt.subplots(figsize=(10, 8))

ax.barh(years, electricCars, color='#33A1C9', edgecolor='white', height=0.85,
        label='Electric Cars')
ax.barh(years, hybridCars, left=electricCars, color='#FFA07A', edgecolor='white',
        height=0.85, label='Hybrid Cars')
ax.barh(years, dieselCars, left=[i + j for i, j in zip(electricCars, hybridCars)], 
        color='#BDB76B', edgecolor='white', height=0.85, label='Diesel Cars')

# Labels and Title
ax.set_xlabel('Number of Cars')
ax.set_title('Car Sales by Type from 2015 to 2021')
ax.legend()

# Display the plot
plt.show()