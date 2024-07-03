
import matplotlib.pyplot as plt

years = [
    2000, 2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010, 2011,
    2012, 2013, 2014, 2015, 2016, 2017,
    2018, 2019, 2020, 2021, 2022
]
revenue = [
    25, 28, 35, 40, 50, 55,
    60, 65, 70, 80, 85, 90,
    95, 100, 105, 110, 115, 120,
    130, 135, 140, 150, 160
]

plt.figure(figsize=(14, 10))
plt.plot(years, revenue, marker='o', color="#FF6347")

for year, rev in zip(years, revenue):
    plt.text(year, rev + 2, f'{rev}M', ha='center', color='#4682B4')

plt.title("Annual Revenue Growth of a Tech Company", pad=20)
plt.xlabel("Year")
plt.ylabel("Revenue (in millions)")

plt.tight_layout()
plt.show()