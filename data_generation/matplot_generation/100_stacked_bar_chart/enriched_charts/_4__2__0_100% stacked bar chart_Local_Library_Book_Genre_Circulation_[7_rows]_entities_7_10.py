
import matplotlib.pyplot as plt
import numpy as np

categories = ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December']
activities = ['Cardio', 'Yoga', 'Weightlifting', 'Running', 'Cycling', 'Swimming']

data = np.array([
    [10, 15, 25, 20, 20, 10],
    [12, 18, 20, 22, 15, 13],
    [15, 20, 18, 25, 10, 12],
    [18, 15, 20, 20, 18, 9],
    [20, 10, 22, 15, 25, 8],
    [25, 12, 15, 18, 20, 10],
    [22, 18, 20, 25, 15, 8],
    [15, 20, 25, 20, 10, 10],
    [18, 25, 15, 10, 15, 17],
    [20, 22, 10, 15, 20, 13],
    [10, 18, 20, 22, 15, 15],
    [12, 25, 18, 20, 10, 15]
])

data_cumsum = np.cumsum(data, axis=1)
activity_colors = ['#4daf4a', '#377eb8', '#ff7f00', '#e41a1c', '#984ea3', '#f781bf']

fig, ax = plt.subplots(figsize=(12, 8))

for i, color in enumerate(activity_colors):
    heights = data[:, i]
    starts = data_cumsum[:, i] - heights
    ax.bar(categories, heights, bottom=starts, width=0.6, label=activities[i], color=color)

ax.set_ylabel('Percentage')
ax.set_title('Monthly Exercise Activity Distribution')
ax.legend(ncol=len(activities), bbox_to_anchor=(1, 1), loc='upper left', fontsize='small')

plt.xticks(rotation=45)
plt.show()