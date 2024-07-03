
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
exercise_hours = [30, 32, 34, 36, 38, 40, 42, 44, 43, 41, 39, 37]

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(months, exercise_hours, marker='o', linestyle='-', color='#32CD32')

# Annotate the highest and lowest exercise hour points
plt.annotate('Highest\n44', xy=('August', 44), xytext=('July', 45),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05), color='#FF4500')
plt.annotate('Lowest\n30', xy=('January', 30), xytext=('February', 28),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05), color='#FF4500')

# Title and labels
plt.title('Monthly Average Exercise Hours in 2023', pad=20)
plt.xlabel('Month')
plt.ylabel('Exercise Hours')

# Customize the grid
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Invert y-axis
plt.gca().invert_yaxis()

# Show the plot
plt.show()