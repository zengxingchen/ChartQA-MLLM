
import matplotlib.pyplot as plt
import numpy as np

categories = [
    'Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5',
    'Category 6', 'Category 7', 'Category 8', 'Category 9', 'Category 10'
]

segment_a = np.array([20, 15, 25, 10, 30, 20, 25, 30, 20, 15])
segment_b = np.array([30, 35, 20, 40, 25, 30, 35, 20, 25, 30])
segment_c = np.array([25, 30, 35, 20, 25, 30, 20, 25, 30, 35])
segment_d = np.array([25, 20, 20, 30, 20, 20, 20, 25, 25, 20])

bar_width = 0.7

fig, ax = plt.subplots(figsize=(10, 8))

ax.barh(categories, segment_a, color='#FF5733', edgecolor='white', height=bar_width)
ax.barh(categories, segment_b, left=segment_a, color='#33FF57', edgecolor='white', height=bar_width)
ax.barh(categories, segment_c, left=segment_a + segment_b, color='#3357FF', edgecolor='white', height=bar_width)
ax.barh(categories, segment_d, left=segment_a + segment_b + segment_c, color='#F0FF33', edgecolor='white', height=bar_width)

ax.set_xlabel('Percentage')
ax.set_title('Distribution of Segments in Categories', pad=20)
ax.legend(['Segment A', 'Segment B', 'Segment C', 'Segment D'], bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()