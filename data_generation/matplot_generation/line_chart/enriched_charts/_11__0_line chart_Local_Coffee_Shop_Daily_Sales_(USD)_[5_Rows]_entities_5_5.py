
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
rainfall = [3.2, 2.8, 4.1, 3.5, 4.7, 3.8, 5.6, 6.2, 4.0, 3.3, 2.9, 3.6]

# Plotting the line chart
plt.figure(figsize=(14, 7))
plt.plot(months, rainfall, marker='s', linestyle='-', color='#ff9900', linewidth=2.5)

# Adding title and labels
plt.title('Average Monthly Rainfall in City XYZ', fontsize=18)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Rainfall (inches)', fontsize=12)

# Adding an annotation for the highest rainfall
highest_rainfall_index = rainfall.index(max(rainfall))
highest_rainfall_month = months[highest_rainfall_index]
plt.annotate('Highest', xy=(highest_rainfall_index, max(rainfall)), xytext=(highest_rainfall_index, max(rainfall) + 0.5),
             arrowprops=dict(facecolor='#3366cc', shrink=0.05))

# Add a grid, set axis ranges and show the plot
plt.grid(True)
plt.ylim(2, 7)
plt.show()