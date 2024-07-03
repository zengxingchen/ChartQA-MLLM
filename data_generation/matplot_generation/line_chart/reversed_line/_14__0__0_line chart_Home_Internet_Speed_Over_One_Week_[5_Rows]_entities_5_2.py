
import matplotlib.pyplot as plt

# Data
months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]
average_high = [20, 30, 40, 50, 60, 70, 80, 90, 75, 65, 45, 30]
average_low = [10, 20, 25, 30, 35, 40, 45, 50, 55, 50, 35, 20]

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(months, average_high, color='#e74c3c', marker='o', label="Average High")
plt.plot(months, average_low, color='#3498db', marker='o', label="Average Low")

# Highlight Highest and Lowest Average Power Generation
highest_power = max(average_high)
lowest_power = min(average_low)
highest_month = months[average_high.index(highest_power)]
lowest_month = months[average_low.index(lowest_power)]

plt.annotate(f'Highest\n{highest_power} kWh', xy=(highest_month, highest_power), xytext=(highest_month, highest_power+5),
             arrowprops=dict(facecolor='black', shrink=0.05), ha='center')
plt.annotate(f'Lowest\n{lowest_power} kWh', xy=(lowest_month, lowest_power), xytext=(lowest_month, lowest_power-5),
             arrowprops=dict(facecolor='black', shrink=0.05), ha='center')

# Customize rest of the chart
plt.title("Monthly Average Solar Power Generation in City Y", y=1.05)
plt.xlabel("Month")
plt.ylabel("Power Generation (kWh)")
plt.legend(loc='upper left')
plt.grid(True)
plt.gca().invert_yaxis()
plt.tight_layout()

# Show the plot
plt.show()