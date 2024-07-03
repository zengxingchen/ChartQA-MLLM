
import matplotlib.pyplot as plt

# Data
days = list(range(1, 31))
revenue = [1500, 1700, 1650, 1800, 1600, 1900, 2000, 2200, 2100, 2500, 
           2400, 2300, 2600, 2800, 2700, 2900, 3000, 3200, 3100, 3300, 
           3400, 3500, 3700, 3600, 3800, 3900, 4100, 4000, 4200, 4300]

plt.figure(figsize=(16, 8))  # Changing width and height of the chart
plt.plot(days, revenue, marker='o', color='#FF5733', linewidth=2)  # Modified color scheme

# Adding annotations for the highest and lowest revenue
plt.annotate('Lowest Revenue', xy=(1, 1500), xytext=(2, 1200),
             arrowprops=dict(facecolor='#FF33A8', shrink=0.05))
plt.annotate('Highest Revenue', xy=(30, 4300), xytext=(29, 4500),
             arrowprops=dict(facecolor='#33FF57', shrink=0.05))

plt.title('Monthly Revenue in June', pad=20)  # New headline which fits the topic
plt.xlabel('Day')  # Changing labels to fit the new data type
plt.ylabel('Revenue ($)')
plt.grid(True)

plt.show()