
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
pollution_index = [80, 75, 85, 70, 65, 60, 55, 50, 45, 40, 35, 30]

plt.figure(figsize=(12, 7))  # Adjust width and height of the chart
plt.plot(months, pollution_index, marker='o', linestyle='-', color='#FF5733')  # Specific hex color

# Annotation for a significant drop
plt.annotate('Significant Drop', xy=('September', 45), xytext=('June', 90),
             arrowprops=dict(facecolor='#33FF57', shrink=0.05))

# Adding labels and title
plt.xlabel('Month')
plt.ylabel('Pollution Index')
plt.title('Monthly Pollution Index in 2023', pad=20)

# Invert Y axis
plt.gca().invert_yaxis()

# Showing the plot
plt.show()