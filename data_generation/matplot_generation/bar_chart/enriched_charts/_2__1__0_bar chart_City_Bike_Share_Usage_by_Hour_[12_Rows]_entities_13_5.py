
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
attendance = [500, 450, 600, 550, 700, 750, 800, 770, 720, 680, 650, 630]

# Colors for each bar
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6','#c4e17f','#76d7c4','#f7c6c7','#ffcc99','#ffb6c1','#c1e1c1']

# Plotting the bar chart horizontally
plt.figure(figsize=(12, 8))  # Change width and height of the chart
plt.barh(months, attendance, color=colors, edgecolor='black', height=0.6)  # Change height for bars and apply color scheme

# Chart title and labels
plt.title('Monthly Gym Attendance', fontsize=18)
plt.xlabel('Number of Attendees', fontsize=14)

# Setting the xlim to provide better clarity for attendance values
plt.xlim(0, max(attendance) + 100)

# Display the chart
plt.tight_layout()
plt.show()