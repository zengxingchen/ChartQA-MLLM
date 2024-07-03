
import matplotlib.pyplot as plt

# Data
days = list(range(1, 31))
sales = [12000, 11500, 11000, 10500, 10000, 9500, 9000, 8500, 8000, 7500,
         7000, 6500, 6000, 5500, 5000, 4500, 4000, 3500, 3000, 2500,
         2000, 1500, 1000, 500, 3000, 3500, 4000, 4500, 5000, 5500]

plt.figure(figsize=(16, 8))  # Changed width and height of the chart
plt.plot(days, sales, marker='o', color='#FF5733', linewidth=2)  # Modified color scheme

# Adding annotations for the highest and lowest sales
plt.annotate('Lowest Sales', xy=(24, 500), xytext=(25, 1500),
             arrowprops=dict(facecolor='#C70039', shrink=0.05))
plt.annotate('Highest Sales', xy=(1, 12000), xytext=(2, 12500),
             arrowprops=dict(facecolor='#900C3F', shrink=0.05))

plt.title('Daily Sales in June', pad=20)  # New headline which fits the topic
plt.xlabel('Day')  # Changing labels to fit the new data type
plt.ylabel('Sales ($)')
plt.gca().invert_yaxis()  # Inverting y-axis
plt.grid(True)

plt.show()