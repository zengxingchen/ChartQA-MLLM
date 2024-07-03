
import matplotlib.pyplot as plt

# Data
countries = [
    "Finland", "Denmark", "Switzerland", "Iceland", "Netherlands",
    "Norway", "Sweden", "Luxembourg", "New Zealand", "Austria",
    "Australia", "Canada"
]
happiness_scores = [7.84, 7.62, 7.57, 7.55, 7.46, 7.39, 7.36, 7.32, 7.27, 7.24, 7.22, 7.12]

# Creating truncated bar chart
fig, ax = plt.subplots(figsize=(10, 6))  # Change the width and height of the chart

ax.bar(countries, happiness_scores, color=[
    '#4CAF50', '#FF9800', '#F44336', '#2196F3',
    '#9C27B0', '#FFEB3B', '#00BCD4', '#795548',
    '#8BC34A', '#CDDC39', '#FFC107', '#FF5722'
], width=0.4)  # Change bar color and width

# Adding labels and title
ax.set_ylabel('Happiness Score')
ax.set_title('Happiness Scores by Country')
ax.set_ylim(7.0, 8.0)  # Truncate y-axis to start from 7.0

# Show the plot
plt.show()