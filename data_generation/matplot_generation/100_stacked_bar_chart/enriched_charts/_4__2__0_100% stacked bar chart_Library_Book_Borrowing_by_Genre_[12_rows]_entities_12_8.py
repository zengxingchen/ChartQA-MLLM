
import matplotlib.pyplot as plt
import numpy as np

categories = ['Formal Wear', 'Casual Wear', 'Sportswear', 'Accessories', 'Footwear']
male = [25, 35, 20, 10, 10]
female = [30, 25, 15, 20, 10]
unisex = [15, 25, 25, 25, 10]

data = np.array([male, female, unisex])
data_cum = data.cumsum(axis=0)

category_colors = ['#3498db', '#e74c3c', '#2ecc71']

fig, ax = plt.subplots(figsize=(10, 8))
category_names = ['Male', 'Female', 'Unisex']

ax.invert_yaxis()
ax.xaxis.set_visible(False)
ax.set_xlim(0, np.sum(data, axis=0).max())

for i, (colname, color) in enumerate(zip(category_names, category_colors)):
    widths = data[i]
    starts = data_cum[i] - widths
    ax.barh(categories, widths, left=starts, height=0.6, label=colname, color=color)

ax.legend(ncol=len(category_names), bbox_to_anchor=(1, 1), loc='lower left', fontsize='small')

plt.title('Fashion & Beauty: Clothing Distribution by Gender', fontsize=16, pad=20)
plt.show()