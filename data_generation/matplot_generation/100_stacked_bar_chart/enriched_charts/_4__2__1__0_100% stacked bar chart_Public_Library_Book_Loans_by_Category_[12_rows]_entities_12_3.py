
import matplotlib.pyplot as plt
import numpy as np

categories = ['Classical', 'Jazz', 'Rock', 'Pop', 'Hip-Hop', 'Electronic', 'Country', 'Folk', 'Reggae', 'Blues', 'Latin', 'World']
age_groups = ['18-25', '26-35', '36-45', '46-55', '56-65', '65+']
values = np.array([
    [15, 20, 25, 10, 20, 10],
    [20, 25, 20, 15, 10, 10],
    [25, 15, 20, 20, 10, 10],
    [30, 20, 10, 25, 10, 5],
    [10, 20, 15, 25, 20, 10],
    [10, 25, 15, 10, 20, 20],
    [20, 15, 20, 20, 10, 15],
    [25, 10, 15, 20, 15, 15],
    [10, 15, 20, 25, 15, 15],
    [15, 20, 25, 20, 10, 10],
    [20, 25, 15, 10, 15, 15],
    [25, 20, 15, 15, 15, 10]
])

percentages = values / values.sum(axis=1)[:, None] * 100

fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.7

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FF8C33', '#33FFF2']

bottom = np.zeros(len(categories))
for i in range(len(age_groups)):
    ax.bar(categories, percentages[:, i], bottom=bottom, width=bar_width, color=colors[i], label=age_groups[i])
    bottom += percentages[:, i]

ax.set_title('Music Genre Popularity by Age Group', pad=20)
ax.set_ylabel('Percentage')
ax.set_xlabel('Genres')

ax.legend(title='Age Groups', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()