
import matplotlib.pyplot as plt

# Data points
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
temperatures = [22, 19, 25, 21, 27, 24, 22]

# Colors for each bar
colors = ['#FF5733', '#33BEFF', '#FFC733', '#33FF57', '#8E33FF', '#FF3380', '#33FFF6']

# Create a horizontal bar chart
plt.figure(figsize=(10, 8))
plt.barh(days, temperatures, color=colors, height=0.6)

# Modify the ticks, labels, and title
plt.xlabel('Average Temperature (°C)')
plt.title('Average Daily Temperatures for a Week')
plt.xlim(15, 30)  # Assuming the temperature ranges between 15 and 30 degrees Celsius

# Display the plot
plt.show()