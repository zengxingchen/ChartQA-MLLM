
import matplotlib.pyplot as plt
import numpy as np

years = np.array(['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020'])
Apples = np.array([50, 52, 55, 58, 60, 63, 65, 68, 70, 72, 75])
Oranges = np.array([30, 32, 35, 38, 40, 42, 45, 48, 50, 52, 55])
Grapes = np.array([60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110])
Berries = np.array([10, 12, 15, 18, 20, 22, 25, 28, 30, 32, 35])

bar_width = 0.35
fig, ax = plt.subplots(figsize=(14, 10))

ax.bar(years, Apples, width=bar_width, label='Apples', color='#FF5733')
ax.bar(years, Oranges, bottom=Apples, width=bar_width, label='Oranges', color='#C70039')
ax.bar(years, Grapes, bottom=Apples+Oranges, width=bar_width, label='Grapes', color='#900C3F')
ax.bar(years, Berries, bottom=Apples+Oranges+Grapes, width=bar_width, label='Berries', color='#581845')

ax.set_ylabel('Quantity of Fruit')
ax.set_title('Quantity of Different Types of Fruit Consumed (2010-2020)', pad=20)
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years)
ax.legend(ncol=2, loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()