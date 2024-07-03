
import matplotlib.pyplot as plt
import numpy as np

data = {
    '2020': [25, 15, 30, 10, 20],
    '2021': [30, 20, 25, 10, 15],
    '2022': [35, 25, 20, 10, 10],
    '2023': [40, 30, 15, 10, 5]
}

categories = ['Wind', 'Solar', 'Hydro', 'Nuclear', 'Fossil Fuels']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

years = list(data.keys())
values = np.array(list(data.values()))
values_cumsum = values.cumsum(axis=1)

fig, ax = plt.subplots(figsize=(10, 6))

for i, (cat, color) in enumerate(zip(categories, colors)):
    widths = values[:, i]
    starts = values_cumsum[:, i] - widths
    ax.barh(years, widths, left=starts, height=0.7, label=cat, color=color)

ax.set_xlabel('Percentage')
ax.set_ylabel('Year')
ax.set_title('Renewable Energy Sources in % (2020-2023)')
ax.legend(loc='lower right')
plt.tight_layout()
plt.show()