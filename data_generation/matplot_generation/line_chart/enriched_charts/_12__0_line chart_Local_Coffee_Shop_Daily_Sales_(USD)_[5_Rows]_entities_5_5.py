
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
attendance = [150, 180, 220, 300, 350, 420, 470, 430, 360, 300, 250, 200]

# Plotting the line chart
plt.figure(figsize=(14, 7))  # Change width and height of the chart
plt.plot(months, attendance, marker='o', linestyle='-', color='#d9534f', linewidth=2.5)  # Modify color scheme

# Adding title and labels
plt.title('Monthly Attendance in the Community Center', fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Attendance', fontsize=14)

# Adding an annotation for the highest attendance
highest_attendance_index = attendance.index(max(attendance))
highest_attendance_month = months[highest_attendance_index]
plt.annotate('Peak Attendance', xy=(highest_attendance_index, max(attendance)), xytext=(highest_attendance_index, max(attendance) + 50),
             arrowprops=dict(facecolor='#5bc0de', shrink=0.05))

# Add a grid, set axis ranges and show the plot
plt.grid(True)
plt.ylim(100, 500)
plt.show()