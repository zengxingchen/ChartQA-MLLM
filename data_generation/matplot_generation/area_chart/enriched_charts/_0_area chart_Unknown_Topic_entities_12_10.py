
import matplotlib.pyplot as plt

# Data
years = range(2010, 2021)
electric_cars = [1000, 1500, 2500, 4000, 7000, 10000, 13000, 18000, 25000, 32000, 45000]
solar_energy_houses = [2000, 2500, 4000, 7500, 12500, 20000, 30000, 40000, 50000, 65000, 80000]
smartphones = [50000, 80000, 150000, 200000, 300000, 400000, 450000, 500000, 600000, 700000, 800000]

# Plot
fig, ax = plt.subplots(figsize=(12, 8))  # changing width and height

# Plotting the area chart
ax.fill_between(years, electric_cars, color="#1f77b4", alpha=0.5, label='Electric Cars')
ax.fill_between(years, solar_energy_houses, color="#ff7f0e", alpha=0.5, label='Solar Energy Houses')
ax.fill_between(years, smartphones, color="#2ca02c", alpha=0.5, label='Smartphones')

# Titles and labels
ax.set_title('Technological Adoption from 2010 to 2020', fontsize=16)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Units', fontsize=14)

# Customizing the y-axis to get a better understanding of scales
ax.set_yscale('linear')

# Legend
ax.legend(loc='upper left')

plt.show()