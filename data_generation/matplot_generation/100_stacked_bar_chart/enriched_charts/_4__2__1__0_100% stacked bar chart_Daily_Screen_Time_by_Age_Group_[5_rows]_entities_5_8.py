
import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    [25, 30, 20, 15, 10],
    [20, 25, 30, 15, 10],
    [15, 20, 25, 30, 10],
    [10, 15, 20, 30, 25],
    [5, 10, 20, 30, 35],
    [30, 25, 20, 15, 10],
    [15, 20, 25, 30, 10],
    [10, 15, 20, 25, 30],
    [20, 25, 30, 15, 10],
    [15, 20, 25, 30, 10]
])

categories = ['Pizza', 'Burger', 'Pasta', 'Salad', 'Sushi', 'Steak', 'Seafood', 'Vegetarian', 'Desserts', 'Fruits']
labels = ['Under 18', '18-25', '26-35', '36-50', 'Over 50']
colors = ['#FF6347', '#FFD700', '#8A2BE2', '#3CB371', '#FF4500']

data_cum = data.cumsum(axis=1)
category_colors = plt.get_cmap('tab20b')(np.linspace(0.15, 0.85, data.shape[1]))

fig, ax = plt.subplots(figsize=(10, 14))
ax.invert_yaxis()
ax.xaxis.set_visible(False)
ax.set_xlim(0, np.sum(data, axis=1).max())

for i, (colname, color) in enumerate(zip(labels, colors)):
    widths = data[:, i]
    starts = data_cum[:, i] - widths
    ax.barh(categories, widths, left=starts, height=0.8, label=colname, color=color)

ax.legend(ncol=len(labels), bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')
ax.set_title('Food Preferences Distribution Among Age Groups', loc='center')

plt.show()