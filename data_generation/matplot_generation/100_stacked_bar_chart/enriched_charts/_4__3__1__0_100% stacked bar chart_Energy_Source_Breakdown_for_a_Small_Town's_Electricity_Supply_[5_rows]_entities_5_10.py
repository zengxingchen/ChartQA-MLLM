
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Week 1': [25, 20, 30, 15, 10],
    'Week 2': [22, 25, 25, 18, 10],
    'Week 3': [20, 28, 22, 20, 10],
    'Week 4': [25, 20, 30, 15, 10],
    'Week 5': [28, 25, 20, 17, 10],
    'Week 6': [25, 30, 20, 15, 10],
    'Week 7': [22, 25, 28, 15, 10],
    'Week 8': [25, 20, 25, 20, 10],
    'Week 9': [22, 25, 28, 15, 10],
    'Week 10': [28, 20, 25, 17, 10],
    'Week 11': [25, 28, 22, 15, 10],
    'Week 12': [22, 25, 28, 15, 10],
}

categories = ['Reading', 'Writing', 'Drawing', 'Painting', 'Sculpting']
weeks = list(data.keys())
values = np.array(list(data.values()))

values_percentage = values / values.sum(axis=1, keepdims=True) * 100

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

fig, ax = plt.subplots(figsize=(10, 14))
bottom = np.zeros(len(weeks))

for i, (cat, color) in enumerate(zip(categories, colors)):
    ax.bar(weeks, values_percentage[:, i], bottom=bottom, color=color, label=cat)
    bottom += values_percentage[:, i]

ax.set_ylabel('Percentage')
ax.set_title('Weekly Distribution of Creative Activities')
ax.legend(loc='upper right')

plt.tight_layout()
plt.show()