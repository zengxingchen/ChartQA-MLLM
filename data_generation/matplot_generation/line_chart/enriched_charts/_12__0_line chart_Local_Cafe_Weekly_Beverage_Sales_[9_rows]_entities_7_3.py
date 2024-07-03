
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
calories = [2500, 2450, 2600, 2700, 2800, 3000, 3200, 3100, 2900, 2750, 2600, 2550]

plt.figure(figsize=(14, 7))

# Plotting the line chart
plt.plot(months, calories, color="#1E90FF", marker='s')  # Using a specific color code and marker for data points

# Adding annotations for specific points
plt.annotate('Calorie peak', xy=('July', 3200), xytext=('June', 3300),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right')
plt.annotate('Post-peak drop', xy=('August', 3100), xytext=('September', 3300),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right')

# Title and labels
plt.title('Average Monthly Calorie Intake in City X')
plt.xlabel('Month')
plt.ylabel('Calories')

# Show the chart
plt.show()