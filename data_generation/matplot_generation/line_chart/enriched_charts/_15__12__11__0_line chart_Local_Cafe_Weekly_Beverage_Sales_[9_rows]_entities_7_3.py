
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
attendance = [40, 45, 50, 60, 70, 65, 60, 55, 60, 50, 45, 40]

plt.figure(figsize=(10, 8))

# Plotting the line chart
plt.plot(months, attendance, color="#4682B4", marker='o')

# Adding annotations for specific points
plt.annotate('Mid-Year Peak', xy=('May', 70), xytext=('March', 75),
             arrowprops=dict(facecolor='green', shrink=0.05),
             horizontalalignment='right')
plt.annotate('End-Year Decline', xy=('December', 40), xytext=('October', 35),
             arrowprops=dict(facecolor='red', shrink=0.05),
             horizontalalignment='right')

# Title and labels
plt.title('Monthly Attendance at the Community Center')
plt.xlabel('Month')
plt.ylabel('Attendance (people)')

# Invert the y-axis
plt.gca().invert_yaxis()

# Show the chart
plt.show()