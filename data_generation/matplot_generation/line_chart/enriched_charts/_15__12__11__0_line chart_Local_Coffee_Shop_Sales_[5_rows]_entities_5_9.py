
import matplotlib.pyplot as plt

years = [
    2000, 2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010, 2011,
    2012, 2013, 2014, 2015, 2016, 2017,
    2018, 2019, 2020, 2021, 2022, 2023,
    2024, 2025
]

population_growth = [
    2.3, 2.5, 2.4, 2.6, 2.5, 2.7,
    2.6, 2.8, 2.7, 2.9, 2.8, 3.0,
    2.9, 3.1, 3.0, 3.2, 3.1, 3.3,
    3.2, 3.4, 3.3, 3.5, 3.4, 3.6,
    3.5, 3.7
]

plt.figure(figsize=(16, 9))
plt.plot(years, population_growth, marker='s', color="#4682B4")

for year, growth in zip(years, population_growth):
    plt.text(year, growth + 0.05, f'{growth}%', ha='center', color='#DC143C')

plt.title("Annual Population Growth Over the Years", pad=30)
plt.xlabel("Year")
plt.ylabel("Annual Population Growth (%)")
plt.gca().invert_yaxis()

plt.tight_layout()
plt.show()