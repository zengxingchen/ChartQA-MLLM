import matplotlib.pyplot as plt
import numpy as np

categories = ['Reading', 'Experiment', 'Lecture', 'Homework', 'Discussion']
category_Physics = np.array([12, 18, 20, 25, 25])
category_Chemistry = np.array([15, 10, 22, 18, 25])
category_Biology = np.array([10, 15, 17, 20, 38])
category_Mathematics = np.array([20, 12, 15, 25, 28])
category_Computer_Science = np.array([18, 10, 25, 15, 32])

data = np.vstack([category_Physics, category_Chemistry, category_Biology, category_Mathematics, category_Computer_Science])
data_cum = data.cumsum(axis=0)

fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.5

colors = ['#FF5733', '#33FFBD', '#337BFF', '#FF33A6', '#85FF33']

for i, (colname, color) in enumerate(zip(['Physics', 'Chemistry', 'Biology', 'Mathematics', 'Computer Science'], colors)):
    heights = data[i]
    starts = data_cum[i] - heights
    ax.bar(categories, heights, bottom=starts, width=bar_width, label=colname, color=color)

ax.set_ylabel('Percentage')
ax.set_title('Time Allocation in Different Science Activities')
ax.legend(ncol=2, bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()