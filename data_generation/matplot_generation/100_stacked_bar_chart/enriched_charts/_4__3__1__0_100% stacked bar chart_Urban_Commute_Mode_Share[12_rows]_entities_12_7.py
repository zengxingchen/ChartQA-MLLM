
import matplotlib.pyplot as plt
import numpy as np

years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
countries = ['USA', 'China', 'India', 'Germany', 'UK', 'France', 'Japan', 'Australia', 'Brazil', 'Canada']

data = [
    [30, 32, 29, 28, 27, 31, 33, 34, 32, 30],
    [15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
    [12, 11, 13, 14, 15, 14, 13, 12, 14, 13],
    [8, 7, 9, 10, 11, 10, 9, 8, 9, 10],
    [7, 8, 6, 7, 6, 5, 7, 8, 6, 7],
    [6, 5, 6, 7, 7, 6, 5, 6, 7, 6],
    [5, 6, 5, 6, 5, 6, 7, 6, 5, 6],
    [5, 4, 5, 4, 3, 4, 5, 6, 5, 4],
    [7, 6, 5, 4, 5, 6, 5, 4, 5, 6],
    [5, 5, 5, 6, 5, 4, 5, 4, 4, 5]
]

data = np.array(data)
data_percentage = data / data.sum(axis=0) * 100

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', '#33FFA1', '#FF9633', '#33A1FF', '#A1FF33', '#FF3333']

fig, ax = plt.subplots(figsize=(10, 12))

bar_width = 0.75
bars = np.arange(len(years))

bottoms = np.zeros(len(years))

for i in range(len(countries)):
    ax.bar(bars, data_percentage[i], bottom=bottoms, color=colors[i], edgecolor='white', width=bar_width)
    bottoms += data_percentage[i]

ax.set_ylabel('Percentage')
ax.set_xlabel('Years')
ax.set_title('Annual Energy Consumption by Country (2010-2019)')
ax.set_xticks(bars)
ax.set_xticklabels(years, rotation=45)
ax.legend(countries, loc='upper right', bbox_to_anchor=(1.2, 1))

plt.show()