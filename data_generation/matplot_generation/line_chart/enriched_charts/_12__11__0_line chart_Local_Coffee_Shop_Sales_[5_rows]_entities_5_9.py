import matplotlib.pyplot as plt

years = [
    2000, 2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010, 2011,
    2012, 2013, 2014, 2015, 2016, 2017,
    2018, 2019, 2020, 2021, 2022, 2023,
    2024, 2025
]

avg_temperatures = [
    15.1, 15.3, 15.2, 15.4, 15.3, 15.5,
    15.4, 15.6, 15.5, 15.7, 15.6, 15.8,
    15.7, 15.9, 15.8, 16.0, 15.9, 16.1,
    16.0, 16.2, 16.1, 16.3, 16.2, 16.4,
    16.3, 16.5
]

plt.figure(figsize=(14, 8))
plt.plot(years, avg_temperatures, marker='o', color="#8B0000")

for year, temp in zip(years, avg_temperatures):
    plt.text(year, temp + 0.05, f'{temp}°C', ha='center', color='#FF8C00')

plt.title("Annual Average Temperatures Over the Years", pad=20)
plt.xlabel("Year")
plt.ylabel("Annual Average Temperature (°C)")

plt.tight_layout()
plt.show()