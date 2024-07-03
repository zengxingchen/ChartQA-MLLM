
import matplotlib.pyplot as plt
import numpy as np

# Data
countries = ["USA", "China", "Germany", "India", "Brazil", "Australia", "France", "Canada", "Japan", "UK"]
solar = [15, 20, 25, 10, 5, 30, 10, 20, 15, 20]
wind = [25, 30, 35, 20, 15, 25, 25, 30, 20, 25]
hydro = [20, 25, 15, 30, 40, 10, 20, 25, 25, 15]
nuclear = [10, 5, 10, 5, 5, 5, 30, 15, 20, 30]
coal = [30, 20, 15, 35, 35, 30, 15, 10, 20, 10]

# Stack data
data = np.array([solar, wind, hydro, nuclear, coal])
data_cum = data.cumsum(axis=0)

# Plotting
fig, ax = plt.subplots(figsize=(10, 7))

category_colors = ['#FFD700', '#87CEEB', '#32CD32', '#8A2BE2', '#A52A2A']
bar_width = 0.75

for i, (colname, color) in enumerate(zip(['Solar', 'Wind', 'Hydro', 'Nuclear', 'Coal'], category_colors)):
    heights = data[i]
    starts = data_cum[i] - heights
    ax.barh(countries, heights, left=starts, height=bar_width, label=colname, color=color)

# Title and labels
ax.set_title('Energy Sources Used in Various Countries (Percentage)', loc='center', fontsize=14)
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1), title='Energy Sources')
ax.set_xlabel('Percentage')
ax.set_ylabel('Country')

plt.show()