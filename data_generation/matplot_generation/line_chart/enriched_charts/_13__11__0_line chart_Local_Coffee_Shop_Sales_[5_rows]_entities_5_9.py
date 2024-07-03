
import matplotlib.pyplot as plt

years = [
    2000, 2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010, 2011,
    2012, 2013, 2014, 2015, 2016, 2017,
    2018, 2019, 2020, 2021, 2022, 2023,
    2024, 2025
]

revenue = [
    500, 550, 600, 620, 670, 700,
    750, 800, 850, 900, 950, 1000,
    1050, 1100, 1150, 1200, 1250, 1300,
    1350, 1400, 1450, 1500, 1550, 1600,
    1650, 1700
]

plt.figure(figsize=(10, 6))
plt.plot(years, revenue, marker='o', color="#FF5733")

for year, rev in zip(years, revenue):
    plt.text(year, rev + 30, f'${rev}K', ha='center', color='#2E8B57')

plt.title("Annual Revenue of Fictional Company", fontsize=16, loc='center')
plt.xlabel("Year", fontsize=14)
plt.ylabel("Revenue (in thousand USD)", fontsize=14)

plt.tight_layout()
plt.show()