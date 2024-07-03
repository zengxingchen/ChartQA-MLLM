import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Sleep Quality', 'Mental Health', 'Exercise', 'Nutrition', 'Stress Levels',
              'Work-Life Balance', 'Social Interaction', 'Happiness', 'Anxiety', 'Mindfulness']
positive = [35, 25, 45, 40, 20, 30, 50, 45, 25, 40]
neutral = [50, 55, 35, 40, 60, 50, 30, 40, 55, 40]
negative = [15, 20, 20, 20, 20, 20, 20, 15, 20, 20]

# Colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Bar width
bar_width = 0.5

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Stack the bars
bottom = np.zeros(len(categories))
for i, (data, color) in enumerate(zip([positive, neutral, negative], colors)):
    ax.barh(categories, data, left=bottom, color=color, edgecolor='white', height=bar_width)
    bottom += np.array(data)

# Customize the chart
ax.set_title('Distribution of Factors Affecting Health & Psychology', pad=20)
ax.set_xlabel('Percentage')
ax.set_ylabel('Categories')
ax.set_xlim(0, 100)
ax.legend(['Positive', 'Neutral', 'Negative'], loc='upper right')

# Display the plot
plt.tight_layout()
plt.show()