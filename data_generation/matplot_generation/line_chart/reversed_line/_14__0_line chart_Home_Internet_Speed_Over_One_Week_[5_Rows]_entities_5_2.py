
import matplotlib.pyplot as plt

# Data
months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]
average_attendance = [80, 85, 90, 95, 100, 110, 120, 115, 110, 105, 90, 85]
minimum_attendance = [50, 55, 60, 65, 70, 75, 80, 78, 75, 70, 65, 60]

# Create the plot
plt.figure(figsize=(14, 7))
plt.plot(months, average_attendance, color='#4CAF50', marker='o', label="Average Attendance")
plt.plot(months, minimum_attendance, color='#FF9800', marker='o', label="Minimum Attendance")

# Highlight Highest and Lowest Attendance
highest_attendance = max(average_attendance)
lowest_attendance = min(minimum_attendance)
highest_month = months[average_attendance.index(highest_attendance)]
lowest_month = months[minimum_attendance.index(lowest_attendance)]

plt.annotate(f'Highest\n{highest_attendance}', xy=(highest_month, highest_attendance), xytext=(highest_month, highest_attendance+5),
             arrowprops=dict(facecolor='black', shrink=0.05), ha='center')
plt.annotate(f'Lowest\n{lowest_attendance}', xy=(lowest_month, lowest_attendance), xytext=(lowest_month, lowest_attendance-5),
             arrowprops=dict(facecolor='black', shrink=0.05), ha='center')

# Customize rest of the chart
plt.title("Average and Minimum Attendance at Music Events")
plt.xlabel("Month")
plt.ylabel("Attendance")
plt.legend(loc='upper left')
plt.grid(True)
plt.gca().invert_yaxis()
plt.tight_layout()

# Show the plot
plt.show()