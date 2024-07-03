
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Skincare': [45, 30, 15, 10],
    'Makeup': [40, 35, 15, 10],
    'Haircare': [35, 25, 20, 20],
    'Fragrance': [30, 20, 30, 20],
    'Nails': [25, 20, 30, 25],
    'Bodycare': [20, 15, 35, 30],
    'Accessories': [15, 10, 40, 35]
}

categories = ['Cardio', 'Strength Training', 'Flexibility', 'Other']
colors = ['#FF4500', '#1E90FF', '#32CD32', '#FFD700']
topics = list(data.keys())
values = np.array(list(data.values()))
values_cum = values.cumsum(axis=1)

fig, ax = plt.subplots(figsize=(8, 12))

for i, col in enumerate(categories):
    heights = values[:, i]
    starts = values_cum[:, i] - heights
    ax.bar(topics, heights, bottom=starts, width=0.7, label=col, color=colors[i])

ax.set_ylabel('Percentage')
ax.set_xlabel('Beauty Category')
ax.set_title('Percentage Distribution of Beauty Product Types Among Categories')
ax.legend(ncol=len(categories), bbox_to_anchor=(1, 1), loc='upper left', fontsize='small')

plt.show()