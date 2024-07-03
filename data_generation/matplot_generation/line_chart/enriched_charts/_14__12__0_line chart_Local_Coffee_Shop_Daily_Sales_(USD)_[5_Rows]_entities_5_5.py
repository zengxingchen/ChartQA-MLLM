
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
attendance = [200, 250, 220, 180, 150, 130, 110, 90, 80, 70, 60, 50]

# Plotting the line chart
plt.figure(figsize=(12, 6))  # Change width and height of the chart
plt.plot(months, attendance, marker='s', linestyle='--', color='#2ca02c', linewidth=2.5)  # Modify color scheme

# Adding title and labels
plt.title('Monthly Membership Decline in Fitness Club', fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Membership', fontsize=14)

# Adding an annotation for the lowest attendance
lowest_attendance_index = attendance.index(min(attendance))
lowest_attendance_month = months[lowest_attendance_index]
plt.annotate('Lowest Membership', xy=(lowest_attendance_index, min(attendance)), xytext=(lowest_attendance_index, min(attendance) + 30),
             arrowprops=dict(facecolor='#d62728', shrink=0.05))

# Add a grid, set axis ranges and show the plot
plt.grid(True)
plt.ylim(0, 300)
plt.gca().invert_yaxis()
plt.show()