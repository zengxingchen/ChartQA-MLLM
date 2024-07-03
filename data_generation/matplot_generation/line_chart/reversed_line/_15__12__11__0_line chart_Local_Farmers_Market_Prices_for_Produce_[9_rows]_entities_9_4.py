
import matplotlib.pyplot as plt

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
co2_emissions = [370.5, 372.2, 374.1, 375.6, 378.0, 380.3, 382.5, 384.9, 387.2, 389.4, 391.6, 393.8, 396.0, 398.2, 400.4, 402.6]

fig, ax = plt.subplots(figsize=(16, 10))

ax.plot(years, co2_emissions, color='#1f77b4', marker='o', linewidth=2)

ax.set_title('CO2 Emissions Over Time', fontsize=18, pad=20)
ax.set_xlabel('Year', fontsize=16)
ax.set_ylabel('CO2 Emissions (ppm)', fontsize=16)

for year, emission in zip(years, co2_emissions):
    ax.annotate(f'{emission}', xy=(year, emission), textcoords="offset points", xytext=(0,10), ha='center')

plt.grid(True)
plt.gca().invert_yaxis()
plt.show()