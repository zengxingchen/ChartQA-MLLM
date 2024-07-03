
import matplotlib.pyplot as plt

# Data
months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]
average_hours_of_daylight = [8, 9, 11, 13, 15, 16, 15, 14, 12, 10, 9, 8]

# Creating vertical bar chart
fig, ax = plt.subplots(figsize=(10, 6))  # Change the width and height of the chart

ax.bar(months, average_hours_of_daylight, color=[
    '#FF6347', '#FF4500', '#FFD700', '#FFA500',
    '#00FF7F', '#32CD32', '#7FFF00', '#ADFF2F',
    '#87CEEB', '#4682B4', '#1E90FF', '#0000CD'
], width=0.6)  # Change bar color and width

# Adding labels and title
ax.set_ylabel('Average Hours of Daylight')
ax.set_title('Average Monthly Daylight Hours in a Year')

# Show the plot
plt.show()