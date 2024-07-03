
import matplotlib.pyplot as plt

# Data
months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]
average_high = [42, 47, 52, 58, 64, 72, 81, 86, 78, 68, 55, 46]
average_low = [26, 31, 36, 42, 47, 53, 60, 66, 58, 48, 37, 29]

# Create the plot
plt.figure(figsize=(16, 9))
plt.plot(months, average_high, color='#2ca02c', marker='o', label="Average High")
plt.plot(months, average_low, color='#d62728', marker='o', label="Average Low")

# Highlight Highest and Lowest Average Temperatures
highest_temp = max(average_high)
lowest_temp = min(average_low)
highest_month = months[average_high.index(highest_temp)]
lowest_month = months[average_low.index(lowest_temp)]

plt.annotate(f'Highest\n{highest_temp}°F', xy=(highest_month, highest_temp), xytext=(highest_month, highest_temp+5),
             arrowprops=dict(facecolor='blue', shrink=0.05), ha='center')
plt.annotate(f'Lowest\n{lowest_temp}°F', xy=(lowest_month, lowest_temp), xytext=(lowest_month, lowest_temp-5),
             arrowprops=dict(facecolor='purple', shrink=0.05), ha='center')

# Customize rest of the chart
plt.title("Monthly Average Temperatures in City X", y=1.05)
plt.xlabel("Month")
plt.ylabel("Temperature (°F)")
plt.legend(loc='lower right')
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()