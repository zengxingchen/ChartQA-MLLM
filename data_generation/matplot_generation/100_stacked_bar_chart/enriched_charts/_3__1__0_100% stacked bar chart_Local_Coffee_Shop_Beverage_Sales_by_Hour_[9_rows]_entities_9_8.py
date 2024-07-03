
import matplotlib.pyplot as plt
import numpy as np

categories = ['Basketball', 'Soccer', 'Tennis', 'Baseball']
years = ['2019', '2020', '2021', '2022']
data = np.array([[30, 25, 35, 40],
                 [20, 30, 25, 20],
                 [25, 20, 20, 25],
                 [25, 25, 20, 15]])

data_percentage = data / data.sum(axis=0) * 100

fig, ax = plt.subplots(figsize=(10, 7))
bar_width = 0.6
indices = np.arange(len(years))

colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']

bottoms = np.zeros(len(years))

for i in range(len(categories)):
    ax.barh(indices, data_percentage[i], left=bottoms, height=bar_width, color=colors[i], label=categories[i])
    bottoms += data_percentage[i]

ax.set_xlabel('Percentage')
ax.set_ylabel('Year')
ax.set_title('Popularity of Sports Over the Years')
ax.set_yticks(indices)
ax.set_yticklabels(years)
ax.legend(loc='upper right')

plt.show()