
import matplotlib.pyplot as plt

# Data
days = list(range(1, 30 + 1))
steps = [15000, 14000, 16000, 15500, 14500, 17000, 16500, 18000, 17500, 16000,
         15500, 15000, 16500, 16000, 17000, 17500, 18000, 18500, 19000, 19500,
         18500, 17500, 18000, 19000, 18500, 19500, 20000, 21000, 20500, 20000]

plt.figure(figsize=(14, 7))  # Adjusted width and height of the chart
plt.plot(days, steps, marker='o', color='#4CAF50', linewidth=2)  # Modified color scheme

# Adding annotations for the highest and lowest steps count
plt.annotate('Lowest Steps', xy=(2, 14000), xytext=(3, 13500),
             arrowprops=dict(facecolor='#FF5733', shrink=0.05))
plt.annotate('Highest Steps', xy=(28, 21000), xytext=(27, 21500),
             arrowprops=dict(facecolor='#FF5733', shrink=0.05))

plt.title('Daily Step Count in June', pad=20)  # New headline which fits the topic
plt.xlabel('Day')  # Changing labels to fit the new data type
plt.ylabel('Steps')
plt.gca().invert_yaxis()  # Invert the y-axis
plt.grid(True)

plt.show()