
import matplotlib.pyplot as plt

# Data
months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]
average_rainfall_mm = [78, 60, 55, 70, 90, 100, 110, 95, 85, 75, 65, 80]

# Creating truncated bar chart
fig, ax = plt.subplots(figsize=(12, 8))

ax.bar(months, average_rainfall_mm, color=[
    '#FF5733', '#FF6F33', '#FF8633', '#FF9E33',
    '#FFB533', '#FFCC33', '#FFE433', '#EFFF33',
    '#D8FF33', '#C0FF33', '#A9FF33', '#91FF33'
], width=0.6)

# Adding labels and title
ax.set_ylabel('Average Rainfall (mm)')
ax.set_title('Average Monthly Rainfall in Fictional City', pad=20)
ax.set_ylim(50, 120)  # Set y-axis limits to truncate the chart

# Show the plot
plt.show()