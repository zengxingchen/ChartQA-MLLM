
import matplotlib.pyplot as plt

# Data
weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
running_distance = [5.2, 6.1, 7.0, 6.5, 7.2, 8.0, 7.5, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5]
calories_burned = [350, 420, 450, 400, 460, 500, 480, 520, 550, 570, 600, 620, 650, 680, 700, 720, 750, 780, 800, 820]

# Scatter plot
plt.figure(figsize=(16, 10))
plt.scatter(weeks, running_distance, color='#FF6347', label='Running Distance (km)')  # Tomato
plt.scatter(weeks, calories_burned, color='#4682B4', label='Calories Burned')  # Steel Blue

# Customize the plot
plt.title('Weekly Running Distance and Calories Burned Over 20 Weeks', pad=20)
plt.xlabel('Week')
plt.ylabel('Count')
plt.legend(loc='upper left')
plt.grid(True)

# Show the plot
plt.show()