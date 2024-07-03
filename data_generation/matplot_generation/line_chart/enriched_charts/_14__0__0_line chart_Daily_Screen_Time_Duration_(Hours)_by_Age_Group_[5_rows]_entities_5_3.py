
import matplotlib.pyplot as plt

# Data points
days = [i for i in range(1, 31)]
calories_burned = [750, 740, 730, 720, 710, 700, 690, 680, 670, 660, 650, 640, 630, 620, 610, 600, 590, 580, 570, 560, 550, 540, 530, 520, 510, 505, 515, 525, 520, 500]

# Creating the line chart
plt.figure(figsize=(10, 8))  # Change the width and height of the chart
plt.plot(days, calories_burned, marker='o', color='#4287f5', label='Calories Burned Daily')  # Specific color code

# Annotation for a significant data point
plt.annotate('Lowest Point', xy=(30, 500), xytext=(25, 530),
             arrowprops=dict(facecolor='#f54291', shrink=0.05))

# Adding the x-axis label, y-axis label, title, legend, and grid
plt.xlabel('Day of the Month')
plt.ylabel('Calories Burned')
plt.title('Daily Calories Burned in June - 2023', pad=20)
plt.legend(loc='upper right')
plt.grid(True)
plt.gca().invert_yaxis()  # Invert the y-axis

# Display the chart
plt.show()