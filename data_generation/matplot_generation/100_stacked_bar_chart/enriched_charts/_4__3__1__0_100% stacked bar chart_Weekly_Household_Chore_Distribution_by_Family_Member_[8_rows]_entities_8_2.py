
import matplotlib.pyplot as plt
import numpy as np

categories = ['Fruits', 'Vegetables', 'Grains', 'Dairy']
years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
data = np.array([
    [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],
    [25, 30, 25, 35, 30, 25, 20, 30, 25, 20, 25],
    [40, 35, 30, 25, 20, 25, 20, 15, 10, 15, 10],
    [25, 20, 25, 15, 20, 15, 20, 10, 15, 10, 5]
])

data_cumsum = np.cumsum(data, axis=0)

fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.6

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6']
for i in range(data.shape[0]):
    ax.bar(years, data[i], bottom=data_cumsum[i] - data[i], color=colors[i], edgecolor='white', width=bar_width)

ax.set_xlabel('Year')
ax.set_ylabel('Percentage')
ax.set_title('Food Consumption Trends Over Time')
ax.legend(categories, loc='upper right')

plt.show()