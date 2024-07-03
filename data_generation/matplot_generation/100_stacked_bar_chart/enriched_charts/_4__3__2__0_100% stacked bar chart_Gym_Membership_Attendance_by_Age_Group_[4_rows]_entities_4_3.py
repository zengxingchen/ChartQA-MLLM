import matplotlib.pyplot as plt
import numpy as np

data = {
    '2019': [20, 25, 15, 20, 20],
    '2020': [25, 30, 10, 15, 20],
    '2021': [30, 20, 15, 20, 15],
    '2022': [35, 15, 20, 15, 15]
}

categories = ['Fiction', 'Non-Fiction', 'Science', 'History', 'Biography']
years = list(data.keys())
values = np.array(list(data.values()))

values_percentage = values / values.sum(axis=1)[:, None] * 100

bar_width = 0.7
fig, ax = plt.subplots(figsize=(12, 8))

bottom = np.zeros(len(years))

colors = ['#E69F00', '#56B4E9', '#009E73', '#F0E442', '#0072B2']

for i, category in enumerate(categories):
    ax.bar(years, values_percentage[:, i], bar_width, bottom=bottom, label=category, color=colors[i])
    bottom += values_percentage[:, i]

ax.set_ylabel('Percentage')
ax.set_title('Literature Book Preferences (2019-2022)')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()