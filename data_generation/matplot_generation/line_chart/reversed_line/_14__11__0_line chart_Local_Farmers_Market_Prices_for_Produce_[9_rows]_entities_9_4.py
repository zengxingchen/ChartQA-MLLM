
import matplotlib.pyplot as plt

years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
happiness_index = [7.2, 7.1, 7.0, 6.8, 6.7, 6.6, 6.5, 6.4, 6.3, 6.1, 6.0, 5.9, 5.8, 5.6, 5.5, 5.4]

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(years, happiness_index, color='#ff5733', marker='o')

ax.set_title('Global Happiness Index Over Time', fontsize=18, pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Happiness Index', fontsize=14)
ax.invert_yaxis()

for year, index in zip(years, happiness_index):
    ax.annotate(f'{index}', xy=(year, index), textcoords="offset points", xytext=(0,10), ha='center')

plt.grid(True)
plt.show()