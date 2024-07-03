
import matplotlib.pyplot as plt
import numpy as np

categories = ['Renewable Energy', 'Fossil Fuels', 'Nuclear Energy', 'Other']
years = ['1990', '2000', '2010', '2020']
data = np.array([
    [5, 15, 25, 35],
    [80, 70, 55, 40],
    [10, 10, 15, 20],
    [5, 5, 5, 5]
])

data_cumsum = np.cumsum(data, axis=0)

fig, ax = plt.subplots(figsize=(10, 7))
bar_width = 0.5

colors = ['#4CAF50', '#FFC107', '#2196F3', '#9E9E9E']
for i in range(data.shape[0]):
    ax.bar(years, data[i], bottom=data_cumsum[i] - data[i], color=colors[i], edgecolor='white', width=bar_width)

ax.set_xlabel('Year')
ax.set_ylabel('Percentage')
ax.set_title('Energy Sources Distribution Over Time')
ax.legend(categories, loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=4)

plt.show()