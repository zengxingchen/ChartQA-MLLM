
import matplotlib.pyplot as plt
import numpy as np

categories = ['Physical Activity', 'Mental Health', 'Work-Life Balance', 'Healthy Eating', 'Social Connections']
subcategory1 = [15, 25, 35, 20, 30]
subcategory2 = [25, 35, 30, 45, 25]
subcategory3 = [60, 40, 35, 35, 45]

bar_width = 0.7

fig, ax = plt.subplots(figsize=(12, 8))

x = np.arange(len(categories))

ax.bar(x, subcategory1, color='#FF5733', width=bar_width, label='Subcategory 1')
ax.bar(x, subcategory2, bottom=subcategory1, color='#33FF57', width=bar_width, label='Subcategory 2')
ax.bar(x, subcategory3, bottom=np.array(subcategory1) + np.array(subcategory2), color='#3357FF', width=bar_width, label='Subcategory 3')

ax.set_ylabel('Percentage')
ax.set_xlabel('Wellness Categories')
ax.set_title('Percentage Distribution of Wellness Subcategories')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend(loc='upper left')

plt.show()