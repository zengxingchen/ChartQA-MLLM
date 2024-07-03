
import matplotlib.pyplot as plt

# Data
days = list(range(1, 31))
exercise_hours = [1.2, 1.5, 1.0, 1.8, 1.3, 2.0, 0.9, 2.1, 1.1, 2.2, 1.4, 1.7, 1.6, 1.9, 1.3, 2.3, 0.8, 2.0, 1.0, 2.4, 1.5, 1.2, 1.9, 1.7, 2.1, 1.6, 2.3, 1.0, 2.5, 1.1]
calories_burned = [250, 300, 220, 330, 270, 350, 200, 360, 240, 370, 290, 320, 310, 340, 260, 380, 190, 350, 230, 390, 300, 250, 340, 320, 360, 310, 380, 220, 400, 240]

# Scatter plot
plt.figure(figsize=(16, 10))  # Width: 16, Height: 10
plt.scatter(days, exercise_hours, color='#FF5733', label='Exercise Hours')  # Orange Red
plt.scatter(days, calories_burned, color='#1ABC9C', label='Calories Burned')  # Turquoise

# Customize the plot
plt.title('Exercise and Calorie Data Over a Month', pad=30)
plt.xlabel('Day')
plt.ylabel('Measurement')
plt.legend(loc='upper left')
plt.grid(True)

# Show the plot
plt.show()