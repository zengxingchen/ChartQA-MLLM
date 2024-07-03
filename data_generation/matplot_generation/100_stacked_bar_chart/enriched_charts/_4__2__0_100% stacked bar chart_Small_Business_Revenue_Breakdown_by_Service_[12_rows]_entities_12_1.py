
import matplotlib.pyplot as plt
import numpy as np

data = {
    '2020': [20, 30, 15, 10, 25],
    '2021': [18, 28, 16, 12, 26],
    '2022': [17, 25, 18, 13, 27],
    '2023': [15, 22, 19, 14, 30],
    '2024': [13, 20, 20, 15, 32],
    '2025': [12, 18, 21, 16, 33]
}

categories = ['Literature', 'Science', 'History', 'Philosophy', 'Art']
colors = ['#4e79a7', '#f28e2b', '#e15759', '#76b7b2', '#59a14f']

years = list(data.keys())
values = np.array(list(data.values()))
values_cumsum = values.cumsum(axis=0)

fig, ax = plt.subplots(figsize=(12, 8))

for i, (cat, color) in enumerate(zip(categories, colors)):
    heights = values[:, i]
    starts = values_cumsum[:, i] - heights
    ax.bar(years, heights, bottom=starts, label=cat, color=color, width=0.6)

ax.set_ylabel('Percentage')
ax.set_xlabel('Year')
ax.set_title('Popularity of Academic Subjects (2020-2025)')
ax.legend(loc='upper left')
plt.tight_layout()
plt.show()