
import matplotlib.pyplot as plt

years = [
    2000, 2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010, 2011,
    2012, 2013, 2014, 2015, 2016, 2017,
    2018, 2019, 2020, 2021, 2022
]
population = [
    75, 73, 74, 72, 71, 70,
    69, 71, 68, 66, 65, 63,
    62, 61, 60, 59, 58, 56,
    55, 54, 53, 52, 50
]

plt.figure(figsize=(14, 10))
plt.plot(years, population, marker='o', color="#FF6347")

for year, pop in zip(years, population):
    plt.text(year, pop + 1, f'{pop}K', ha='center', color='#4682B4')

plt.gca().invert_yaxis()
plt.title("Annual Population Decline in Small Town", pad=20, loc='right')
plt.xlabel("Year")
plt.ylabel("Population (in thousands)")

plt.tight_layout()
plt.show()