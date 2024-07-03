
import matplotlib.pyplot as plt

# Data points
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
visitors_to_art_gallery = [150, 170, 200, 190, 250, 300, 280]
books_sold = [30, 35, 40, 38, 50, 60, 55]

# Mapped days to x-axis numerical values to plot
day_mapping = {day: i for i, day in enumerate(days)}
day_indices = [day_mapping[day] for day in days]

# Scatterplot
plt.figure(figsize=(12, 6))  # Modify the width and height of the chart
plt.scatter(day_indices, visitors_to_art_gallery, s=books_sold, c='#FF6347', alpha=0.6)  # Modify color using a specific color code
plt.scatter(day_indices, books_sold, s=visitors_to_art_gallery, c='#4682B4', alpha=0.6)  # Add another set of data points

# Customizing the plot
plt.title('Visitors to Art Gallery vs Books Sold by Day', pad=20)
plt.xlabel('Day of the Week')
plt.ylabel('Count')
plt.xticks(day_indices, days)  # Set x-axis ticks to be the days of the week
plt.grid(True)

# Show plot
plt.show()