
import matplotlib.pyplot as plt
import numpy as np

categories = ['Quantum Computing', 'Artificial Intelligence', 'Nanotechnology', 'Biotechnology', 'Robotics', 
              'Virtual Reality', 'Augmented Reality', '3D Printing', 'Blockchain', 'Internet of Things']

subcategory1 = [35, 50, 45, 30, 40, 25, 20, 30, 40, 35]
subcategory2 = [40, 30, 35, 50, 30, 45, 50, 40, 35, 45]
subcategory3 = [25, 20, 20, 20, 30, 30, 30, 30, 25, 20]

barWidth = 0.5

r = np.arange(len(categories))

fig, ax = plt.subplots(figsize=(14, 8))

ax.barh(r, subcategory1, color='#FF9999', edgecolor='grey', height=barWidth, label='Subcategory 1')
ax.barh(r, subcategory2, left=subcategory1, color='#66B2FF', edgecolor='grey', height=barWidth, label='Subcategory 2')
ax.barh(r, subcategory3, left=np.array(subcategory1) + np.array(subcategory2), color='#99FF99', edgecolor='grey', height=barWidth, label='Subcategory 3')

ax.set_xlabel('Percentage')
ax.set_title('Future Technologies & Society: Research Focus Distribution', pad=20)
ax.set_yticks(r)
ax.set_yticklabels(categories)
ax.legend(loc='upper right', bbox_to_anchor=(1, 1))

plt.show()