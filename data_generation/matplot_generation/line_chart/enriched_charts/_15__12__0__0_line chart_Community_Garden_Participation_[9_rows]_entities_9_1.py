
import matplotlib.pyplot as plt

# Data
days = list(range(1, 31))
profit = [500, 700, 800, 1000, 1200, 1100, 1300, 1400, 1600, 1700, 
          1800, 2000, 1900, 2200, 2100, 2300, 2400, 2500, 2600, 2700, 
          2900, 2800, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700]

plt.figure(figsize=(14, 7))
plt.plot(days, profit, marker='o', color='#4B0082', linewidth=2)

# Adding annotations for the highest and lowest profit
plt.annotate('Lowest Profit', xy=(1, 500), xytext=(3, 300),
             arrowprops=dict(facecolor='#FFD700', shrink=0.05))
plt.annotate('Highest Profit', xy=(30, 3700), xytext=(27, 3900),
             arrowprops=dict(facecolor='#00FF00', shrink=0.05))

plt.title('Daily Profit for a Startup in June', pad=20)
plt.xlabel('Day')
plt.ylabel('Profit ($)')
plt.grid(True)
plt.gca().invert_yaxis()

plt.show()