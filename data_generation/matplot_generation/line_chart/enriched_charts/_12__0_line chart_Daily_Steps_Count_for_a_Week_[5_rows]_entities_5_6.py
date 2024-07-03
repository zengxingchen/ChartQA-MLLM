
import matplotlib.pyplot as plt

# Given the data above
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
pollution_levels = [95, 85, 75, 80, 70, 65, 60, 55, 50, 45, 55, 60]

plt.figure(figsize=(14, 8))  # Change width (14) and height (8)

# Plot the line chart with a new color scheme and trend
plt.plot(months, pollution_levels, color='#3498DB', linewidth=2)

# Annotate the peak sales value in January
plt.annotate('Highest Pollution', xy=('January', 95), xytext=('February', 85),
             arrowprops=dict(facecolor='#E74C3C', shrink=0.05))

plt.title('Monthly Air Pollution Levels (AQI)')  # Set a relevant title
plt.xlabel('Month')  # Label the x-axis
plt.ylabel('Air Quality Index (AQI)')  # Label the y-axis

# Display the chart
plt.show()