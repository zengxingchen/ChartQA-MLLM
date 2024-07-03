
import matplotlib.pyplot as plt
import numpy as np

categories = ['Breakfast', 'Lunch', 'Dinner', 'Snacks']
protein = [20, 25, 30, 15]
carbohydrates = [50, 40, 35, 60]
fats = [10, 15, 20, 10]
vitamins = [10, 10, 10, 10]
minerals = [10, 10, 5, 5]

data = np.array([protein, carbohydrates, fats, vitamins, minerals])
data_cum = data.cumsum(axis=0)

category_colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700']

fig, ax = plt.subplots(figsize=(10, 7))
category_names = ['Protein', 'Carbohydrates', 'Fats', 'Vitamins', 'Minerals']

ax.invert_yaxis()
ax.xaxis.set_visible(False)
ax.set_xlim(0, np.sum(data, axis=0).max())

for i, (colname, color) in enumerate(zip(category_names, category_colors)):
    widths = data[i]
    starts = data_cum[i] - widths
    ax.barh(categories, widths, left=starts, height=0.5, label=colname, color=color)

ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')

plt.title('Nutritional Content in Meals', fontsize=16)
plt.show()