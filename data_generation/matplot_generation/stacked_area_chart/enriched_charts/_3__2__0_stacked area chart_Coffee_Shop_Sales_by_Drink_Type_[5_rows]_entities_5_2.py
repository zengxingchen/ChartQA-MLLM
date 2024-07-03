
import matplotlib.pyplot as plt

# Data for each year
years = list(range(2010, 2026))
satellites = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]
space_probes = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
rovers = [1, 2, 3, 3, 4, 5, 6, 7, 7, 8, 9, 10, 11, 12, 13, 14]
space_telescopes = [2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 8, 9, 10, 11, 11, 12]

# Creating a stacked area chart
plt.figure(figsize=(16, 10))
plt.stackplot(years, satellites, space_probes, rovers, space_telescopes, colors=['#FF6347', '#4682B4', '#9ACD32', '#8A2BE2'])

# Adding labels and title
plt.title('Growth of Space Exploration Assets (2010-2025)', fontsize=18, loc='center')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Assets', fontsize=14)

# Adding a legend
plt.legend(['Satellites', 'Space Probes', 'Rovers', 'Space Telescopes'], loc='upper left')

# Annotating the last data points
plt.annotate(f'{satellites[-1]}', (years[-1], sum([satellites[-1], space_probes[-1], rovers[-1], space_telescopes[-1]])), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, color='#FF6347')
plt.annotate(f'{space_probes[-1]}', (years[-1], sum([space_probes[-1], rovers[-1], space_telescopes[-1]])), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, color='#4682B4')
plt.annotate(f'{rovers[-1]}', (years[-1], sum([rovers[-1], space_telescopes[-1]])), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, color='#9ACD32')
plt.annotate(f'{space_telescopes[-1]}', (years[-1], space_telescopes[-1]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, color='#8A2BE2')

plt.show()