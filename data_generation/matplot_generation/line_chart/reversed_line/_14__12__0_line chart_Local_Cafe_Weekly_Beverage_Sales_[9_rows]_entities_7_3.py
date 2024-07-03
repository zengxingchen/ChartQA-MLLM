
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
calories = [3200, 3100, 3000, 2900, 2800, 2700, 2600, 2500, 2400, 2300, 2200, 2100]

plt.figure(figsize=(10, 5))

# Plotting the line chart
plt.plot(months, calories, color="#FF4500", marker='o')  # Using a specific color code and marker for data points

# Adding annotations for specific points
plt.annotate('Calorie peak', xy=('January', 3200), xytext=('February', 3300),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right')
plt.annotate('Post-peak drop', xy=('February', 3100), xytext=('March', 3200),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right')

# Title and labels
plt.title('Monthly Calorie Intake Decrease in City X')
plt.xlabel('Month')
plt.ylabel('Calories')

# Invert the y-axis
plt.gca().invert_yaxis()

# Show the chart
plt.show()