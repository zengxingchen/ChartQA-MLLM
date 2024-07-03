
import matplotlib.pyplot as plt

# Data
days = list(range(1, 31))
income = [5000, 5300, 5200, 5100, 5500, 5600, 5800, 6000, 6200, 6100,
          6300, 6400, 6500, 6600, 6800, 6700, 6900, 7100, 7000, 7200,
          7300, 7500, 7400, 7600, 7800, 7700, 7900, 8000, 8200, 8100]

plt.figure(figsize=(12, 8))  # Changing width and height of the chart
plt.plot(days, income, marker='s', color='#FF5733', linewidth=2)  # Modified color scheme

# Adding annotations for significant income points
plt.annotate('Lowest Income', xy=(1, 5000), xytext=(2, 5200),
             arrowprops=dict(facecolor='#DAF7A6', shrink=0.05))
plt.annotate('Highest Income', xy=(29, 8200), xytext=(28, 8400),
             arrowprops=dict(facecolor='#C70039', shrink=0.05))

plt.title('Daily Income in June', pad=20)  # New headline which fits the topic
plt.xlabel('Day')  # Changing labels to fit the new data type
plt.ylabel('Income (USD)')
plt.grid(True)

plt.show()