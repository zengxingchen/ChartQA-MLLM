
import matplotlib.pyplot as plt

years = [
    2000, 2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010, 2011,
    2012, 2013, 2014, 2015, 2016, 2017,
    2018, 2019, 2020, 2021, 2022, 2023,
    2024, 2025
]

population = [
    5.0, 5.2, 5.4, 5.6, 5.7, 5.9,
    6.1, 6.2, 6.3, 6.4, 6.6, 6.7,
    6.8, 6.9, 7.0, 7.1, 7.2, 7.3,
    7.4, 7.5, 7.6, 7.7, 7.8, 7.9,
    8.0, 8.1
]

plt.figure(figsize=(14, 8))
plt.plot(years, population, marker='o', color="#FF6347")

for year, pop in zip(years, population):
    plt.text(year, pop + 0.05, f'{pop}B', ha='center', color='#2E8B57')

plt.gca().invert_yaxis()
plt.title("World Population Growth Over the Years")
plt.xlabel("Year")
plt.ylabel("Population (in billion)")
plt.tight_layout()
plt.show()