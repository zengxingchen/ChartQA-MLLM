
import matplotlib.pyplot as plt

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
average_step_count = [5000, 5200, 4800, 5300, 5600, 5500, 5400, 5700, 5900, 6100, 6200, 5800]
average_screen_time = [300, 310, 320, 295, 310, 330, 290, 315, 305, 320, 310, 300]

# Create the plot
plt.figure(figsize=(14, 8))
plt.plot(months, average_step_count, color='#1f77b4', marker='o', label="Average Step Count")
plt.plot(months, average_screen_time, color='#ff7f0e', marker='o', label="Average Screen Time (minutes)")

# Highlight Highest and Lowest Intakes
highest_steps = max(average_step_count)
lowest_screen_time = min(average_screen_time)
highest_steps_month = months[average_step_count.index(highest_steps)]
lowest_screen_time_month = months[average_screen_time.index(lowest_screen_time)]

plt.annotate(f'Highest Steps\n{highest_steps}', xy=(highest_steps_month, highest_steps), xytext=(highest_steps_month, highest_steps + 300),
             arrowprops=dict(facecolor='black', shrink=0.05), ha='center')
plt.annotate(f'Lowest Screen Time\n{lowest_screen_time} mins', xy=(lowest_screen_time_month, lowest_screen_time), xytext=(lowest_screen_time_month, lowest_screen_time - 20),
             arrowprops=dict(facecolor='black', shrink=0.05), ha='center')

# Customize the rest of the chart
plt.title("Monthly Average Physical Activity and Screen Time", y=1.02)
plt.xlabel("Month")
plt.ylabel("Value")
plt.legend(loc='upper left')
plt.grid(True)
plt.gca().invert_yaxis()
plt.tight_layout()

# Show the plot
plt.show()