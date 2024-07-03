
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
temperatures = [5, 6, 10, 14, 18, 22, 25, 24, 20, 15, 9, 6]

# Colors for each bar
colors = ['#FF5733', '#FF681F', '#FF763B', '#FF8F56', '#FFB072', '#FFC488', '#FFD19E', '#FFDFB3', '#FFEDC8', '#FFE4D3', '#FFEFE0', '#FFFAF0']

# Plotting the bar chart horizontally
plt.figure(figsize=(12, 8))   # Change width and height of the chart
plt.barh(months, temperatures, color=colors, edgecolor='black', height=0.7)  # Change band width for bars and apply color scheme

# Chart title and labels
plt.title('Average Monthly Temperatures in a City', fontsize=15)
plt.xlabel('Average Temperature (°C)', fontsize=12)

# Setting the xlim to provide better clarity for temperature values
plt.xlim(0, max(temperatures) + 5)

# Display the chart
plt.tight_layout()
plt.show()