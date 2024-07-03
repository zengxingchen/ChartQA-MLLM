
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Apple', 'Banana', 'Orange', 'Strawberry', 'Blueberry', 'Grapes', 'Watermelon', 'Peach', 'Pineapple', 'Mango']
protein = [1, 1.3, 1.2, 0.8, 0.7, 0.6, 0.6, 0.9, 0.5, 0.8]
fat = [0.2, 0.3, 0.2, 0.3, 0.3, 0.3, 0.2, 0.3, 0.2, 0.6]
carbohydrate = [14, 27, 12, 7.7, 14, 18, 8, 15, 13, 25]

# Stack data
data = np.array([protein, fat, carbohydrate])
data_cum = data.cumsum(axis=0)

# Color codes
colors = ['#FF9999', '#66B2FF', '#99FF99']

# Bar width
bar_width = 0.5

# Plotting
fig, ax = plt.subplots(figsize=(10, 7))
ax.invert_yaxis()
ax.xaxis.set_visible(False)
ax.set_xlim(0, np.sum(data, axis=0).max())

for i, colname in enumerate(['Protein', 'Fat', 'Carbohydrate']):
    widths = data[i]
    starts = data_cum[i] - widths
    ax.barh(categories, widths, left=starts, height=bar_width, label=colname, color=colors[i])

ax.legend(ncol=3, bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')
plt.title('Nutritional Content of Various Fruits')
plt.show()