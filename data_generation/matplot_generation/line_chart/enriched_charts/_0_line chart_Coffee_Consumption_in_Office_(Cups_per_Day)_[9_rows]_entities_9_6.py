
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
temperatures = [5, 6, 10, 15, 20, 25, 30, 28, 24, 18, 12, 7]

plt.figure(figsize=(10, 6))  # Adjust width and height of the chart
plt.plot(months, temperatures, marker='o', linestyle='-', color='#007acc')  # Specific hex color

# Annotation for the highest temperature
plt.annotate('Hottest day', xy=('July', 30), xytext=('August', 32),
             arrowprops=dict(facecolor='#ff5733', shrink=0.05))

# Adding labels and title
plt.xlabel('Month')
plt.ylabel('Average Temperature (°C)')
plt.title('Average Monthly Temperatures')

# Showing the plot
plt.show()