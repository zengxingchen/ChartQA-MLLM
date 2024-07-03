
import matplotlib.pyplot as plt
import numpy as np

categories = ['Grade 1', 'Grade 2', 'Grade 3', 'Grade 4', 'Grade 5', 
              'Grade 6', 'Grade 7', 'Grade 8', 'Grade 9', 'Grade 10',
              'Grade 11', 'Grade 12']
subjects = ['Science', 'Math', 'English', 'History', 'Art', 'Physical Education']

data = np.array([
    [20, 15, 25, 10, 15, 15],
    [22, 13, 23, 12, 18, 12],
    [25, 18, 20, 10, 12, 15],
    [18, 22, 15, 20, 15, 10],
    [15, 20, 18, 22, 10, 15],
    [20, 17, 20, 15, 12, 16],
    [18, 20, 15, 22, 15, 10],
    [22, 15, 20, 18, 12, 13],
    [20, 18, 25, 10, 15, 12],
    [25, 20, 15, 15, 10, 15],
    [18, 25, 15, 20, 15, 7],
    [20, 15, 22, 10, 20, 13]
])

data_cumsum = np.cumsum(data, axis=1)
category_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

fig, ax = plt.subplots(figsize=(10, 7))

for i, color in enumerate(category_colors):
    widths = data[:, i]
    starts = data_cumsum[:, i] - widths
    ax.barh(categories, widths, left=starts, height=0.7, label=subjects[i], color=color)

ax.set_xlabel('Percentage')
ax.set_title('Student Performance by Subject and Grade')
ax.legend(ncol=len(subjects), bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')

plt.show()