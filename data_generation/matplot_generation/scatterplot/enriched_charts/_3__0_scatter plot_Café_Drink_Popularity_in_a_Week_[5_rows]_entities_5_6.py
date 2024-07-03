
import matplotlib.pyplot as plt

# Data
days = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30
]
exercise_duration = [
    30, 45, 20, 50, 60, 10, 40, 35, 50, 55,
    30, 45, 20, 50, 60, 10, 40, 35, 50, 55,
    30, 45, 20, 50, 60, 10, 40, 35, 50, 55
]
stress_level = [
    40, 35, 50, 30, 25, 70, 45, 55, 30, 28,
    42, 38, 53, 32, 22, 75, 40, 50, 27, 26,
    45, 33, 60, 29, 20, 80, 43, 52, 28, 25
]

# Map the exercise duration to a color
exercise_colors = [
    '#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#57FF33',
    '#FF8333', '#8333FF', '#33FF83', '#FF3385', '#3385FF',
    '#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#57FF33',
    '#FF8333', '#8333FF', '#33FF83', '#FF3385', '#3385FF',
    '#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#57FF33',
    '#FF8333', '#8333FF', '#33FF83', '#FF3385', '#3385FF'
]

# Scatter plot
fig, ax = plt.subplots(figsize=(12, 7))  # Changed width and height
sc = ax.scatter(days, exercise_duration, s=[s + 10 for s in stress_level], c=exercise_colors, alpha=0.75)

# Customizing the axes and title
ax.set_xlabel('Day of the Month')
ax.set_ylabel('Exercise Duration (mins)')
ax.set_title('Daily Exercise Duration and Stress Levels')
ax.grid(True)

# Show plot
plt.show()