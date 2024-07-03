
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
distances = [5, 8, 12, 15, 18, 22, 26, 28, 25, 20, 15, 10]

plt.figure(figsize=(12, 7))  # Adjust width and height of the chart
plt.plot(months, distances, marker='o', linestyle='-', color='#ff4500')  # Specific hex color

# Annotation for the highest running distance
plt.annotate('Peak Distance', xy=('August', 28), xytext=('September', 30),
             arrowprops=dict(facecolor='#32cd32', shrink=0.05))

# Adding labels and title
plt.xlabel('Month')
plt.ylabel('Running Distance (km)')
plt.title('Monthly Running Distance Over a Year')

# Showing the plot
plt.show()