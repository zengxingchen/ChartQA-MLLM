
import matplotlib.pyplot as plt
import numpy as np

categories = ['Solar Energy', 'Wind Energy', 'Hydro Energy', 'Nuclear Energy']
years = ['2018', '2019', '2020', '2021', '2022']

data = np.array([
    [25, 30, 35, 40, 45],  # Solar Energy
    [20, 25, 30, 35, 40],  # Wind Energy
    [30, 25, 20, 15, 10],  # Hydro Energy
    [25, 20, 15, 10, 5]    # Nuclear Energy
])

data_cum = data.cumsum(axis=0)

fig, ax = plt.subplots(figsize=(12, 7))

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']
width = 0.5

for i, (colname, color) in enumerate(zip(categories, colors)):
    heights = data[i]
    starts = data_cum[i] - heights
    ax.barh(years, heights, left=starts, label=colname, color=color, height=width)

ax.set_xlabel('Percentage (%)')
ax.set_ylabel('Year')
ax.set_title('Energy Sources Percentage Over Years')
ax.legend(loc='best', bbox_to_anchor=(1, 1))

plt.show()