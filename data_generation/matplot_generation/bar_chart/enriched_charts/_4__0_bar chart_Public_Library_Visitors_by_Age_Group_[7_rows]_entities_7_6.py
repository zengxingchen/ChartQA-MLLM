
import matplotlib.pyplot as plt

# Data
categories = [
    "Happiness Index", "Stress Levels", "Physical Health", "Mental Well-being",
    "Life Satisfaction", "Social Connections", "Work-Life Balance", "Financial Security",
    "Personal Growth", "Sleep Quality", "Exercise Frequency", "Nutritional Health"
]
values = [7.8, 4.3, 6.5, 5.2, 7.0, 6.8, 5.7, 6.0, 5.9, 5.1, 6.3, 6.6]

# Creating truncated vertical bar chart
fig, ax = plt.subplots(figsize=(10, 14))

ax.bar(categories, values, color=[
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
    '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
    '#bcbd22', '#17becf', '#1f77b4', '#ff7f0e'
], width=0.6)

# Adding labels and title
ax.set_ylabel('Score')
ax.set_title('Health & Psychology Indicators')

# Setting y-axis limits to truncate the chart
ax.set_ylim(4, 8)

# Show the plot
plt.show()