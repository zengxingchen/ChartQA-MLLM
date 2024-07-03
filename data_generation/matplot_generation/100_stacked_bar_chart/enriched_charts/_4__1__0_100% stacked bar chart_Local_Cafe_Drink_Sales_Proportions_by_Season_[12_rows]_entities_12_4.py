
import matplotlib.pyplot as plt
import numpy as np

categories = ['Painting', 'Sculpture', 'Digital Art', 'Photography', 'Graphic Design', 'Fashion Design']
value_1 = np.array([15, 25, 20, 10, 30, 35])
value_2 = np.array([20, 15, 25, 30, 20, 25])
value_3 = np.array([30, 35, 30, 25, 25, 20])
value_4 = np.array([35, 25, 25, 35, 25, 20])

totals = value_1 + value_2 + value_3 + value_4
value_1 = value_1 / totals * 100
value_2 = value_2 / totals * 100
value_3 = value_3 / totals * 100
value_4 = value_4 / totals * 100

colors = ['#FF8C00', '#6A5ACD', '#20B2AA', '#FF1493']

fig, ax = plt.subplots(figsize=(10, 14))

bar_width = 0.6

bars1 = ax.bar(categories, value_1, color=colors[0], edgecolor='white', width=bar_width)
bars2 = ax.bar(categories, value_2, bottom=value_1, color=colors[1], edgecolor='white', width=bar_width)
bars3 = ax.bar(categories, value_3, bottom=value_1+value_2, color=colors[2], edgecolor='white', width=bar_width)
bars4 = ax.bar(categories, value_4, bottom=value_1+value_2+value_3, color=colors[3], edgecolor='white', width=bar_width)

ax.set_ylabel('Percentage (%)')
ax.set_title('Distribution of Art & Design Skills by Categories')

ax.legend(['Painting', 'Sculpture', 'Digital Art', 'Photography'], loc='upper right')

plt.show()