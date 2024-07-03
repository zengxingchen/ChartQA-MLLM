
import matplotlib.pyplot as plt

# Data
months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]
average_high_distance = [30, 35, 40, 50, 60, 70, 75, 80, 70, 60, 50, 40]
average_low_distance = [20, 22, 28, 35, 45, 50, 55, 60, 50, 40, 30, 25]

# Create the plot
plt.figure(figsize=(14, 7))
plt.plot(months, average_high_distance, color='#FF5733', marker='o', label="Average High Distance")
plt.plot(months, average_low_distance, color='#33C1FF', marker='o', label="Average Low Distance")

# Highlight Highest and Lowest Average Distances
highest_distance = max(average_high_distance)
lowest_distance = min(average_low_distance)
highest_month = months[average_high_distance.index(highest_distance)]
lowest_month = months[average_low_distance.index(lowest_distance)]

plt.annotate(f'Highest\n{highest_distance} km', xy=(highest_month, highest_distance), xytext=(highest_month, highest_distance+5),
             arrowprops=dict(facecolor='black', shrink=0.05), ha='center')
plt.annotate(f'Lowest\n{lowest_distance} km', xy=(lowest_month, lowest_distance), xytext=(lowest_month, lowest_distance-5),
             arrowprops=dict(facecolor='black', shrink=0.05), ha='center')

# Customize rest of the chart
plt.title("Average Monthly Running Distance in City X", pad=20)
plt.xlabel("Month")
plt.ylabel("Distance (km)")
plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()