
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
attendance = [550, 470, 620, 580, 710, 760, 810, 780, 730, 690, 660, 640]

# Colors for each bar
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#FF8C33', '#8C33FF', '#33FFC1', '#FF3333', '#33FF8C', '#5733FF', '#33A6FF', '#A633FF']

# Plotting the bar chart vertically
plt.figure(figsize=(14, 10))  # Change width and height of the chart
plt.bar(months, attendance, color=colors, edgecolor='black', width=0.5)  # Change width for bars and apply color scheme

# Chart title and labels
plt.title('Monthly Gym Attendance', fontsize=20)
plt.ylabel('Number of Attendees', fontsize=16)

# Setting the ylim to provide better clarity for attendance values
plt.ylim(0, max(attendance) + 100)

# Display the chart
plt.tight_layout()
plt.show()