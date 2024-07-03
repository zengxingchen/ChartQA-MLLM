
import matplotlib.pyplot as plt

# Data points
weeks = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6",
         "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12",
         "Week 13", "Week 14", "Week 15", "Week 16"]
fruit_consumption = [16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

plt.figure(figsize=(10, 6))  # Adjust width and height of the chart
plt.plot(weeks, fruit_consumption, marker='o', linestyle='-', color='#2E8B57')  # Specific hex color

# Annotation for the highest step count
plt.annotate('Peak Consumption', xy=('Week 1', 16), xytext=('Week 3', 17),
             arrowprops=dict(facecolor='#FF6347', shrink=0.05))

# Adding labels and title
plt.xlabel('Week')
plt.ylabel('Fruit Consumption (Servings)')
plt.title('Weekly Fruit Consumption Over 16 Weeks', pad=20)

# Invert the y-axis
plt.gca().invert_yaxis()

# Showing the plot
plt.show()