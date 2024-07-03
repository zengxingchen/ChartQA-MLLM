
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
stress_levels = [20, 25, 30, 35, 40, 45, 50, 60, 55, 50, 45, 40]

plt.figure(figsize=(10, 8))  # Change width and height of the chart

# Plotting the line chart
plt.plot(months, stress_levels, color="#1f77b4", marker='s')  # Using a specific color code and marker for data points

# Adding annotations for specific points
plt.annotate('Exam Preparation', xy=('March', 30), xytext=('April', 33),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right')
plt.annotate('Vacation', xy=('August', 60), xytext=('July', 58),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='right')

# Title and labels
plt.title('Monthly Stress Levels of College Students')
plt.xlabel('Month')
plt.ylabel('Stress Level')

# Show the chart
plt.show()