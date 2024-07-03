
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
temperatures = [30, 32, 35, 40, 45, 50, 55, 53, 48, 43, 38, 33]

# Colors for each bar
colors = ['#ff5733', '#33ff57', '#3357ff', '#ff33a8', '#a833ff', '#33fff5', '#ff9133', '#33ff91', '#9133ff', '#ff3391', '#3391ff', '#f5ff33']

# Plotting the bar chart horizontally
plt.figure(figsize=(8, 12))  # Change width and height of the chart
plt.barh(months, temperatures, color=colors, edgecolor='black', height=0.6)  # Change width for bars and apply color scheme

# Chart title and labels
plt.title('Average Monthly Temperatures in a City', fontsize=15)
plt.xlabel('Average Temperature (°C)', fontsize=12)

# Setting the ylim to provide better clarity for temperature values
plt.xlim(25, max(temperatures) + 5)

# Display the chart
plt.tight_layout()
plt.show()