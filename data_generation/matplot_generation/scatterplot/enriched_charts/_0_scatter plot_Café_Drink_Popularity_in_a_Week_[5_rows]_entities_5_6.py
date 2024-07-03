
import matplotlib.pyplot as plt

# Data
days = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30
]
temperatures = [
    22, 24, 19, 21, 23, 20, 18, 25, 27, 28,
    29, 30, 31, 22, 24, 19, 26, 20, 21, 28,
    31, 25, 29, 30, 33, 34, 23, 22, 21, 20
]
humidity = [
    60, 58, 75, 65, 50, 80, 90, 55, 45, 48,
    43, 40, 38, 70, 60, 76, 52, 85, 68, 47,
    42, 50, 44, 41, 35, 33, 51, 69, 72, 78
]

# Map the temperature to a color
temp_colors = [f'#{hex(min(255, temp * 5))[-2:]}00{hex(255 - min(255, temp * 5))[-2:]}' for temp in temperatures]

# Scatter plot
fig, ax = plt.subplots(figsize=(10, 6))  # Changed width and height
sc = ax.scatter(days, temperatures, s=[h + 20 for h in humidity], c=temp_colors, alpha=0.75)

# Customizing the axes and title
ax.set_xlabel('Day of the Month')
ax.set_ylabel('Temperature (°C)')
ax.set_title('Daily Temperature and Humidity Measurements')
ax.grid(True)

# Show plot
plt.show()