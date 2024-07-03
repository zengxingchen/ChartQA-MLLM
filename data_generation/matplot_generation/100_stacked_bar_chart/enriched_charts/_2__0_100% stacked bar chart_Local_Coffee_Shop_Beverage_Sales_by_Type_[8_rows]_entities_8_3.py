
import matplotlib.pyplot as plt
import numpy as np

categories = ['Math', 'Science', 'History', 'Art', 'PE']
subcategory1 = [30, 25, 20, 15, 10]
subcategory2 = [40, 35, 25, 45, 50]
subcategory3 = [30, 40, 55, 40, 40]

bar_width = 0.5

fig, ax = plt.subplots(figsize=(10, 6))

x = np.arange(len(categories))

ax.barh(x, subcategory1, color='#FF5733', height=bar_width, label='Subcategory 1')
ax.barh(x, subcategory2, left=subcategory1, color='#33FF57', height=bar_width, label='Subcategory 2')
ax.barh(x, subcategory3, left=np.array(subcategory1) + np.array(subcategory2), color='#3357FF', height=bar_width, label='Subcategory 3')

ax.set_xlabel('Percentage')
ax.set_ylabel('Subjects')
ax.set_title('Percentage Distribution of Subcategories in Education')
ax.set_yticks(x)
ax.set_yticklabels(categories)
ax.legend()

plt.show()