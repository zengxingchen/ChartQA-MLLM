
import matplotlib.pyplot as plt

# Data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
temperatures = [78, 82, 85, 88, 90, 92, 80]

# Colors for each bar
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#FF8C33', '#8C33FF', '#33FFC1']

# Plotting the bar chart horizontally
plt.figure(figsize=(10, 14))  # Change width and height of the chart
plt.barh(days, temperatures, color=colors, edgecolor='black', height=0.5)  # Change height for bars and apply color scheme

# Chart title and labels
plt.title('Daily High Temperatures', fontsize=20, pad=20)
plt.xlabel('Temperature (°F)', fontsize=16)

# Setting the ylim to start from a specific value
plt.xlim(75, max(temperatures) + 10)

# Display the chart
plt.tight_layout()
plt.show()