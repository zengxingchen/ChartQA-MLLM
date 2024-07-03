import matplotlib.pyplot as plt
import numpy as np

categories = ['Sculpture', 'Painting', 'Literature', 'Music', 'Architecture', 'Dance', 'Theater']
classical = [35, 40, 25, 30, 20, 45, 30]
modern = [45, 35, 40, 40, 30, 35, 40]
contemporary = [20, 25, 35, 30, 50, 20, 30]

barWidth = 0.85
r = np.arange(len(categories))

fig, ax = plt.subplots(figsize=(10, 7))

ax.barh(r, classical, color='#FF9999', edgecolor='white', height=barWidth, label='Classical')
ax.barh(r, modern, left=classical, color='#66B2FF', edgecolor='white', height=barWidth, label='Modern')
ax.barh(r, contemporary, left=np.add(classical, modern), color='#99FF99', edgecolor='white', height=barWidth, label='Contemporary')

ax.set_xlabel('Percentage')
ax.set_title('Art and Design Styles Distribution', pad=20)
ax.set_yticks(r)
ax.set_yticklabels(categories)
ax.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1)
plt.tight_layout()
plt.show()