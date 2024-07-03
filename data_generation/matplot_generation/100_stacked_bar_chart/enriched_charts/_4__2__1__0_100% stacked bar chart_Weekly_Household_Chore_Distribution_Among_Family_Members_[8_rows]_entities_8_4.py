import matplotlib.pyplot as plt
import numpy as np

categories = [
    'Mathematics', 'Science', 'History', 'Geography', 
    'Art', 'Music', 'Physical Education', 'Literature', 
    'Technology', 'Languages'
]

data = np.array([
    [22, 33, 45],
    [20, 35, 45],
    [18, 27, 55],
    [25, 30, 45],
    [22, 32, 46],
    [15, 25, 60],
    [28, 37, 35],
    [23, 27, 50],
    [25, 30, 45],
    [20, 25, 55]
])

colors = ['#FF6347', '#4682B4', '#8A2BE2']

fig, ax = plt.subplots(figsize=(10, 12))
bar_width = 0.6

cumulative_data = np.cumsum(data, axis=1)

for i in range(data.shape[1]):
    if i == 0:
        ax.bar(categories, data[:, i], color=colors[i], edgecolor='white', width=bar_width)
    else:
        ax.bar(categories, data[:, i], bottom=cumulative_data[:, i-1], color=colors[i], edgecolor='white', width=bar_width)

ax.set_ylabel('Percentage')
ax.set_title('Student Participation in Different School Subjects', pad=20)
ax.legend(['Segment A', 'Segment B', 'Segment C'], loc='upper right')

plt.tight_layout()
plt.show()