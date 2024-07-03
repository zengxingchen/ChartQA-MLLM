
import matplotlib.pyplot as plt

# Data
months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]
average_high = [38, 42, 53, 65, 75, 83, 87, 85, 78, 67, 55, 43]
average_low = [22, 25, 33, 44, 54, 63, 68, 66, 59, 47, 37, 27]

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(months, average_high, color='#FF5733', marker='o', label="Average High")
plt.plot(months, average_low, color='#33C1FF', marker='o', label="Average Low")

# Highlight Highest and Lowest Average Temperatures
highest_temp = max(average_high)
lowest_temp = min(average_low)
highest_month = months[average_high.index(highest_temp)]
lowest_month = months[average_low.index(lowest_temp)]

plt.annotate(f'Highest\n{highest_temp}°', xy=(highest_month, highest_temp), xytext=(highest_month, highest_temp+5),
             arrowprops=dict(facecolor='black', shrink=0.05), ha='center')
plt.annotate(f'Lowest\n{lowest_temp}°', xy=(lowest_month, lowest_temp), xytext=(lowest_month, lowest_temp-5),
             arrowprops=dict(facecolor='black', shrink=0.05), ha='center')

# Customize rest of the chart
plt.title("Average High and Low Temperatures in City X")
plt.xlabel("Month")
plt.ylabel("Temperature (°F)")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()