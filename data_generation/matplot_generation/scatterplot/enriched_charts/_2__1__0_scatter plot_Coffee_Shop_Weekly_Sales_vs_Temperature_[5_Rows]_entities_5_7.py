
import matplotlib.pyplot as plt

# Data
weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
attendance = [50, 60, 70, 55, 65, 80, 75, 85, 90, 95, 100, 110, 105, 115, 120, 125, 130, 135, 140, 145]
hours = [4, 5, 6, 4.5, 5.5, 6.5, 5.8, 6.9, 7, 7.2, 7.5, 8, 7.8, 8.3, 8.5, 8.7, 9, 9.2, 9.5, 9.8]

# Scatter plot
plt.figure(figsize=(14, 8))
plt.scatter(weeks, attendance, color='#8A2BE2', label='Attendance')  # Blue Violet
plt.scatter(weeks, hours, color='#7FFF00', label='Study Hours')  # Chartreuse

# Customize the plot
plt.title('Weekly Attendance and Study Hours Over 20 Weeks', pad=20)
plt.xlabel('Week')
plt.ylabel('Count')
plt.legend(loc='upper right')
plt.grid(True)

# Show the plot
plt.show()