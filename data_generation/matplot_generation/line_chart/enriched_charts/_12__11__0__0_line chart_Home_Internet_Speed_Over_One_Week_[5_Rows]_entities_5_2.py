
import matplotlib.pyplot as plt

# Data
months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]
average_high_stress = [45, 50, 55, 60, 65, 70, 75, 80, 85, 70, 55, 40]
average_low_stress = [30, 35, 40, 45, 50, 55, 60, 65, 70, 55, 40, 25]

# Create the plot
plt.figure(figsize=(14, 8))
plt.plot(months, average_high_stress, color='#1f77b4', marker='o', label="Average High Stress")
plt.plot(months, average_low_stress, color='#ff7f0e', marker='o', label="Average Low Stress")

# Highlight Highest and Lowest Average Stress Levels
highest_stress = max(average_high_stress)
lowest_stress = min(average_low_stress)
highest_month = months[average_high_stress.index(highest_stress)]
lowest_month = months[average_low_stress.index(lowest_stress)]

plt.annotate(f'Highest\n{highest_stress}', xy=(highest_month, highest_stress), xytext=(highest_month, highest_stress+5),
             arrowprops=dict(facecolor='blue', shrink=0.05), ha='center')
plt.annotate(f'Lowest\n{lowest_stress}', xy=(lowest_month, lowest_stress), xytext=(lowest_month, lowest_stress-5),
             arrowprops=dict(facecolor='purple', shrink=0.05), ha='center')

# Customize rest of the chart
plt.title("Monthly Average Stress Levels in 2023", y=1.05)
plt.xlabel("Month")
plt.ylabel("Stress Level (0-100)")
plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()