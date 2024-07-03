
import matplotlib.pyplot as plt

# Data
months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]
average_precipitation_mm = [75, 60, 85, 120, 155, 180, 220, 210, 175, 130, 95, 80]

# Creating vertical bar chart
fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(months, average_precipitation_mm, color=[
    '#3366FF', '#3399FF', '#33CCFF', '#33FFFF',
    '#66FFCC', '#66FF99', '#66FF66', '#99FF66',
    '#CCFF66', '#FFFF66', '#FFCC66', '#FF9966'
], width=0.6)  # Change bar color and width

# Adding labels and title
ax.set_ylabel('Average Precipitation (mm)')
ax.set_title('Average Monthly Precipitation in Fictional City', pad=20)

# Show the plot
plt.show()