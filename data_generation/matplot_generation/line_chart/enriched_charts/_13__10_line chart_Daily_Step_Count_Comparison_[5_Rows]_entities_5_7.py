
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

data = [
    {'Date': '2023-03-01', 'Person A Sales': 5000, 'Person B Sales': 7000},
    {'Date': '2023-03-02', 'Person A Sales': 5200, 'Person B Sales': 7200},
    {'Date': '2023-03-03', 'Person A Sales': 5400, 'Person B Sales': 7400},
    {'Date': '2023-03-04', 'Person A Sales': 5600, 'Person B Sales': 7600},
    {'Date': '2023-03-05', 'Person A Sales': 5800, 'Person B Sales': 7800},
    {'Date': '2023-03-06', 'Person A Sales': 6000, 'Person B Sales': 8000},
    {'Date': '2023-03-07', 'Person A Sales': 6200, 'Person B Sales': 8200},
    {'Date': '2023-03-08', 'Person A Sales': 6400, 'Person B Sales': 8400},
    {'Date': '2023-03-09', 'Person A Sales': 6600, 'Person B Sales': 8600},
    {'Date': '2023-03-10', 'Person A Sales': 6800, 'Person B Sales': 8800}
]

dates = [datetime.strptime(d['Date'], '%Y-%m-%d') for d in data]
person_a_sales = [d['Person A Sales'] for d in data]
person_b_sales = [d['Person B Sales'] for d in data]

plt.figure(figsize=(14, 8))

plt.plot(dates, person_a_sales, label='Person A', color='#3498db', linestyle='-', marker='o', linewidth=2)
plt.plot(dates, person_b_sales, label='Person B', color='#e74c3c', linestyle='--', marker='x', linewidth=2)

plt.title('Daily Sales Comparison: Business & Entrepreneurship', pad=20)
plt.xlabel('Date')
plt.ylabel('Sales in USD')
plt.legend(loc='upper left')
plt.grid(True)

plt.gca().invert_yaxis()

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

plt.gcf().autofmt_xdate()

for i, txt in enumerate(person_a_sales):
    plt.annotate(txt, (dates[i], person_a_sales[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
for i, txt in enumerate(person_b_sales):
    plt.annotate(txt, (dates[i], person_b_sales[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)

plt.show()