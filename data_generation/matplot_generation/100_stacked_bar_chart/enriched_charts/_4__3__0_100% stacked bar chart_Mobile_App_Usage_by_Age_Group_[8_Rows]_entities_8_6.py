import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Acoustic', 'Electronic', 'Rock', 'Pop', 'Jazz', 'Hip-Hop', 'Classical', 'Country', 'Folk', 'Blues']
melody = [15, 5, 20, 25, 10, 30, 20, 25, 10, 5]
harmony = [25, 15, 15, 20, 30, 15, 25, 20, 25, 15]
rhythm = [30, 50, 40, 30, 35, 25, 30, 25, 35, 40]
lyrics = [10, 20, 10, 15, 10, 20, 5, 10, 20, 30]
instrumentation = [20, 10, 15, 10, 15, 10, 20, 20, 10, 10]

# Stack data
data = np.array([melody, harmony, rhythm, lyrics, instrumentation])
data_cum = data.cumsum(axis=0)

# Category colors
category_colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#DA70D6']

# Figure and Axes
fig, ax = plt.subplots(figsize=(12, 8))

# Plotting
labels = ['Melody', 'Harmony', 'Rhythm', 'Lyrics', 'Instrumentation']
for i, (colname, color) in enumerate(zip(labels, category_colors)):
    heights = data[i]
    starts = data_cum[i] - heights
    ax.bar(categories, heights, bottom=starts, width=0.5, label=colname, color=color)

# Customization
ax.set_title('Musical Elements Distribution Across Genres', fontsize=15, pad=20)
ax.legend(ncol=5, bbox_to_anchor=(1.0, 1.0), loc='upper left', fontsize='small')
ax.set_ylabel('Percentage (%)')
ax.set_xlabel('Music Genres')

# Display
plt.tight_layout()
plt.show()