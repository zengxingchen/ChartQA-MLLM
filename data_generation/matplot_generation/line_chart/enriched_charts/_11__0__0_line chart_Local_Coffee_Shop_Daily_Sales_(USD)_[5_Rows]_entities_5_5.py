
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
temperatures = [5, 6, 9, 13, 18, 22, 25, 24, 20, 15, 10, 6]

# Plotting the line chart
plt.figure(figsize=(16, 8))  # Change width and height of the chart
plt.plot(months, temperatures, marker='o', linestyle='-', color='#0073e6', linewidth=2.5)  # Modify color scheme

# Adding title and labels
plt.title('Monthly Average Temperature in City XYZ', fontsize=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)

# Adding an annotation for the highest temperature
highest_temp_index = temperatures.index(max(temperatures))
highest_temp_month = months[highest_temp_index]
plt.annotate('Peak Temperature', xy=(highest_temp_index, max(temperatures)), xytext=(highest_temp_index, max(temperatures) + 3),
             arrowprops=dict(facecolor='#ff5733', shrink=0.05))

# Add a grid, set axis ranges and show the plot
plt.grid(True)
plt.ylim(0, 30)
plt.show()