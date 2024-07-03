import matplotlib.pyplot as plt

years = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027]
population = [102, 104, 106, 109, 111, 114, 117, 120, 124, 127, 131, 135, 138, 142, 146, 151, 155, 160, 165, 170, 175, 180, 185]

plt.figure(figsize=(16, 12))
plt.fill_between(years, population, color='#FF5733', alpha=0.6)

plt.title('Projected Population Growth of Small Town', fontsize=22, pad=20)
plt.xlabel('Year', fontsize=18)
plt.ylabel('Population (in thousands)', fontsize=18)

for i, txt in enumerate(population):
    plt.annotate(txt, (years[i], population[i]), textcoords="offset points", xytext=(0, 5), ha='center')

plt.show()