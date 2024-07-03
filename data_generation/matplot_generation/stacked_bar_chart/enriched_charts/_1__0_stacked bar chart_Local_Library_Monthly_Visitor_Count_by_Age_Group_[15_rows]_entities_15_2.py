
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
beach_bookings = [80, 100, 90, 95, 110, 120, 130, 125, 105, 115, 90, 85]
mountain_bookings = [70, 80, 85, 90, 100, 110, 120, 115, 95, 105, 85, 75]
city_bookings = [60, 70, 75, 85, 95, 100, 110, 105, 90, 100, 80, 65]

# Color codes for each trip type
colors = ['#ff9999', '#66b3ff', '#99ff99']

# Plot stacked bar chart
plt.figure(figsize=(12, 10)) # Width and height of the chart in inches
bar_width = 0.6 # Width of the bars

plt.bar(months, beach_bookings, color=colors[0], edgecolor='white', width=bar_width, label='Beach')
plt.bar(months, mountain_bookings, bottom=beach_bookings, color=colors[1], edgecolor='white', width=bar_width, label='Mountain')
plt.bar(months, city_bookings, bottom=[i+j for i,j in zip(beach_bookings, mountain_bookings)], color=colors[2], edgecolor='white', width=bar_width, label='City')

# Add labels and title
plt.ylabel('Bookings')
plt.xlabel('Month')
plt.title('Monthly Bookings for Different Types of Trips')
plt.legend(loc='upper left')

# Display the final result
plt.show()