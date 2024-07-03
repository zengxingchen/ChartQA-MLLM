
import matplotlib.pyplot as plt

# Data points
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
visitors_to_food_festival = [120, 150, 180, 170, 230, 310, 290]
food_items_sold = [40, 45, 50, 48, 60, 80, 75]

# Mapped days to x-axis numerical values to plot
day_mapping = {day: i for i, day in enumerate(days)}
day_indices = [day_mapping[day] for day in days]

# Scatterplot
plt.figure(figsize=(14, 7))  # Modify the width and height of the chart
plt.scatter(day_indices, visitors_to_food_festival, s=food_items_sold, c='#8A2BE2', alpha=0.7)
plt.scatter(day_indices, food_items_sold, s=visitors_to_food_festival, c='#FFD700', alpha=0.7)

# Customizing the plot
plt.title('Visitors to Food Festival vs Food Items Sold by Day', pad=20)
plt.xlabel('Day of the Week')
plt.ylabel('Count')
plt.xticks(day_indices, days)  # Set x-axis ticks to be the days of the week
plt.grid(True)

# Show plot
plt.show()