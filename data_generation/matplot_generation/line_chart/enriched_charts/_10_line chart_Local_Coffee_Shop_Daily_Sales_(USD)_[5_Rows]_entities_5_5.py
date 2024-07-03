
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

data = [
    {'Date': '2023-03-01', 'Stock Price': 100},
    {'Date': '2023-03-02', 'Stock Price': 105},
    {'Date': '2023-03-03', 'Stock Price': 102},
    {'Date': '2023-03-04', 'Stock Price': 108},
    {'Date': '2023-03-05', 'Stock Price': 107},
    {'Date': '2023-03-06', 'Stock Price': 110},
    {'Date': '2023-03-07', 'Stock Price': 115},
    {'Date': '2023-03-08', 'Stock Price': 120},
    {'Date': '2023-03-09', 'Stock Price': 117},
    {'Date': '2023-03-10', 'Stock Price': 123},
    {'Date': '2023-03-11', 'Stock Price': 122},
    {'Date': '2023-03-12', 'Stock Price': 125}
]

dates = [datetime.strptime(item['Date'], "%Y-%m-%d") for item in data]
prices = [item['Stock Price'] for item in data]

plt.figure(figsize=(12, 8))

plt.plot(dates, prices, 
         color='#1f77b4',         # Line color
         linestyle='-',           # Line style
         linewidth=2,             # Line width
         marker='s',              # Marker style
         markersize=10,           # Marker size
         markerfacecolor='#ff7f0e', # Marker face color
         markeredgewidth=2,       # Marker edge width
         markeredgecolor='#d62728') # Marker edge color

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

for date, price in zip(dates, prices):
    plt.text(date, price + 1, f'{price}', ha='center', va='bottom')

plt.title('Stock Prices Over a Week', pad=20)
plt.xlabel('Date')
plt.ylabel('Stock Price')

plt.gcf().autofmt_xdate()

plt.grid(True)

plt.show()