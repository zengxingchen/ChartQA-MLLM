
import matplotlib.pyplot as plt
import numpy as np

categories = ['Sports', 'Fitness', 'Wellness']
years = ['2019', '2020', '2021', '2022', '2023']
data = np.array([
    [20, 30, 25, 25, 35], 
    [35, 25, 20, 20, 25], 
    [45, 45, 55, 55, 40]
])

data_cum = np.cumsum(data, axis=0)
data_perc = 100 * data / data_cum[-1]

colors = ['#FF5733', '#33FF57', '#3357FF']

fig, ax = plt.subplots(figsize=(10, 14))

bar_width = 0.6

for i, (colname, color) in enumerate(zip(categories, colors)):
    starts = data_cum[i] - data[i]
    ax.bar(years, data_perc[i], bottom=starts, width=bar_width, label=colname, color=color)

ax.set_title('Health & Wellness Trends Over Years', fontsize=18, pad=25)
ax.set_ylabel('Percentage', fontsize=14)
ax.set_xlabel('Years', fontsize=14)
ax.legend(loc='upper right', fontsize=12)

plt.show()