
import matplotlib.pyplot as plt

# Data points
weeks = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6",
         "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12",
         "Week 13", "Week 14", "Week 15", "Week 16"]
steps = [12000, 11500, 11000, 10500, 10000, 9500, 9000, 8500, 8000, 7500, 7000, 6500, 6000, 5500, 5000, 4500]

plt.figure(figsize=(10, 6))  # Adjust width and height of the chart
plt.plot(weeks, steps, marker='o', linestyle='-', color='#1E90FF')  # Specific hex color

# Annotation for the lowest step count
plt.annotate('Lowest Activity', xy=('Week 16', 4500), xytext=('Week 15', 3500),
             arrowprops=dict(facecolor='#FF6347', shrink=0.05))

# Adding labels and title
plt.xlabel('Week')
plt.ylabel('Energy Consumption (kJ)')
plt.title('Weekly Energy Consumption Over 16 Weeks')

# Invert the y-axis
plt.gca().invert_yaxis()

# Showing the plot
plt.show()