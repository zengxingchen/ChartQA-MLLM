import matplotlib.pyplot as plt
import numpy as np

categories = ['Rock', 'Pop', 'Jazz', 'Classical']
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
data = np.array([
    [15, 25, 35, 45],
    [25, 20, 30, 25],
    [35, 25, 25, 20],
    [45, 25, 20, 10],
    [25, 35, 20, 20],
    [20, 30, 25, 25],
    [30, 25, 20, 25],
    [35, 20, 25, 20],
    [40, 30, 20, 10],
    [50, 25, 15, 10]
])

data_cum = data.cumsum(axis=1)
data_sum = data.sum(axis=1)
data_normalized = data / data_sum[:, np.newaxis]

colors = ['#FF7F0E', '#1F77B4', '#2CA02C', '#D62728']

fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.5

for i in range(len(categories)):
    if i == 0:
        ax.bar(years, data_normalized[:, i], color=colors[i], edgecolor='white', width=bar_width, label=categories[i])
    else:
        ax.bar(years, data_normalized[:, i], bottom=data_normalized[:, :i].sum(axis=1), color=colors[i], edgecolor='white', width=bar_width, label=categories[i])

ax.set_title('Music Genre Popularity Over Years', pad=20)
ax.set_ylabel('Percentage')
ax.set_xlabel('Year')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1)

plt.tight_layout()
plt.show()