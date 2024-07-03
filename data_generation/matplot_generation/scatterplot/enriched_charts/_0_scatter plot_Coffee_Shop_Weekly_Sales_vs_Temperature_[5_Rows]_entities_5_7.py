
import matplotlib.pyplot as plt

# Data
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
air_temperature = [22.1, 23.3, 24.7, 23.9, 25.1, 26.3, 25.7, 26.9, 28.1, 27.4]
co2_levels = [414.2, 416.5, 418.3, 417.9, 420.4, 422.1, 421.7, 423.4, 425.6, 423.8]

# Scatter plot
plt.figure(figsize=(10, 6))  # Width:10, Height:6
plt.scatter(days, air_temperature, color='#FF5733', label='Air Temperature')  # Orange
plt.scatter(days, co2_levels, color='#3498DB', label='CO2 Levels')  # Blue

# Customize the plot
plt.title('Environmental Data Over 10 Days')
plt.xlabel('Day')
plt.ylabel('Measurements')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()