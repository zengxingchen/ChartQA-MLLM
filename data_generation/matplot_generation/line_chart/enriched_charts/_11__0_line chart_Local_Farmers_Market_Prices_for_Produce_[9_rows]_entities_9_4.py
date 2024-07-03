import matplotlib.pyplot as plt

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
life_expectancy = [70.2, 70.4, 70.6, 70.8, 71.0, 71.1, 71.3, 71.4, 71.5, 71.7, 71.8, 71.9, 72.0, 72.1, 72.2, 72.3]

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(years, life_expectancy, color='#1f77b4', marker='s')

ax.set_title('Global Life Expectancy Over Time', fontsize=16)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Life Expectancy (Years)', fontsize=14)

for year, expectancy in zip(years, life_expectancy):
    ax.annotate(f'{expectancy}', xy=(year, expectancy), textcoords="offset points", xytext=(0,10), ha='center')

plt.grid(True)
plt.show()