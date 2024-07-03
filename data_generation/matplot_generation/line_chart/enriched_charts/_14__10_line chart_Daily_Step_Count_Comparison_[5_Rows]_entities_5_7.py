
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

data = [
    {'Date': '2023-03-01', 'Person A Steps': 8000, 'Person B Steps': 6000},
    {'Date': '2023-03-02', 'Person A Steps': 7500, 'Person B Steps': 5000},
    {'Date': '2023-03-03', 'Person A Steps': 9000, 'Person B Steps': 7000},
    {'Date': '2023-03-04', 'Person A Steps': 7000, 'Person B Steps': 4500},
    {'Date': '2023-03-05', 'Person A Steps': 10000, 'Person B Steps': 8500},
    {'Date': '2023-03-06', 'Person A Steps': 8500, 'Person B Steps': 6500},
    {'Date': '2023-03-07', 'Person A Steps': 9000, 'Person B Steps': 7000},
    {'Date': '2023-03-08', 'Person A Steps': 9500, 'Person B Steps': 7500},
    {'Date': '2023-03-09', 'Person A Steps': 10500, 'Person B Steps': 9500},
    {'Date': '2023-03-10', 'Person A Steps': 12000, 'Person B Steps': 10000}
]

dates = [datetime.strptime(d['Date'], '%Y-%m-%d') for d in data]
person_a_steps = [d['Person A Steps'] for d in data]
person_b_steps = [d['Person B Steps'] for d in data]

plt.figure(figsize=(14, 8))

plt.plot(dates, person_a_steps, label='Person A', color='#3498db', linestyle='-', marker='o', linewidth=2)
plt.plot(dates, person_b_steps, label='Person B', color='#e74c3c', linestyle='--', marker='x', linewidth=2)

plt.title('Daily Step Count: Fitness & Health', pad=40)
plt.xlabel('Date')
plt.ylabel('Number of Steps')
plt.legend(loc='lower right')
plt.grid(True)
plt.gca().invert_yaxis()

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

plt.gcf().autofmt_xdate()

for i, txt in enumerate(person_a_steps):
    plt.annotate(txt, (dates[i], person_a_steps[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
for i, txt in enumerate(person_b_steps):
    plt.annotate(txt, (dates[i], person_b_steps[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)

plt.show()