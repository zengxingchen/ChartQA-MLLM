
import matplotlib.pyplot as plt

# Data
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
caloric_intake = [2200, 2300, 2100, 2400, 2250, 2350, 2150, 2500, 2450, 2300]
calories_burned = [2500, 2450, 2550, 2600, 2700, 2750, 2650, 2800, 2850, 2900]

# Scatter plot
plt.figure(figsize=(14, 8))  # Width: 14, Height: 8
plt.scatter(days, caloric_intake, color='#FF4500', label='Caloric Intake')  # OrangeRed
plt.scatter(days, calories_burned, color='#1E90FF', label='Calories Burned')  # DodgerBlue

# Customize the plot
plt.title('Daily Caloric Intake vs. Calories Burned Over 10 Days', pad=20)
plt.xlabel('Day')
plt.ylabel('Calories')
plt.legend(loc='lower right')
plt.grid(True)

# Show the plot
plt.show()