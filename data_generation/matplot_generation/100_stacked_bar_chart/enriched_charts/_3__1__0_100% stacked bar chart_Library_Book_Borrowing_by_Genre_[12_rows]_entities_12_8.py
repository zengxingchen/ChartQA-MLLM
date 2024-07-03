import matplotlib.pyplot as plt
import numpy as np

categories = ['Renewable Energy', 'Fossil Fuels', 'Nuclear Energy', 'Hydropower']
years = ['2018', '2019', '2020', '2021']

data = np.array([
    [30, 25, 35, 10],  # Renewable Energy
    [40, 45, 30, 20],  # Fossil Fuels
    [20, 20, 20, 40],  # Nuclear Energy
    [10, 10, 15, 30]   # Hydropower
])

data_cumsum = np.cumsum(data, axis=1)
category_colors = ['#FF5733', '#DAF7A6', '#C70039', '#900C3F']

fig, ax = plt.subplots(figsize=(10, 7))

for i, (colname, color) in enumerate(zip(categories, category_colors)):
    widths = data[i]
    starts = data_cumsum[i] - widths
    ax.barh(years, widths, left=starts, height=0.5, label=colname, color=color)

ax.set_title('Energy Sources Distribution Over Years', pad=20)
ax.legend(ncol=len(categories), bbox_to_anchor=(0.5, -0.1), loc='lower center')
plt.show()