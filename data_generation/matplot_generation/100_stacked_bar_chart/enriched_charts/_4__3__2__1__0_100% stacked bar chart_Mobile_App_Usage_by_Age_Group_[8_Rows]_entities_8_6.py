
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Fashion Trends', 'Beauty Standards', 'Celebrity News', 'Movie Releases', 
              'TV Shows', 'Music Festivals', 'Book Reviews', 'Video Games', 
              'Art Exhibitions', 'Theater Performances']
positive = [45, 50, 40, 35, 30, 55, 25, 50, 45, 35]
neutral = [35, 30, 45, 50, 40, 35, 55, 40, 40, 45]
negative = [20, 20, 15, 15, 30, 10, 20, 10, 15, 20]

# Colors
colors = ['#4CAF50', '#FFC107', '#F44336']

# Bar width
bar_width = 0.6

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 14))

# Stack the bars
bottom = np.zeros(len(categories))
for i, (data, color) in enumerate(zip([positive, neutral, negative], colors)):
    ax.bar(categories, data, bottom=bottom, color=color, edgecolor='white', width=bar_width)
    bottom += np.array(data)

# Customize the chart
ax.set_title('Factors Influencing Entertainment & Leisure Preferences', pad=20)
ax.set_ylabel('Percentage')
ax.set_xlabel('Categories')
ax.set_ylim(0, 100)
ax.legend(['Positive', 'Neutral', 'Negative'], loc='upper left')

# Display the plot
plt.tight_layout()
plt.show()