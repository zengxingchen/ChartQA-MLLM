
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

data = [
    {'Date': '2023-03-01', 'Daily Steps Count': 5000},
    {'Date': '2023-03-02', 'Daily Steps Count': 5200},
    {'Date': '2023-03-03', 'Daily Steps Count': 5400},
    {'Date': '2023-03-04', 'Daily Steps Count': 5300},
    {'Date': '2023-03-05', 'Daily Steps Count': 5500},
    {'Date': '2023-03-06', 'Daily Steps Count': 5600},
    {'Date': '2023-03-07', 'Daily Steps Count': 5800},
    {'Date': '2023-03-08', 'Daily Steps Count': 6000},
    {'Date': '2023-03-09', 'Daily Steps Count': 5900},
    {'Date': '2023-03-10', 'Daily Steps Count': 6100},
    {'Date': '2023-03-11', 'Daily Steps Count': 6200},
    {'Date': '2023-03-12', 'Daily Steps Count': 6400},
    {'Date': '2023-03-13', 'Daily Steps Count': 6600},
    {'Date': '2023-03-14', 'Daily Steps Count': 6500},
    {'Date': '2023-03-15', 'Daily Steps Count': 6700},
    {'Date': '2023-03-16', 'Daily Steps Count': 6800},
    {'Date': '2023-03-17', 'Daily Steps Count': 7000},
    {'Date': '2023-03-18', 'Daily Steps Count': 7200},
    {'Date': '2023-03-19', 'Daily Steps Count': 7100},
    {'Date': '2023-03-20', 'Daily Steps Count': 7300},
    {'Date': '2023-03-21', 'Daily Steps Count': 7500}
]

dates = [datetime.strptime(item['Date'], "%Y-%m-%d") for item in data]
steps = [item['Daily Steps Count'] for item in data]

plt.figure(figsize=(16, 10))

plt.plot(dates, steps, 
         color='#1f77b4',          # Line color
         linestyle='-',            # Line style
         linewidth=2,              # Line width
         marker='o',               # Marker style
         markersize=8,             # Marker size
         markerfacecolor='#ff7f0e', # Marker face color
         markeredgewidth=2,        # Marker edge width
         markeredgecolor='#2ca02c') # Marker edge color

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

for date, step in zip(dates, steps):
    plt.text(date, step + 100, f'{step}', ha='center', va='bottom')

plt.title('Health & Psychology: Daily Steps Count Over Time', pad=20)
plt.xlabel('Date')
plt.ylabel('Daily Steps Count')
plt.gca().invert_yaxis()

plt.gcf().autofmt_xdate()

plt.grid(True)

plt.show()