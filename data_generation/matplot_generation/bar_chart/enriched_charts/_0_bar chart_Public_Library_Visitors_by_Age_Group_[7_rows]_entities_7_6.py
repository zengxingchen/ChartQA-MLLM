
import matplotlib.pyplot as plt

# Data
months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]
average_temperatures_celsius = [5, 6, 10, 15, 20, 25, 30, 29, 24, 18, 10, 6]

# Creating horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))  # Change the width and height of the chart

ax.barh(months, average_temperatures_celsius, color=[
    '#FF5733', '#FF7D33', '#FFA233', '#FFC733',
    '#1E7EB2', '#1EA2B2', '#1EB282', '#1EB264',
    '#E0D71E', '#D8B11E', '#996A13', '#6E4911'
], height=0.5)  # Change bar color and height

# Adding labels and title
ax.set_xlabel('Average Temperature (°C)')
ax.set_title('Average Monthly Temperatures in Fictional City')

# Show the plot
plt.show()