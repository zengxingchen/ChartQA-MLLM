
import matplotlib.pyplot as plt

# Data
months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]
average_temperature = [30, 32, 45, 55, 65, 75, 85, 84, 75, 60, 45, 35]

# Creating vertical bar chart
fig, ax = plt.subplots(figsize=(10, 6))  # Change the width and height of the chart

ax.bar(months, average_temperature, color=[
    '#FF5733', '#FF8D1A', '#FFC300', '#DAF7A6',
    '#33FF57', '#1AFF8D', '#00FFC3', '#33D7FF',
    '#1A8DFF', '#5733FF', '#8D1AFF', '#C300FF'
], width=0.4)  # Change bar color and width

# Adding labels and title
ax.set_ylabel('Average Temperature (°F)')
ax.set_title('Monthly Average Temperature', pad=20)

# Set y-axis limits
ax.set_ylim(25, 90)

# Show the plot
plt.show()