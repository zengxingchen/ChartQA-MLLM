
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
rainfall = [80, 60, 70, 100, 130, 160, 200, 190, 150, 110, 90, 85]

plt.figure(figsize=(12, 7))  # Adjust width and height of the chart
plt.plot(months, rainfall, marker='s', linestyle='--', color='#e74c3c')  # Specific hex color

# Annotation for the highest rainfall
plt.annotate('Peak Rainfall', xy=('July', 200), xytext=('September', 220),
             arrowprops=dict(facecolor='#2ecc71', shrink=0.05))

# Adding labels and title
plt.xlabel('Month')
plt.ylabel('Average Rainfall (mm)')
plt.title('Average Monthly Rainfall in 2023')

# Showing the plot
plt.show()