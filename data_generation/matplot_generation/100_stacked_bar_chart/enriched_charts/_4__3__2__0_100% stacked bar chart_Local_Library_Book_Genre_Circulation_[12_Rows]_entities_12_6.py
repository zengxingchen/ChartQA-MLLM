
import matplotlib.pyplot as plt
import numpy as np

categories = ['Running', 'Swimming', 'Cycling', 'Weightlifting']
years = ['2018', '2019', '2020', '2021', '2022']

data = np.array([
    [15, 20, 25, 30, 35],  # Running
    [25, 30, 35, 20, 15],  # Swimming
    [35, 25, 20, 25, 30],  # Cycling
    [25, 25, 20, 25, 20]   # Weightlifting
])

data_cum = data.cumsum(axis=0)

fig, ax = plt.subplots(figsize=(10, 12))

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']
width = 0.5

for i, (colname, color) in enumerate(zip(categories, colors)):
    heights = data[i]
    starts = data_cum[i] - heights
    ax.bar(years, heights, bottom=starts, label=colname, color=color, width=width)

ax.set_ylabel('Percentage (%)')
ax.set_xlabel('Year')
ax.set_title('Sports & Fitness: Percentage of Time Spent on Various Activities Over Years')
ax.legend(loc='best', bbox_to_anchor=(1, 0.5))

plt.show()