
import matplotlib.pyplot as plt

years = [
    2000, 2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010, 2011,
    2012, 2013, 2014, 2015, 2016, 2017,
    2018, 2019, 2020, 2021, 2022, 2023,
    2024, 2025
]

co2_emissions = [
    2500, 2550, 2600, 2580, 2620, 2700,
    2750, 2800, 2850, 2900, 2950, 3000,
    3100, 3200, 3250, 3300, 3350, 3400,
    3450, 3500, 3600, 3650, 3700, 3750,
    3800, 3850
]

plt.figure(figsize=(12, 7))
plt.plot(years, co2_emissions, marker='o', color="#4682B4")

for year, emission in zip(years, co2_emissions):
    plt.text(year, emission + 50, f'{emission}M', ha='center', color='#6B8E23')

plt.title("Annual CO2 Emissions Over the Years")
plt.xlabel("Year")
plt.ylabel("CO2 Emissions (in million metric tons)")

plt.tight_layout()
plt.show()