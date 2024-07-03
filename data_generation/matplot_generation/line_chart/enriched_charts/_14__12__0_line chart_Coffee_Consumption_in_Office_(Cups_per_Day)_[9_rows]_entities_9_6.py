
import matplotlib.pyplot as plt

# Data points
weeks = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6",
         "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12",
         "Week 13", "Week 14", "Week 15", "Week 16"]
values = [10000, 12000, 15000, 14000, 13000, 12500, 13500, 14500, 16000, 17000, 15500, 16500, 17500, 19000, 18500, 18000]

plt.figure(figsize=(14, 10))  # Adjust width and height of the chart
plt.plot(weeks, values, marker='o', linestyle='-', color='#1E90FF')  # Specific hex color

# Annotation for the highest value
plt.annotate('Peak Performance', xy=('Week 14', 19000), xytext=('Week 15', 20000),
             arrowprops=dict(facecolor='#32CD32', shrink=0.05))

# Adding labels and title
plt.xlabel('Week')
plt.ylabel('Hours Studied')
plt.title('Weekly Study Hours Over 16 Weeks')

# Invert the y-axis
plt.gca().invert_yaxis()

# Showing the plot
plt.show()