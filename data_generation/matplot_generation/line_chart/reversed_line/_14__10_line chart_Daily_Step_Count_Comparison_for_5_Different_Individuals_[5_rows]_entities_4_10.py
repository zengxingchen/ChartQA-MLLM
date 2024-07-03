
import matplotlib.pyplot as plt
from datetime import datetime

data = [
    {'Date': '2023-01-01', 'Person A': 1567, 'Person B': 3890, 'Person C': 2745, 'Person D': 1678, 'Person E': 4870},
    {'Date': '2023-01-02', 'Person A': 1896, 'Person B': 3980, 'Person C': 3560, 'Person D': 2789, 'Person E': 5890},
    {'Date': '2023-01-03', 'Person A': 2400, 'Person B': 3200, 'Person C': 4020, 'Person D': 3090, 'Person E': 6234},
    {'Date': '2023-01-04', 'Person A': 2890, 'Person B': 4300, 'Person C': 4790, 'Person D': 3450, 'Person E': 5021},
    {'Date': '2023-01-05', 'Person A': 3350, 'Person B': 4500, 'Person C': 5200, 'Person D': 3800, 'Person E': 5500},
    {'Date': '2023-01-06', 'Person A': 3500, 'Person B': 4600, 'Person C': 5400, 'Person D': 3900, 'Person E': 5700},
    {'Date': '2023-01-07', 'Person A': 3700, 'Person B': 4700, 'Person C': 5600, 'Person D': 4000, 'Person E': 5850},
    {'Date': '2023-01-08', 'Person A': 3800, 'Person B': 4800, 'Person C': 5700, 'Person D': 4100, 'Person E': 5900},
    {'Date': '2023-01-09', 'Person A': 3900, 'Person B': 4900, 'Person C': 5800, 'Person D': 4200, 'Person E': 6000},
    {'Date': '2023-01-10', 'Person A': 4000, 'Person B': 5000, 'Person C': 5900, 'Person D': 4300, 'Person E': 6100}
]

dates = [datetime.strptime(d['Date'], '%Y-%m-%d') for d in data]
values_a = [d['Person A'] for d in data]
values_b = [d['Person B'] for d in data]
values_c = [d['Person C'] for d in data]
values_d = [d['Person D'] for d in data]
values_e = [d['Person E'] for d in data]

plt.figure(figsize=(10,6))

plt.plot(dates, values_a, color='#FF5733', marker='o', linestyle='-', label='Person A')
plt.plot(dates, values_b, color='#33FF57', marker='v', linestyle='--', label='Person B')
plt.plot(dates, values_c, color='#3357FF', marker='s', linestyle='-.', label='Person C')
plt.plot(dates, values_d, color='#FF33A6', marker='^', linestyle=':', label='Person D')
plt.plot(dates, values_e, color='#A633FF', marker='*', linestyle='-', label='Person E')

plt.title('Sports & Fitness: Weekly Step Counts')
plt.xlabel('Date')
plt.ylabel('Step Counts')
plt.xticks(dates, [d.strftime('%Y-%m-%d') for d in dates], rotation=45)
plt.legend(loc='upper left')
plt.tight_layout()
plt.gca().invert_yaxis()

plt.annotate('Lowest Step Count', xy=(dates[0], values_d[0]), xytext=(dates[0], values_d[0]+200),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()