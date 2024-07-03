
import matplotlib.pyplot as plt

# Data points
days = [i for i in range(1, 32)]
temp_city_a = [25.5, 25.7, 25.9, 26.1, 26.3, 26.5, 26.8, 27.0, 27.2, 27.5, 27.7, 27.9, 28.1,
               28.4, 28.6, 28.8, 29.0, 29.2, 29.5, 29.7, 29.9, 30.1, 30.3, 30.5, 30.7, 30.9,
               31.1, 31.3, 31.5, 31.7, 31.9]
temp_city_b = [30.0, 29.8, 29.6, 29.4, 29.2, 29.0, 28.8, 28.6, 28.4, 28.2, 28.0, 27.8, 27.5,
               27.3, 27.1, 26.9, 26.7, 26.5, 26.3, 26.1, 25.9, 25.7, 25.5, 25.3, 25.1, 24.9,
               24.7, 24.5, 24.3, 24.1, 23.9]

# Creating plot
plt.figure(figsize=(10, 6))
plt.plot(days, temp_city_a, color='#FF5733', label='City A')  # bright red
plt.plot(days, temp_city_b, color='#33B5FF', label='City B')  # bright blue

# Adding a title and labels to the axes
plt.title('Average Daily Temperature in July')
plt.xlabel('Day of the Month')
plt.ylabel('Average Temperature (°C)')

# Add annotations for maximum and minimum temperatures of both cities
plt.annotate('City A Warmer', xy=(31, temp_city_a[-1]), xytext=(28, temp_city_a[-4]),
             arrowprops=dict(facecolor='#FF5733', shrink=0.05))

plt.annotate('City B Cooler', xy=(31, temp_city_b[-1]), xytext=(28, temp_city_b[-4]),
             arrowprops=dict(facecolor='#33B5FF', shrink=0.05))

# Show grid and legend
plt.grid(True)
plt.legend()

# Show the plot
plt.show()