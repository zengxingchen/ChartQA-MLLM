
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
temperature = [2, 3, 6, 10, 15, 20, 25, 24, 18, 12, 7, 3]
humidity = [80, 78, 75, 70, 65, 60, 55, 58, 65, 70, 75, 80]
rainfall = [50, 40, 55, 60, 70, 80, 90, 85, 75, 65, 60, 55]

# Plot setup
fig, ax = plt.subplots(figsize=(16,10))

# Create bar chart
bar_width = 0.35
bar_locations_temp = range(len(temperature))
bar_locations_hum = [x + bar_width for x in bar_locations_temp]
bar_locations_rain = [x + bar_width for x in bar_locations_hum]

bars1 = ax.bar(bar_locations_temp, temperature, bar_width, label='Temperature (°C)', color='#1f77b4')
bars2 = ax.bar(bar_locations_hum, humidity, bar_width, label='Humidity (%)', color='#ff7f0e')
bars3 = ax.bar(bar_locations_rain, rainfall, bar_width, label='Rainfall (mm)', color='#2ca02c')

# Set the position of the x ticks
ax.set_xticks([r + bar_width for r in range(len(temperature))])
ax.set_xticklabels(months)

# Adding labels and title
plt.ylabel('Measurements')
plt.title('Monthly Weather Statistics')
ax.legend()

# Display the plot
plt.tight_layout()
plt.show()