
import matplotlib.pyplot as plt

# Data points
weeks = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6",
         "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12",
         "Week 13", "Week 14", "Week 15", "Week 16"]
steps = [3000, 4500, 5000, 6500, 7000, 8500, 9000, 10500, 12000, 11500, 11000, 9500, 8000, 7000, 6500, 6000]

plt.figure(figsize=(12, 8))  # Adjust width and height of the chart
plt.plot(weeks, steps, marker='s', linestyle='--', color='#8A2BE2')  # Specific hex color

# Annotation for the highest step count
plt.annotate('Peak Activity', xy=('Week 9', 12000), xytext=('Week 10', 13000),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05))

# Adding labels and title
plt.xlabel('Week')
plt.ylabel('Steps Taken')
plt.title('Weekly Step Count Over 16 Weeks')

# Showing the plot
plt.show()