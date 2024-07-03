
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ["Action", "Comedy", "Drama", "Horror", "Thriller", "Sci-Fi", "Romance", "Adventure", "Fantasy", "Animation", "Documentary"]
value1 = [25, 30, 20, 35, 40, 50, 45, 55, 60, 70, 65]
value2 = [35, 40, 25, 45, 30, 20, 25, 20, 30, 20, 25]
value3 = [40, 30, 55, 20, 30, 30, 30, 25, 10, 10, 10]

# Create stacked bar chart
barWidth = 0.35
fig, ax = plt.subplots(figsize=(12, 8))

# Set position of bar on X axis
r = np.arange(len(categories))

# Make the plot
ax.bar(r, value1, color='#8b0000', edgecolor='grey', width=barWidth, label='Value 1')
ax.bar(r, value2, bottom=value1, color='#ffa500', edgecolor='grey', width=barWidth, label='Value 2')
ax.bar(r, value3, bottom=np.add(value1, value2), color='#006400', edgecolor='grey', width=barWidth, label='Value 3')

# Add labels
ax.set_ylabel('Percentage')
ax.set_xlabel('Genres')
ax.set_title('Distribution of Audience Preferences by Genre', pad=20)
ax.set_xticks(r)
ax.set_xticklabels(categories)
ax.legend(loc='upper left')

plt.show()