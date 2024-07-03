
import matplotlib.pyplot as plt

# Data
days = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30
]
steps = [
    5000, 7000, 8000, 6000, 7500, 6800, 7200, 7900, 8500, 6200,
    7800, 9000, 8200, 7600, 8800, 6800, 7100, 8300, 9200, 7700,
    8000, 8500, 8700, 6500, 6900, 7100, 8400, 9200, 8100, 7800
]
calories_burned = [
    200, 300, 400, 250, 320, 280, 310, 350, 370, 260,
    340, 380, 360, 330, 390, 280, 300, 350, 410, 340,
    370, 390, 380, 270, 290, 310, 350, 410, 360, 340
]

# Map the calories burned to a color
calories_colors = [
    '#FF6666', '#FF9933', '#FFFF66', '#CCFF66', '#66FF66', '#66FFCC', '#66CCFF', '#6699FF', '#9966FF', '#FF66CC',
    '#FF6699', '#FF3333', '#FF3333', '#FFCC66', '#66FF99', '#33FFCC', '#33CCFF', '#3399FF', '#3366FF', '#3333FF',
    '#9966CC', '#9933FF', '#9933CC', '#CC6699', '#FF99CC', '#FF3399', '#FF6699', '#FF3366', '#FF9933', '#FF6600'
]

# Scatter plot
fig, ax = plt.subplots(figsize=(12, 8))
sc = ax.scatter(days, steps, s=[c // 2 for c in calories_burned], c=calories_colors, alpha=0.75)

# Customizing the axes and title
ax.set_xlabel('Day of the Month')
ax.set_ylabel('Steps Taken')
ax.set_title('Daily Steps and Calories Burned')
ax.grid(True)

# Show plot
plt.show()