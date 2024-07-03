
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

data = [
    {'Date': '2023-03-01', 'Stock Price': 150},
    {'Date': '2023-03-02', 'Stock Price': 145},
    {'Date': '2023-03-03', 'Stock Price': 148},
    {'Date': '2023-03-04', 'Stock Price': 140},
    {'Date': '2023-03-05', 'Stock Price': 135},
    {'Date': '2023-03-06', 'Stock Price': 130},
    {'Date': '2023-03-07', 'Stock Price': 125},
    {'Date': '2023-03-08', 'Stock Price': 120},
    {'Date': '2023-03-09', 'Stock Price': 115},
    {'Date': '2023-03-10', 'Stock Price': 110},
    {'Date': '2023-03-11', 'Stock Price': 105},
    {'Date': '2023-03-12', 'Stock Price': 100},
    {'Date': '2023-03-13', 'Stock Price': 110},
    {'Date': '2023-03-14', 'Stock Price': 115},
    {'Date': '2023-03-15', 'Stock Price': 120},
    {'Date': '2023-03-16', 'Stock Price': 125},
    {'Date': '2023-03-17', 'Stock Price': 130},
    {'Date': '2023-03-18', 'Stock Price': 135},
    {'Date': '2023-03-19', 'Stock Price': 140},
    {'Date': '2023-03-20', 'Stock Price': 145},
    {'Date': '2023-03-21', 'Stock Price': 150}
]

dates = [datetime.strptime(item['Date'], "%Y-%m-%d") for item in data]
prices = [item['Stock Price'] for item in data]

plt.figure(figsize=(14, 9))

plt.plot(dates, prices, 
         color='#00429d',         # Line color
         linestyle='-',           # Line style
         linewidth=2,             # Line width
         marker='o',              # Marker style
         markersize=8,            # Marker size
         markerfacecolor='#ffa600', # Marker face color
         markeredgewidth=2,       # Marker edge width
         markeredgecolor='#d62728') # Marker edge color

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

for date, price in zip(dates, prices):
    plt.text(date, price + 1, f'{price}', ha='center', va='bottom')

plt.title('Future Technologies & Society: Tech Stock Prices Over Time', pad=20)
plt.xlabel('Date')
plt.ylabel('Tech Stock Price')

plt.gcf().autofmt_xdate()

plt.grid(True)

plt.show()