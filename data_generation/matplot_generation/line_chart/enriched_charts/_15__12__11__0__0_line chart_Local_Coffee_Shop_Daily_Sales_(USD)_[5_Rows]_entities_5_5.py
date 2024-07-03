
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
gym_attendance = [800, 760, 780, 720, 690, 650, 640, 660, 710, 750, 790, 810]

# Plotting the line chart
plt.figure(figsize=(12, 8))  # Change width and height of the chart
plt.plot(months, gym_attendance, marker='o', linestyle='-', color='#4682B4', linewidth=2.5)  # Modify color scheme

# Adding title and labels
plt.title('Monthly Gym Attendance in 2023', fontsize=22, pad=20)
plt.xlabel('Month', fontsize=16)
plt.ylabel('Gym Attendance', fontsize=16)

# Adding an annotation for the highest gym attendance
highest_attendance_index = gym_attendance.index(max(gym_attendance))
highest_attendance_month = months[highest_attendance_index]
plt.annotate('Peak Attendance', xy=(highest_attendance_index, max(gym_attendance)), xytext=(highest_attendance_index, max(gym_attendance) + 20),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05))

# Add a grid, set axis ranges, invert y-axis, and show the plot
plt.grid(True)
plt.ylim(850, 600)
plt.gca().invert_yaxis()
plt.show()