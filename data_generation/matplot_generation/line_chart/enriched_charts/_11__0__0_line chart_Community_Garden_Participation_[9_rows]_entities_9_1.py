
import matplotlib.pyplot as plt

# Data
days = list(range(1, 31))
temperature = [20, 22, 25, 18, 21, 24, 27, 19, 23, 29, 
               32, 28, 30, 26, 22, 24, 31, 33, 29, 27, 
               25, 28, 30, 32, 34, 36, 38, 35, 33, 31]

plt.figure(figsize=(16, 8))  # Changing width and height of the chart
plt.plot(days, temperature, marker='o', color='#FF5733', linewidth=2)  # Modified color scheme

# Adding annotations for the highest and lowest temperatures
plt.annotate('Lowest Temp', xy=(4, 18), xytext=(5, 15),
             arrowprops=dict(facecolor='#1F618D', shrink=0.05))
plt.annotate('Highest Temp', xy=(27, 38), xytext=(26, 40),
             arrowprops=dict(facecolor='#F1C40F', shrink=0.05))

plt.title('Daily Temperature in June', pad=20)  # New headline which fits the topic
plt.xlabel('Day')  # Changing labels to fit the new data type
plt.ylabel('Temperature (°C)')
plt.grid(True)

plt.show()