
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
temperatures = [2, 4, 8, 12, 16, 20, 24, 23, 19, 13, 7, 3]

# Colors for each bar
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', '#33FFA1', '#FFA133', '#5733FF', '#FF3333', '#33FFA8', '#A8FF33', '#FF33D4']

# Plotting the bar chart horizontally
plt.figure(figsize=(12, 8))  # Change width and height of the chart
plt.barh(months, temperatures, color=colors, edgecolor='black', height=0.6)  # Change bar height and apply color scheme

# Chart title and labels
plt.title('Average Monthly Temperatures in a City', fontsize=18, pad=20)
plt.xlabel('Average Temperature (°C)', fontsize=14)

# Setting the xlim to provide better clarity for temperature values
plt.xlim(0, max(temperatures) + 5)

# Display the chart
plt.tight_layout()
plt.show()