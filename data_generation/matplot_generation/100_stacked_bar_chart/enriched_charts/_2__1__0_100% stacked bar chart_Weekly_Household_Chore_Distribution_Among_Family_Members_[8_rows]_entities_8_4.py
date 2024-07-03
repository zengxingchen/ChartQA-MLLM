
import matplotlib.pyplot as plt
import numpy as np

categories = [
    'Digital Marketing', 'Product Development', 'Human Resources', 'Sales', 
    'Customer Support', 'Finance', 'IT', 'Operations', 'Legal', 'R&D'
]

data = np.array([
    [25, 35, 40],
    [20, 30, 50],
    [15, 25, 60],
    [30, 40, 30],
    [20, 30, 50],
    [10, 20, 70],
    [25, 35, 40],
    [30, 40, 30],
    [20, 30, 50],
    [15, 25, 60]
])

colors = ['#FF5733', '#33FF57', '#3357FF']

fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.7

cumulative_data = np.cumsum(data, axis=1)

for i in range(data.shape[1]):
    if i == 0:
        ax.barh(categories, data[:, i], color=colors[i], edgecolor='white', height=bar_width)
    else:
        ax.barh(categories, data[:, i], left=cumulative_data[:, i-1], color=colors[i], edgecolor='white', height=bar_width)

ax.set_xlabel('Percentage')
ax.set_title('Departmental Budget Allocation in a Company', pad=20)
ax.legend(['Segment A', 'Segment B', 'Segment C'], loc='upper left', bbox_to_anchor=(1,1))

plt.tight_layout()
plt.show()