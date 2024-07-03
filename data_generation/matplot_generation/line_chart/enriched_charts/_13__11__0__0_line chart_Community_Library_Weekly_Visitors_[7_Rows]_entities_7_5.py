
import matplotlib.pyplot as plt

years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
population_growth = [1.2, 1.3, 1.4, 1.6, 1.5, 1.7, 1.8, 1.9, 2.0, 2.1, 2.3, 2.4, 2.5]

plt.figure(figsize=(12, 6))
plt.plot(years, population_growth, color='#4682B4', marker='o')

# Customize the trend of the data by simulating a slight dip and then increase
population_growth[4] = 1.5
plt.plot(years, population_growth, linestyle='--', color='#32CD32')

for i, growth in enumerate(population_growth):
    plt.annotate(f"{growth}%", (years[i], population_growth[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.title('Global Population Growth (2010-2022)', pad=20)
plt.xlabel('Year')
plt.ylabel('Population Growth (%)')
plt.grid(True)

plt.show()