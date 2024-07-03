
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
revenue = [200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420]

plt.figure(figsize=(10, 6))  # Adjust width and height of the chart
plt.plot(months, revenue, marker='o', linestyle='-', color='#1e90ff')  # Specific hex color

# Annotation for the highest revenue
plt.annotate('Peak Revenue', xy=('December', 420), xytext=('November', 440),
             arrowprops=dict(facecolor='#ff6347', shrink=0.05))

# Adding labels and title
plt.xlabel('Month')
plt.ylabel('Revenue (Thousands of $)')
plt.title('Monthly Revenue Over a Year')

# Invert Y axis
plt.gca().invert_yaxis()

# Showing the plot
plt.show()