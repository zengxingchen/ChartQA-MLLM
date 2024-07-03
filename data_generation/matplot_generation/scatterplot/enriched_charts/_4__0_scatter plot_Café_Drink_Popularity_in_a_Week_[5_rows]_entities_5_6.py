
import matplotlib.pyplot as plt

# Data
days = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30
]
exercise_duration = [
    30, 45, 50, 60, 55, 40, 35, 50, 55, 60,
    70, 80, 75, 65, 60, 45, 50, 55, 60, 70,
    75, 80, 85, 90, 95, 100, 90, 80, 75, 70
]
happiness_level = [
    75, 80, 78, 82, 79, 77, 74, 81, 85, 87,
    90, 92, 91, 89, 88, 84, 83, 86, 88, 91,
    92, 93, 95, 97, 98, 99, 96, 93, 91, 90
]

# Map the exercise duration to a color
exercise_colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
]

# Scatter plot
fig, ax = plt.subplots(figsize=(12, 8))
sc = ax.scatter(days, exercise_duration, s=[h + 10 for h in happiness_level], c=exercise_colors, alpha=0.75)

# Customizing the axes and title
ax.set_xlabel('Day of the Month')
ax.set_ylabel('Exercise Duration (minutes)')
ax.set_title('Daily Exercise Duration and Happiness Levels', pad=20)
ax.grid(True)

# Show plot
plt.show()