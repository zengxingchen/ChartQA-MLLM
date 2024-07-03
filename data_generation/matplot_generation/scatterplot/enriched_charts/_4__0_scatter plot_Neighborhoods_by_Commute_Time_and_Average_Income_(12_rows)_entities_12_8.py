
import matplotlib.pyplot as plt

# Data points
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday",
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
calories_burned = [220, 250, 200, 270, 300, 350, 320, 240, 260, 210, 280, 310, 360, 330]
steps_taken = [3000, 3500, 2800, 3800, 4200, 5000, 4600, 3100, 3700, 2900, 3900, 4300, 5200, 4700]

# Mapped days to x-axis numerical values to plot
day_mapping = {day: i for i, day in enumerate(days)}
day_indices = [day_mapping[day] for day in days]

# Scatterplot
plt.figure(figsize=(12, 6))  # Modify the width and height of the chart
plt.scatter(day_indices, calories_burned, s=[steps / 10 for steps in steps_taken], c='#FF6347', alpha=0.6)  # Modify color using a specific color code
plt.scatter(day_indices, steps_taken, s=[calories / 2 for calories in calories_burned], c='#4682B4', alpha=0.6)  # Add another set of data points

# Customizing the plot
plt.title('Calories Burned vs Steps Taken (Counts by Day)', pad=20)
plt.xlabel('Day of the Week')
plt.ylabel('Count')
plt.xticks(day_indices, days)  # Set x-axis ticks to be the days of the week
plt.grid(True)

# Show plot
plt.show()