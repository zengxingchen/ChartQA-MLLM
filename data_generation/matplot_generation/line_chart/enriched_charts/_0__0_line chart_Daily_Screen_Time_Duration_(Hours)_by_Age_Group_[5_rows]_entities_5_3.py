
import matplotlib.pyplot as plt

# Data points
days = [i for i in range(1, 31)]
calories_burned = [500, 520, 530, 515, 510, 505, 525, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750]

# Creating the line chart
plt.figure(figsize=(12, 6))  # Change the width and height of the chart
plt.plot(days, calories_burned, marker='o', color='#ff5733', label='Daily Calories Burned')  # Specific color code

# Annotation for the highest calorie burn day
plt.annotate('Peak', xy=(30, 750), xytext=(25, 700),
             arrowprops=dict(facecolor='#33ff57', shrink=0.05))

# Adding the x-axis label, y-axis label, title, legend, and grid
plt.xlabel('Day of the Month')
plt.ylabel('Calories Burned')
plt.title('Daily Calories Burned in June - 2023')
plt.legend()
plt.grid(True)

# Display the chart
plt.show()