
import matplotlib.pyplot as plt

# Data points
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
calories_burned = [300, 350, 400, 370, 450, 500, 480]
steps_taken = [7000, 8000, 8500, 7800, 9000, 10000, 9500]

# Mapped days to x-axis numerical values to plot
day_mapping = {day: i for i, day in enumerate(days)}
day_indices = [day_mapping[day] for day in days]

# Scatterplot
plt.figure(figsize=(14, 8))  # Modify the width and height of the chart
plt.scatter(day_indices, calories_burned, s=steps_taken, c='#1E90FF', alpha=0.6)  # Modify color using a specific color code
plt.scatter(day_indices, steps_taken, s=calories_burned, c='#32CD32', alpha=0.6)  # Add another set of data points

# Customizing the plot
plt.title('Calories Burned vs Steps Taken by Day', pad=20)
plt.xlabel('Day of the Week')
plt.ylabel('Count')
plt.xticks(day_indices, days)  # Set x-axis ticks to be the days of the week
plt.grid(True)

# Show plot
plt.show()