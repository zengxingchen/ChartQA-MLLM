
import matplotlib.pyplot as plt

# Data for plotting
years = [
    2011, 2012, 2013, 2014, 2015, 2016,
    2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025
]
renewable_energy_capacity = [
    1000, 1100, 1250, 1450, 1700, 2000,
    2400, 2850, 3350, 4000, 4800, 5500,
    6300, 7200, 8200
]

# Changing figure size
plt.figure(figsize=(12, 10))

# Plotting - vertical bar chart
bar_width = 0.5
plt.bar(years, renewable_energy_capacity, color=[
    '#1e90ff', '#ff6347', '#32cd32', '#8a2be2', '#ffa500',
    '#ff69b4', '#daa520', '#8b0000', '#00ced1', '#ff4500',
    '#2e8b57', '#d2691e', '#00ff7f', '#4682b4', '#dc143c'
], width=bar_width)

# Customize chart
plt.xlabel('Year', fontsize=14)
plt.ylabel('Global Renewable Energy Capacity (GW)', fontsize=14)
plt.title('Global Renewable Energy Capacity Over the Years', fontsize=16)

# Resize bar width
plt.xticks(years, [str(year) for year in years], fontsize=10)

# Show plot
plt.show()