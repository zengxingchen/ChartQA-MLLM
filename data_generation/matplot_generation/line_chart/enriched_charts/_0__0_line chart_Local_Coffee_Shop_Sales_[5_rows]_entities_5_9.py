
import matplotlib.pyplot as plt

years = [
    2000, 2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010, 2011,
    2012, 2013, 2014, 2015, 2016, 2017,
    2018, 2019, 2020
]
population = [
    126926, 130000, 133045, 136256, 139500, 142700,
    145800, 148950, 151000, 153050, 155000, 156950,
    158900, 160850, 162800, 164750, 166700, 168650,
    170600, 172550, 174500
]

plt.figure(figsize=(12, 8))
plt.plot(years, population, marker='o', color="#4682B4")

for year, pop in zip(years, population):
    plt.text(year, pop + 300, f'{pop/1000:.1f}K', ha='center', color='#2E8B57')

plt.title("Population Growth Over the Years", pad=20)
plt.xlabel("Year")
plt.ylabel("Population")

plt.tight_layout()
plt.show()