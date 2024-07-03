
import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
          'August', 'September', 'October', 'November', 'December']
planets_discovered = [12, 14, 15, 18, 20, 22, 25, 27, 28, 30, 33, 35]
stars_observed = [50, 52, 55, 58, 60, 63, 65, 68, 70, 73, 75, 78]
galaxies_mapped = [3, 4, 4, 5, 6, 7, 8, 9, 9, 10, 11, 12]
space_missions = [1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 8]
new_exoplanets = [7, 9, 11, 14, 16, 18, 21, 23, 24, 26, 28, 30]

fig, ax = plt.subplots(figsize=(14, 8))

# Stacking the data
y = np.vstack([planets_discovered, stars_observed, galaxies_mapped, space_missions, new_exoplanets])

# Colors
colors = ['#4B0082', '#FF4500', '#2E8B57', '#4682B4', '#8A2BE2']

# Plotting the stacked area chart
ax.stackplot(months, y, labels=['Planets Discovered', 'Stars Observed', 'Galaxies Mapped', 'Space Missions', 'New Exoplanets'], colors=colors)

# Annotating specific points
ax.annotate('Record New Exoplanets', xy=('December', 30 + sum(y[:-1, -1])), xytext=('November', 28 + sum(y[:-1, -2])),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('High Space Missions', xy=('December', 8 + sum(y[:-1, -1])), xytext=('November', 7 + sum(y[:-1, -2])),
            arrowprops=dict(facecolor='orange', shrink=0.05))

# Adding title and labels
ax.set_title('Space Exploration Achievements in 2023')
ax.set_xlabel('Month')
ax.set_ylabel('Counts')

# Adding legend
ax.legend(loc='upper left')

plt.tight_layout()
plt.show()