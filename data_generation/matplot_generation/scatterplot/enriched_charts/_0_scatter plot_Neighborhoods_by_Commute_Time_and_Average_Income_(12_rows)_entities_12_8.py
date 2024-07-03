
import matplotlib.pyplot as plt

# Data points
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
temperature = [72, 68, 75, 70, 77, 82, 80]
ice_creams_sold = [82, 76, 96, 80, 104, 135, 121]

# Mapped days to x-axis numerical values to plot
day_mapping = {day: i for i, day in enumerate(days)}
day_indices = [day_mapping[day] for day in days]

# Scatterplot
plt.figure(figsize=(10, 5))  # Modify the width and height of the chart
plt.scatter(day_indices, temperature, s=ice_creams_sold, c='#FFA07A', alpha=0.5)  # Modify color using a specific color code
plt.scatter(day_indices, ice_creams_sold, s=temperature, c='#20B2AA', alpha=0.5)  # Add another set of data points

# Customizing the plot
plt.title('Temperature vs Ice Creams Sold (Counts by Day)')
plt.xlabel('Day of the Week')
plt.ylabel('Count')
plt.xticks(day_indices, days)  # Set x-axis ticks to be the days of the week
plt.grid(True)

# Show plot
plt.show()