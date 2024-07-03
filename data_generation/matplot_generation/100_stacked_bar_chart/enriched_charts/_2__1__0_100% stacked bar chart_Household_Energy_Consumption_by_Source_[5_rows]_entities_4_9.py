import matplotlib.pyplot as plt
import numpy as np

data = {
    '2015': [25, 30, 25, 20],
    '2016': [30, 25, 20, 25],
    '2017': [20, 35, 25, 20],
    '2018': [35, 20, 25, 20],
    '2019': [30, 25, 30, 15],
    '2020': [25, 30, 20, 25],
    '2021': [20, 30, 30, 20],
    '2022': [30, 25, 25, 20],
    '2023': [25, 35, 20, 20]
}

categories = list(data.keys())
activities = ['Internet Use', 'Outdoor Activities', 'Reading', 'Others']
colors = ['#FF5733', '#33FF57', '#3357FF', '#F0FF33']

data_values = np.array(list(data.values()))
data_cum = data_values.cumsum(axis=1)

fig, ax = plt.subplots(figsize=(10, 7))

ax.barh(categories, data_values[:, 0], color=colors[0], height=0.6, label=activities[0])
for i in range(1, data_values.shape[1]):
    ax.barh(categories, data_values[:, i], left=data_cum[:, i - 1], color=colors[i], height=0.6, label=activities[i])

ax.set_xlabel('Percentage of Activities')
ax.set_ylabel('Year')
ax.set_title('Distribution of Leisure Activities Over Years')
ax.legend(loc='best')
plt.show()