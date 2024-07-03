
import matplotlib.pyplot as plt
import numpy as np

data = np.array([
    [20, 25, 30, 25],
    [15, 35, 30, 20],
    [25, 15, 35, 25],
    [30, 25, 20, 25],
    [10, 30, 30, 30],
    [35, 20, 25, 20]
])

categories = ['Math', 'Science', 'History', 'Arts', 'PE', 'Music']
types = ['Type1', 'Type2', 'Type3', 'Type4']
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']

data_cum = data.cumsum(axis=1)
fig, ax = plt.subplots(figsize=(10, 7))

ax.invert_yaxis()
ax.xaxis.set_visible(False)
ax.set_xlim(0, np.sum(data, axis=1).max())

for i, col in enumerate(types):
    widths = data[:, i]
    starts = data_cum[:, i] - widths
    ax.barh(categories, widths, left=starts, height=0.5, label=col, color=colors[i])

ax.legend(ncol=len(types), bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')
plt.title('Percentage Distribution of Subjects in Education & Learning', pad=20)
plt.show()