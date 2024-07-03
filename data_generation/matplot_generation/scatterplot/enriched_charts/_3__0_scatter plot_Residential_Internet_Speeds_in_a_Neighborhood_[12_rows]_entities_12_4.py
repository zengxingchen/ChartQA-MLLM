
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
average_workout_duration = [30, 32, 35, 40, 45, 50, 55, 54, 48, 42, 38, 34]
gym_attendance = [150, 160, 180, 220, 260, 300, 340, 330, 270, 230, 200, 170]

# Convert month names to numbers for plotting
month_numbers = [i+1 for i, _ in enumerate(months)]

# Scatter plot
plt.figure(figsize=(12, 6))  # Change the size of the plot
plt.scatter(month_numbers, average_workout_duration, c=['#FF5733', '#33FF57', '#3357FF', '#FF33A6',
                                                       '#A633FF', '#33FFF7', '#FFC733', '#33FFA6',
                                                       '#A6FF33', '#FF3333', '#33A6FF', '#5733FF'],
            s=gym_attendance, alpha=0.7)  # Size corresponds to gym attendance, improved color scheme

# Customize the axes
plt.xticks(month_numbers, months, rotation=45)
plt.xlabel('Month')
plt.ylabel('Average Workout Duration (Minutes)')
plt.title('Monthly Gym Attendance vs. Average Workout Duration')
plt.xlim(0, 13)  # Set the limit to include all months

# Show the plot
plt.tight_layout()  # Adjust layout to fit the figure neatly
plt.show()