
import matplotlib.pyplot as plt
from datetime import datetime

data = [
    {'Date': '2023-01-01', 'Person A': 4567, 'Person B': 7890, 'Person C': 6745, 'Person D': 5678, 'Person E': 9870},
    {'Date': '2023-01-02', 'Person A': 5896, 'Person B': 7980, 'Person C': 7560, 'Person D': 6789, 'Person E': 10890},
    {'Date': '2023-01-03', 'Person A': 6400, 'Person B': 7200, 'Person C': 8020, 'Person D': 7090, 'Person E': 11234},
    {'Date': '2023-01-04', 'Person A': 6890, 'Person B': 8300, 'Person C': 8790, 'Person D': 7450, 'Person E': 10021},
    {'Date': '2023-01-05', 'Person A': 7350, 'Person B': 8500, 'Person C': 9200, 'Person D': 7800, 'Person E': 10500},
    {'Date': '2023-01-06', 'Person A': 7500, 'Person B': 8600, 'Person C': 9400, 'Person D': 7900, 'Person E': 10700},
    {'Date': '2023-01-07', 'Person A': 7700, 'Person B': 8700, 'Person C': 9600, 'Person D': 8000, 'Person E': 10850},
    {'Date': '2023-01-08', 'Person A': 7800, 'Person B': 8800, 'Person C': 9700, 'Person D': 8100, 'Person E': 10900},
    {'Date': '2023-01-09', 'Person A': 7900, 'Person B': 8900, 'Person C': 9800, 'Person D': 8200, 'Person E': 11000},
    {'Date': '2023-01-10', 'Person A': 8000, 'Person B': 9000, 'Person C': 9900, 'Person D': 8300, 'Person E': 11100}
]

dates = [datetime.strptime(d['Date'], '%Y-%m-%d') for d in data]
values_a = [d['Person A'] for d in data]
values_b = [d['Person B'] for d in data]
values_c = [d['Person C'] for d in data]
values_d = [d['Person D'] for d in data]
values_e = [d['Person E'] for d in data]

plt.figure(figsize=(12,7))

plt.plot(dates, values_a, color='#1f77b4', marker='o', linestyle='-', label='Person A')
plt.plot(dates, values_b, color='#ff7f0e', marker='v', linestyle='--', label='Person B')
plt.plot(dates, values_c, color='#2ca02c', marker='s', linestyle='-.', label='Person C')
plt.plot(dates, values_d, color='#d62728', marker='^', linestyle=':', label='Person D')
plt.plot(dates, values_e, color='#9467bd', marker='*', linestyle='-', label='Person E')

plt.title('Trend of Daily Productivity Scores')
plt.xlabel('Date')
plt.ylabel('Productivity Scores')
plt.xticks(dates, [d.strftime('%Y-%m-%d') for d in dates], rotation=45)
plt.legend()
plt.tight_layout()

plt.annotate('Highest Score', xy=(dates[-1], values_a[-1]), xytext=(dates[-1], values_a[-1]+200),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()