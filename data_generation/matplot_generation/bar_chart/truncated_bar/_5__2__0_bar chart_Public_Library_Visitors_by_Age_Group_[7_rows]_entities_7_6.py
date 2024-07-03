
import matplotlib.pyplot as plt

# Data
months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]
average_hours_of_sleep = [7.5, 7.2, 7.0, 6.8, 6.5, 6.2, 6.0, 6.3, 6.7, 7.0, 7.3, 7.6]

# Creating horizontal bar chart
fig, ax = plt.subplots(figsize=(8, 10))  # Change the width and height of the chart

ax.barh(months, average_hours_of_sleep, color=[
    '#FF6347', '#FF4500', '#FFD700', '#FFA500',
    '#00FF7F', '#32CD32', '#7FFF00', '#ADFF2F',
    '#87CEEB', '#4682B4', '#1E90FF', '#0000CD'
], height=0.5)  # Change bar color and height

# Adding labels and title
ax.set_xlabel('Average Hours of Sleep')
ax.set_title('Average Monthly Sleep Hours in a Year', pad=20)

# Setting y-axis limit to truncate the bar chart
ax.set_xlim(5.5, 8)

# Show the plot
plt.show()