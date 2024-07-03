
import matplotlib.pyplot as plt

# Provided data
data = [
    {'Week': '2023-W09', 'AverageTemperature': 22},
    {'Week': '2023-W10', 'AverageTemperature': 24},
    {'Week': '2023-W11', 'AverageTemperature': 21},
    {'Week': '2023-W12', 'AverageTemperature': 25},
    {'Week': '2023-W13', 'AverageTemperature': 23},
    {'Week': '2023-W14', 'AverageTemperature': 27},
    {'Week': '2023-W15', 'AverageTemperature': 26},
    {'Week': '2023-W16', 'AverageTemperature': 28},
    {'Week': '2023-W17', 'AverageTemperature': 29},
    {'Week': '2023-W18', 'AverageTemperature': 30},
    {'Week': '2023-W19', 'AverageTemperature': 32},
    {'Week': '2023-W20', 'AverageTemperature': 31}
]

# Extracting weeks and average temperatures
weeks = [entry['Week'] for entry in data]
avg_temperatures = [entry['AverageTemperature'] for entry in data]

# Creating the line chart
plt.figure(figsize=(14, 8))
line, = plt.plot(weeks, avg_temperatures, color='#4a90e2', linestyle='-', linewidth=2, marker='s', markerfacecolor='#d0021b', markeredgewidth=2, markersize=8)

# Highlighting the highest average temperature
max_temp = max(avg_temperatures)
max_week = weeks[avg_temperatures.index(max_temp)]
plt.annotate(f'Peak\n{max_temp}', xy=(max_week, max_temp), xytext=(max_week, max_temp + 1),
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='center')

# Highlighting the lowest average temperature
min_temp = min(avg_temperatures)
min_week = weeks[avg_temperatures.index(min_temp)]
plt.annotate(f'Low\n{min_temp}', xy=(min_week, min_temp), xytext=(min_week, min_temp - 2),
             arrowprops=dict(facecolor='red', shrink=0.05),
             horizontalalignment='center')

# Aesthetic settings for the chart
plt.title('Weekly Average Temperatures in 2023', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Week', fontsize=14)
plt.ylabel('Average Temperature (°C)', fontsize=14)
plt.grid(True, which='major', linestyle='--', linewidth=0.5, color='grey')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the chart
plt.show()