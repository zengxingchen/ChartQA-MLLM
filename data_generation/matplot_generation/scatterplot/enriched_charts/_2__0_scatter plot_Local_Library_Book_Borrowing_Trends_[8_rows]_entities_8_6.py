
import matplotlib.pyplot as plt

# Data for scatterplot
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
average_sleep_hours = [6.5, 7, 6, 7.5, 8, 7, 6.5, 7.5, 8, 7, 6, 6.5]
daily_caffeine_intake_mg = [200, 180, 210, 160, 150, 170, 220, 140, 130, 200, 230, 210]
stress_level = [5, 4, 6, 3, 2, 4, 5, 2, 1, 3, 6, 5]

# Size of each point will be proportional to the stress level
sizes = [stress * 30 for stress in stress_level]

# Different colors for different caffeine intake levels
colors = ['#FF7F50', '#FFD700', '#FFA500', '#9ACD32', '#89CFF0', '#7BB8FA',
          '#6495ED', '#CD5C5C', '#F08080', '#8B0000', '#FF8C00', '#FF4500']

# Create scatterplot
plt.figure(figsize=(14, 10))  # increase the width and height of the chart
plt.scatter(months, average_sleep_hours, s=sizes, c=colors, alpha=0.7)

# Chart details
plt.title('Monthly Sleep Patterns and Caffeine Intake')
plt.xlabel('Month')
plt.ylabel('Average Sleep Hours')
plt.grid(True)

# Show the chart
plt.show()