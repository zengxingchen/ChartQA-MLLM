
import matplotlib.pyplot as plt
import numpy as np

# Data
schools = ['School A', 'School B', 'School C', 'School D', 'School E', 'School F', 'School G', 'School H', 'School I', 'School J', 'School K', 'School L', 'School M', 'School N', 'School O']
math_scores = [88, 75, 90, 68, 82, 77, 93, 81, 74, 85, 79, 91, 73, 84, 78]
science_scores = [92, 80, 87, 73, 88, 72, 95, 86, 78, 89, 82, 94, 75, 88, 81]
reading_scores = [85, 78, 89, 70, 84, 76, 91, 83, 76, 87, 80, 90, 74, 86, 79]
writing_scores = [78, 82, 84, 65, 80, 70, 89, 88, 74, 83, 77, 92, 72, 81, 76]

# Stacked bar chart data
data = np.array([math_scores, science_scores, reading_scores, writing_scores])
data_cum = data.cumsum(axis=0)

# Category names and colors
category_names = ['Math Scores', 'Science Scores', 'Reading Scores', 'Writing Scores']
colors = ['#4e79a7', '#f28e2c', '#e15759', '#76b7b2']

# Plot
fig, ax = plt.subplots(figsize=(14, 10))
bar_height = 0.6

# Plot each layer of the bar chart
for i, (colname, color) in enumerate(zip(category_names, colors)):
    heights = data[i]
    starts = data_cum[i] - heights
    ax.bar(schools, heights, bottom=starts, width=bar_height, label=colname, color=color)

# Add labels, title, and legend
ax.set_ylabel('Scores')
ax.set_title('Student Performance Metrics by School', loc='center')
ax.legend(ncol=len(category_names), bbox_to_anchor=(1, 1), loc='upper left', fontsize='small')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()