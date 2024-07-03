import matplotlib.pyplot as plt

# Data
months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]
average_high = [40, 45, 50, 55, 60, 70, 80, 85, 80, 70, 55, 45]
average_low = [25, 30, 35, 40, 45, 50, 60, 65, 60, 50, 40, 30]

# Create the plot
plt.figure(figsize=(14, 8))
plt.plot(months, average_high, color='#1f77b4', marker='o', label="Average High")
plt.plot(months, average_low, color='#ff7f0e', marker='o', label="Average Low")

# Highlight Highest and Lowest Average Temperatures
highest_temp = max(average_high)
lowest_temp = min(average_low)
highest_month = months[average_high.index(highest_temp)]
lowest_month = months[average_low.index(lowest_temp)]

plt.annotate(f'Highest\n{highest_temp}°F', xy=(highest_month, highest_temp), xytext=(highest_month, highest_temp+5),
             arrowprops=dict(facecolor='black', shrink=0.05), ha='center')
plt.annotate(f'Lowest\n{lowest_temp}°F', xy=(lowest_month, lowest_temp), xytext=(lowest_month, lowest_temp-5),
             arrowprops=dict(facecolor='black', shrink=0.05), ha='center')

# Customize rest of the chart
plt.title("Monthly Average Temperatures in City Y", y=1.05)
plt.xlabel("Month")
plt.ylabel("Temperature (°F)")
plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()