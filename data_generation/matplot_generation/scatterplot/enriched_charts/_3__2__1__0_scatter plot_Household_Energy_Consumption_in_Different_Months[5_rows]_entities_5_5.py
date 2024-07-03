
import matplotlib.pyplot as plt

# Data for plotting
dates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
max_temperature = [85, 88, 90, 87, 92, 89, 93, 94, 96, 95, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116]
min_temperature = [65, 67, 70, 68, 71, 69, 72, 74, 75, 73, 76, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96]

# Create a scatterplot
plt.figure(figsize=(14, 9))
plt.scatter(dates, max_temperature, c="#FF4500", label="Max Temperature")
plt.scatter(dates, min_temperature, c="#1E90FF", label="Min Temperature")

# Customize the chart
plt.title("Daily Maximum and Minimum Temperatures in June", pad=20)
plt.xlabel("Day of the Month")
plt.ylabel("Temperature (°F)")
plt.legend(loc='lower left')
plt.grid(True)

# Show the scatterplot
plt.show()