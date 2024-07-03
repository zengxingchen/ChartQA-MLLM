
import matplotlib.pyplot as plt

# Data points
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
running_distance = [5.0, 6.2, 5.8, 6.5, 7.0, 8.0, 7.5]
running_time = [30, 35, 32, 40, 45, 50, 48]

# Mapped days to x-axis numerical values to plot
day_mapping = {day: i for i, day in enumerate(days)}
day_indices = [day_mapping[day] for day in days]

# Scatterplot
plt.figure(figsize=(16, 10))  # Modify the width and height of the chart
plt.scatter(day_indices, running_distance, s=running_time, c='#FF4500', alpha=0.6)  # Modify color using a specific color code
plt.scatter(day_indices, running_time, s=[d*10 for d in running_distance], c='#4682B4', alpha=0.6)  # Add another set of data points

# Customizing the plot
plt.title('Running Distance vs Running Time by Day', pad=20)
plt.xlabel('Day of the Week')
plt.ylabel('Value')
plt.xticks(day_indices, days)  # Set x-axis ticks to be the days of the week
plt.grid(True)
plt.legend(['Distance (km)', 'Time (minutes)'], loc='upper left')

# Show plot
plt.show()