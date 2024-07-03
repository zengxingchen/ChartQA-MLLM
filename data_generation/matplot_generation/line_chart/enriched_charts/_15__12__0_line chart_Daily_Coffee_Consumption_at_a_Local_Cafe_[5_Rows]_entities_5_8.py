
import matplotlib.pyplot as plt

# Data points
days = [i for i in range(1, 32)]
temperature_a = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
temperature_b = [80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50]

# Creating plot
plt.figure(figsize=(10, 6))
plt.plot(days, temperature_a, color='#1A5276', label='Temperature A')  # dark blue
plt.plot(days, temperature_b, color='#D35400', label='Temperature B')  # dark orange

# Adding a title and labels to the axes
plt.title('Daily Temperatures in July', pad=20)
plt.xlabel('Day of the Month')
plt.ylabel('Temperature (°F)')

# Add annotations for maximum and minimum temperatures of both series
plt.annotate('Temperature A Highest', xy=(31, temperature_a[-1]), xytext=(25, temperature_a[-5]),
             arrowprops=dict(facecolor='#1A5276', shrink=0.05))

plt.annotate('Temperature B Lowest', xy=(31, temperature_b[-1]), xytext=(25, temperature_b[-5]),
             arrowprops=dict(facecolor='#D35400', shrink=0.05))

# Invert y-axis
plt.gca().invert_yaxis()

# Show grid and legend
plt.grid(True)
plt.legend(loc='upper left')

# Show the plot
plt.show()