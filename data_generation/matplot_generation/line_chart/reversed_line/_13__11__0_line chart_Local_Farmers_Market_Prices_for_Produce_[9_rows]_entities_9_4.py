
import matplotlib.pyplot as plt

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
carbon_footprint = [8.0, 8.2, 7.9, 7.5, 7.3, 7.0, 6.8, 6.7, 6.5, 6.2, 6.0, 5.9, 5.7, 5.6, 5.4, 5.3]

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(years, carbon_footprint, color='#ff5733', marker='o')

ax.set_title('Annual Carbon Footprint Over Time', fontsize=18)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Carbon Footprint (Tons)', fontsize=14)

for year, footprint in zip(years, carbon_footprint):
    ax.annotate(f'{footprint}', xy=(year, footprint), textcoords="offset points", xytext=(0,10), ha='center')

plt.grid(True)
plt.show()