import matplotlib.pyplot as plt
import numpy as np

data = {
    'January': [10, 20, 30, 40],
    'February': [12, 18, 28, 42],
    'March': [14, 17, 27, 42],
    'April': [11, 19, 29, 41],
    'May': [15, 21, 26, 38],
    'June': [13, 20, 27, 40],
    'July': [12, 18, 29, 41],
    'August': [14, 19, 28, 39],
    'September': [15, 21, 27, 37],
    'October': [16, 22, 30, 32],
    'November': [14, 20, 29, 37],
    'December': [13, 21, 28, 38]
}

categories = ['Streaming Services', 'Music Concerts', 'Movie Tickets', 'Gaming']

months = list(data.keys())
values = np.array(list(data.values()))

values_percentage = values / values.sum(axis=0) * 100

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.6

bottoms = np.zeros(len(months))
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

for i, (category, color) in enumerate(zip(categories, colors)):
    ax.barh(months, values_percentage[:, i], bar_width, left=bottoms, color=color, label=category)
    bottoms += values_percentage[:, i]

ax.set_xlabel('Percentage')
ax.set_ylabel('Month')
ax.set_title('Monthly Spending on Leisure Activities in 2023')
ax.legend(loc='lower right', bbox_to_anchor=(1.15, 0))

plt.tight_layout()
plt.show()