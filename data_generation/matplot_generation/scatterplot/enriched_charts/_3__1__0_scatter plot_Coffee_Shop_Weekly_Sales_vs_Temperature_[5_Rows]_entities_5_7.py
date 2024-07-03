
import matplotlib.pyplot as plt

# Data
days = list(range(1, 31))
precipitation = [12, 10, 15, 8, 20, 14, 7, 18, 6, 22, 13, 9, 16, 11, 19, 15, 5, 20, 8, 21, 12, 10, 15, 9, 18, 14, 6, 20, 7, 22]
temperature = [25, 27, 24, 26, 23, 28, 22, 29, 21, 30, 24, 27, 25, 26, 23, 28, 22, 29, 21, 30, 25, 27, 24, 26, 23, 28, 22, 29, 21, 30]

# Scatter plot
plt.figure(figsize=(14, 8))  # Width: 14, Height: 8
plt.scatter(days, precipitation, color='#1E90FF', label='Precipitation (mm)')  # Dodger Blue
plt.scatter(days, temperature, color='#32CD32', label='Temperature (°C)')  # Lime Green

# Customize the plot
plt.title('Weather Data Over a Month', pad=20)
plt.xlabel('Day')
plt.ylabel('Measurement')
plt.legend(loc='upper right')
plt.grid(True)

# Show the plot
plt.show()