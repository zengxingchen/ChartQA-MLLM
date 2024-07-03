
import matplotlib.pyplot as plt

# Data points
dates = ["January", "February", "March", "April", "May", "June",
         "July", "August", "September", "October", "November", "December"]
temperatures = [5, 6, 10, 15, 20, 25, 30, 28, 22, 16, 10, 6]

plt.figure(figsize=(14, 8))  # Adjust width and height of the chart
plt.plot(dates, temperatures, marker='o', linestyle='-', color='#3498db')  # Specific hex color

# Annotation for the highest temperature
plt.annotate('Peak Temperature', xy=('July', 30), xytext=('September', 32),
             arrowprops=dict(facecolor='#e74c3c', shrink=0.05))

# Adding labels and title
plt.xlabel('Month')
plt.ylabel('Average Temperature (°C)')
plt.title('Average Monthly Temperature in 2023')

# Showing the plot
plt.show()