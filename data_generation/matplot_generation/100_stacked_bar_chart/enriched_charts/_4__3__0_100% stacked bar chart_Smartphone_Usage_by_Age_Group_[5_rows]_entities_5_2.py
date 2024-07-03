import matplotlib.pyplot as plt
import numpy as np

categories = ['Documentaries', 'Reality Shows', 'Sitcoms', 'Dramas', 'News', 'Sports']
values = np.array([[40, 30, 20, 10],
                   [25, 35, 15, 25],
                   [20, 30, 25, 25],
                   [35, 20, 25, 20],
                   [15, 25, 30, 30],
                   [30, 15, 20, 35]])

values_percentage = values / values.sum(axis=1)[:, None] * 100

bar_width = 0.7
fig, ax = plt.subplots(figsize=(12, 8))

bottoms = np.zeros(len(categories))
colors = ['#6A5ACD', '#FF4500', '#32CD32', '#FFD700']

for i in range(values.shape[1]):
    ax.bar(categories, values_percentage[:, i], bottom=bottoms, width=bar_width, color=colors[i])
    bottoms += values_percentage[:, i]

ax.set_ylabel('Percentage')
ax.set_title('Percentage Distribution of TV Show Genres')
ax.legend(['Documentaries', 'Reality Shows', 'Sitcoms', 'Dramas'], loc='upper left')

plt.show()