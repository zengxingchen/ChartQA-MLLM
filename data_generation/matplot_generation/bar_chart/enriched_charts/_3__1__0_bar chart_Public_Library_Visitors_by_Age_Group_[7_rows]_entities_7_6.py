
import matplotlib.pyplot as plt

# Data
months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]
average_temperature_c = [4, 5, 9, 12, 17, 20, 22, 21, 18, 13, 8, 5]

# Creating horizontal bar chart
fig, ax = plt.subplots(figsize=(8, 12))

ax.barh(months, average_temperature_c, color=[
    '#FF5733', '#FF6F33', '#FF8633', '#FF9E33',
    '#FFB533', '#FFCC33', '#FFE433', '#EFFF33',
    '#D8FF33', '#C0FF33', '#A9FF33', '#91FF33'
], height=0.5)

# Adding labels and title
ax.set_xlabel('Average Temperature (°C)')
ax.set_title('Average Monthly Temperature in Fictional City', pad=20)

# Show the plot
plt.show()