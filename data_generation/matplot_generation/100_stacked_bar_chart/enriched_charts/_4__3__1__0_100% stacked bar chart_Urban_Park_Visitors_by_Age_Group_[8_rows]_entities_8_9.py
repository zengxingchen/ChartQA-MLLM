
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Classical', 'Rock', 'Pop', 'Jazz', 'Hip-Hop', 'Electronic', 'Country', 'Reggae', 'Blues', 'Metal']
genre1 = [30, 20, 25, 15, 10, 35, 40, 10, 30, 25]
genre2 = [20, 30, 35, 25, 15, 25, 20, 35, 20, 15]
genre3 = [50, 50, 40, 60, 75, 40, 40, 55, 50, 60]

# Stack data
data = np.array([genre1, genre2, genre3])
data_cum = data.cumsum(axis=0)

# Color codes
colors = ['#FF5733', '#33FF57', '#3357FF']

# Bar width
bar_width = 0.7

# Plotting
fig, ax = plt.subplots(figsize=(12, 9))
ax.set_ylim(0, np.sum(data, axis=0).max())
ax.invert_yaxis()
ax.yaxis.set_visible(False)

for i, colname in enumerate(['Genre1', 'Genre2', 'Genre3']):
    heights = data[i]
    starts = data_cum[i] - heights
    ax.bar(categories, heights, bottom=starts, width=bar_width, label=colname, color=colors[i])

ax.legend(ncol=3, bbox_to_anchor=(1, 1), loc='upper left', fontsize='small')
plt.title('Popularity Distribution of Music Genres', loc='left')
plt.xticks(rotation=45)
plt.show()