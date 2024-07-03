
import matplotlib.pyplot as plt
import numpy as np

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
classical = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
pop = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
jazz = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
hiphop = [60, 65, 70, 75, 80, 85, 90, 95, 100, 105]
country = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
electronic = [35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
rock = [55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

# Bubble sizes
bubble_scale = 50
classical_sizes = np.array(classical) * bubble_scale
pop_sizes = np.array(pop) * bubble_scale
jazz_sizes = np.array(jazz) * bubble_scale
hiphop_sizes = np.array(hiphop) * bubble_scale
country_sizes = np.array(country) * bubble_scale
electronic_sizes = np.array(electronic) * bubble_scale
rock_sizes = np.array(rock) * bubble_scale

fig, ax = plt.subplots(figsize=(14, 8))

# Create scatter points for each category
ax.scatter(years, classical, s=classical_sizes, color='#8A2BE2', alpha=0.6, label='Classical')
ax.scatter(years, pop, s=pop_sizes, color='#FF69B4', alpha=0.6, label='Pop')
ax.scatter(years, jazz, s=jazz_sizes, color='#FFD700', alpha=0.6, label='Jazz')
ax.scatter(years, hiphop, s=hiphop_sizes, color='#1E90FF', alpha=0.6, label='Hip-Hop')
ax.scatter(years, country, s=country_sizes, color='#32CD32', alpha=0.6, label='Country')
ax.scatter(years, electronic, s=electronic_sizes, color='#FF4500', alpha=0.6, label='Electronic')
ax.scatter(years, rock, s=rock_sizes, color='#4682B4', alpha=0.6, label='Rock')

# Chart title and labels
ax.set_title('Trends in Music Genre Popularity Over the Years', fontsize=20, pad=20)
ax.set_xlabel('Year', fontsize=16)
ax.set_ylabel('Number of Fans (in millions)', fontsize=16)

# Legend
ax.legend(loc='upper left', title='Genre')

plt.tight_layout()
plt.show()