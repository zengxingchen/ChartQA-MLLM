
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
distances = [50, 55, 60, 70, 80, 90, 85, 75, 65, 60, 55, 50]

plt.figure(figsize=(12, 8))  # Adjust width and height of the chart
plt.plot(months, distances, marker='o', linestyle='-', color='#33a02c')  # Specific hex color

# Annotation for the highest distance
plt.annotate('Longest run', xy=('June', 90), xytext=('July', 95),
             arrowprops=dict(facecolor='#ff7f00', shrink=0.05))

# Adding labels and title
plt.xlabel('Month')
plt.ylabel('Average Distance Run (km)')
plt.title('Average Monthly Running Distance')

# Invert y-axis
plt.gca().invert_yaxis()

# Showing the plot
plt.show()