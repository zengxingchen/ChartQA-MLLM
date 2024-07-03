
import matplotlib.pyplot as plt
import numpy as np

categories = ['2018', '2019', '2020', '2021', '2022']
classical = [20, 22, 25, 18, 15]
jazz = [25, 23, 20, 22, 18]
pop = [15, 18, 20, 25, 30]
rock = [10, 15, 20, 18, 20]
hiphop = [20, 12, 10, 12, 10]
country = [10, 10, 5, 5, 7]

bar_width = 0.85

classical_colors = '#FF5733'
jazz_colors = '#33FF57'
pop_colors = '#3357FF'
rock_colors = '#FF33A6'
hiphop_colors = '#A633FF'
country_colors = '#33FFF0'

fig, ax = plt.subplots(figsize=(10, 7))

ax.barh(categories, classical, color=classical_colors, edgecolor='white', height=bar_width)
ax.barh(categories, jazz, left=np.array(classical), color=jazz_colors, edgecolor='white', height=bar_width)
ax.barh(categories, pop, left=np.array(classical) + np.array(jazz), color=pop_colors, edgecolor='white', height=bar_width)
ax.barh(categories, rock, left=np.array(classical) + np.array(jazz) + np.array(pop), color=rock_colors, edgecolor='white', height=bar_width)
ax.barh(categories, hiphop, left=np.array(classical) + np.array(jazz) + np.array(pop) + np.array(rock), color=hiphop_colors, edgecolor='white', height=bar_width)
ax.barh(categories, country, left=np.array(classical) + np.array(jazz) + np.array(pop) + np.array(rock) + np.array(hiphop), color=country_colors, edgecolor='white', height=bar_width)

ax.set_xlabel('Percentage')
ax.set_title('Music Genre Popularity Over Years')
ax.legend(['Classical', 'Jazz', 'Pop', 'Rock', 'HipHop', 'Country'], loc='upper right')

plt.tight_layout()
plt.show()