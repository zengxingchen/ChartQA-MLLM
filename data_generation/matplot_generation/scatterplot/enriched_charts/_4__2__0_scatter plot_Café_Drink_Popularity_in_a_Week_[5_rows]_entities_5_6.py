
import matplotlib.pyplot as plt

# Data
days = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31
]
pages_read = [
    20, 35, 45, 25, 40, 30, 50, 55, 60, 35,
    45, 50, 65, 55, 70, 60, 40, 50, 65, 75,
    45, 50, 55, 40, 35, 45, 55, 60, 65, 70, 75
]
focus_level = [
    50, 60, 70, 55, 65, 50, 80, 85, 90, 55,
    70, 80, 95, 85, 100, 90, 60, 80, 95, 100,
    70, 80, 85, 60, 55, 70, 85, 90, 95, 100, 100
]

# Map the focus level to a color
focus_colors = [
    '#FF5733', '#FF8D1A', '#FFC300', '#DAF7A6', '#33FF57', '#33FFBD', '#33D4FF', '#3383FF', '#7033FF', '#FF33C8',
    '#FF5733', '#FF8D1A', '#FFC300', '#DAF7A6', '#33FF57', '#33FFBD', '#33D4FF', '#3383FF', '#7033FF', '#FF33C8',
    '#FF5733', '#FF8D1A', '#FFC300', '#DAF7A6', '#33FF57', '#33FFBD', '#33D4FF', '#3383FF', '#7033FF', '#FF33C8',
    '#FF5733'
]

# Scatter plot
fig, ax = plt.subplots(figsize=(14, 9))
sc = ax.scatter(days, pages_read, s=[f // 2 for f in focus_level], c=focus_colors, alpha=0.75)

# Customizing the axes and title
ax.set_xlabel('Day of the Month')
ax.set_ylabel('Pages Read')
ax.set_title('Daily Reading and Focus Levels')
ax.grid(True)

# Show plot
plt.show()