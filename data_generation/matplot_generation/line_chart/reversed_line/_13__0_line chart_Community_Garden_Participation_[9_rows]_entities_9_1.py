
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]
attendance = [100, 120, 150, 200, 180, 160, 140, 130, 110, 90, 70, 60]

plt.figure(figsize=(14, 7))  # Changing width and height of the chart
plt.plot(months, attendance, marker='o', color='#2E86C1', linewidth=2)  # Modified color scheme

# Adding annotations for the highest and lowest attendance months
plt.annotate('Lowest Attendance', xy=(11, 60), xytext=(10, 50),
             arrowprops=dict(facecolor='#E74C3C', shrink=0.05))
plt.annotate('Highest Attendance', xy=(3, 200), xytext=(4, 210),
             arrowprops=dict(facecolor='#27AE60', shrink=0.05))

plt.title('Monthly Gym Attendance')  # New headline which fits the topic
plt.xlabel('Month')  # Changing labels to fit the new data type
plt.ylabel('Attendance')
plt.grid(True)

plt.show()