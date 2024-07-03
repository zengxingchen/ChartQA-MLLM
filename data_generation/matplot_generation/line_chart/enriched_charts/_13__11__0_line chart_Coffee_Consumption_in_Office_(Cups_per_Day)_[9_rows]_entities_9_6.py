
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
temperatures = [5, 3, 8, 12, 15, 20, 25, 30, 28, 22, 15, 10]

plt.figure(figsize=(14, 8))  # Adjust width and height of the chart
plt.plot(months, temperatures, marker='o', linestyle='-', color='#1f77b4')  # Specific hex color

# Annotation for the highest temperature
plt.annotate('Peak Temperature', xy=('August', 30), xytext=('September', 32),
             arrowprops=dict(facecolor='#ff7f0e', shrink=0.05))

# Adding labels and title
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.title('Monthly Average Temperature Over a Year')

# Showing the plot
plt.show()