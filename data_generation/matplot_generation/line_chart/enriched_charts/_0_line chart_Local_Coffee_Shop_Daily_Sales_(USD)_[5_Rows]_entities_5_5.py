
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
temperature = [31, 34, 42, 53, 64, 73, 79, 78, 70, 59, 47, 35]

# Plotting the line chart
plt.figure(figsize=(12, 6))  # Change width and height of the chart
plt.plot(months, temperature, marker='o', linestyle='-', color='#007acc', linewidth=2.5)  # Modify color scheme

# Adding title and labels
plt.title('Average Monthly Temperatures in City XYZ', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Temperature (°F)', fontsize=12)

# Adding an annotation for the highest temperature
highest_temp_index = temperature.index(max(temperature))
highest_temp_month = months[highest_temp_index]
plt.annotate('Highest', xy=(highest_temp_index, max(temperature)), xytext=(highest_temp_index, max(temperature) + 5),
             arrowprops=dict(facecolor='#ff5733', shrink=0.05))

# Add a grid, set axis ranges and show the plot
plt.grid(True)
plt.ylim(25, 85)
plt.show()