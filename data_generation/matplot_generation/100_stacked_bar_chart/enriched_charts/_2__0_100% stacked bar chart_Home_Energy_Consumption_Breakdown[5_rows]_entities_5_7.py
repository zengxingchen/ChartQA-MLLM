
import matplotlib.pyplot as plt
import numpy as np

categories = ['Sustainable Energy', 'Pollution Control', 'Biodiversity', 'Climate Change Awareness', 'Recycling Efforts', 'Water Conservation', 'Renewable Resources', 'Carbon Footprint Reduction', 'Eco-friendly Products', 'Environmental Education']
option1 = [40, 25, 35, 20, 30, 25, 30, 40, 35, 20]
option2 = [30, 50, 20, 35, 25, 40, 30, 20, 25, 40]
option3 = [30, 25, 45, 45, 45, 35, 40, 40, 40, 40]

# Data
data = np.array([option1, option2, option3])
data_cum = data.cumsum(axis=0)

# Parameters
category_colors = ['#FF5733', '#33FF57', '#3357FF']
bar_width = 0.7
fig_width, fig_height = 10, 7

fig, ax = plt.subplots(figsize=(fig_width, fig_height))
ax.invert_yaxis()
ax.xaxis.set_visible(False)
ax.set_xlim(0, np.sum(data, axis=0).max())

for i, (colname, color) in enumerate(zip(categories, category_colors)):
    widths = data[i]
    starts = data_cum[i] - widths
    ax.barh(categories, widths, left=starts, height=bar_width, label=colname, color=color)

ax.legend(ncol=len(category_colors), bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')
ax.set_title('Environment & Climate Change Initiatives')

plt.show()