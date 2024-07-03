
import matplotlib.pyplot as plt
import numpy as np

years = np.array(['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'])
Apples  = np.array([50, 45, 48, 60, 55, 53, 50, 52, 57, 60])
Oranges = np.array([35, 40, 55, 47, 50, 65, 60, 55, 65, 70])
Grapes  = np.array([60, 65, 70, 82, 75, 80, 85, 95, 90, 100])
Berries = np.array([20, 25, 22, 30, 28, 26, 24, 32, 29, 34])

bar_width = 0.5
fig, ax = plt.subplots(figsize=(10, 8))

ax.barh(years, Apples, height=bar_width, label='Apples', color='#FF9999')
ax.barh(years, Oranges, left=Apples, height=bar_width, label='Oranges', color='#FFCC99')
ax.barh(years, Grapes, left=Apples+Oranges, height=bar_width, label='Grapes', color='#99CCFF')
ax.barh(years, Berries, left=Apples+Oranges+Grapes, height=bar_width, label='Berries', color='#99FF99')

ax.set_xlabel('Quantity of Fruit')
ax.set_title('Quantity of Different Types of Fruit Consumed (2010-2019)')
ax.set_yticks(years)
ax.set_yticklabels(years)
ax.legend(ncol=4)

plt.tight_layout()
plt.show()