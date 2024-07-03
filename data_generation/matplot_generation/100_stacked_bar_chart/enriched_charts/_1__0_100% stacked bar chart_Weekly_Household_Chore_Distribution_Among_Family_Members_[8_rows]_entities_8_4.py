
import matplotlib.pyplot as plt
import numpy as np

categories = ['Fruits', 'Vegetables', 'Dairy', 'Grains', 'Protein']
region_a = [25, 20, 15, 30, 10]
region_b = [30, 25, 20, 15, 10]
region_c = [20, 30, 25, 20, 5]
region_d = [15, 15, 30, 25, 15]
region_e = [10, 10, 10, 10, 10]

data = np.array([region_a, region_b, region_c, region_d, region_e])
data_cumsum = data.cumsum(axis=0)

colors = ['#FF5733', '#33FF57', '#3357FF', '#F333FF', '#33FFF3']
category_colors = {cat: color for cat, color in zip(categories, colors)}

fig, ax = plt.subplots(figsize=(12, 8))

for i, colname in enumerate(categories):
    widths = data[i, :]
    starts = data_cumsum[i] - widths
    ax.barh(categories, widths, left=starts, height=0.6, label=colname, color=category_colors[colname])

ax.set_xlabel('Percentage')
ax.set_title('Nutrition Distribution by Region')
ax.legend(ncol=5, bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')

plt.tight_layout()
plt.show()