
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

data = [
    {'Date': '2023-03-01', 'Reading Hours': 2.5, 'Book Sales': 150},
    {'Date': '2023-03-02', 'Reading Hours': 3.0, 'Book Sales': 200},
    {'Date': '2023-03-03', 'Reading Hours': 2.0, 'Book Sales': 180},
    {'Date': '2023-03-04', 'Reading Hours': 3.5, 'Book Sales': 220},
    {'Date': '2023-03-05', 'Reading Hours': 2.8, 'Book Sales': 190},
    {'Date': '2023-03-06', 'Reading Hours': 3.3, 'Book Sales': 210},
    {'Date': '2023-03-07', 'Reading Hours': 2.7, 'Book Sales': 195},
    {'Date': '2023-03-08', 'Reading Hours': 3.4, 'Book Sales': 225},
    {'Date': '2023-03-09', 'Reading Hours': 2.2, 'Book Sales': 170},
    {'Date': '2023-03-10', 'Reading Hours': 3.1, 'Book Sales': 205},
    {'Date': '2023-03-11', 'Reading Hours': 2.4, 'Book Sales': 180},
    {'Date': '2023-03-12', 'Reading Hours': 3.6, 'Book Sales': 230},
    {'Date': '2023-03-13', 'Reading Hours': 2.9, 'Book Sales': 200},
    {'Date': '2023-03-14', 'Reading Hours': 2.6, 'Book Sales': 185}
]

dates = [datetime.strptime(item['Date'], '%Y-%m-%d') for item in data]
reading_hours = [item['Reading Hours'] for item in data]
book_sales = [item['Book Sales'] for item in data]

plt.figure(figsize=(16, 8))
plt.plot(dates, reading_hours, marker='o', linestyle='-', color='#1f77b4', label='Reading Hours')
plt.plot(dates, book_sales, marker='s', linestyle='--', color='#ff7f0e', label='Book Sales')

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

plt.xlabel('Date')
plt.ylabel('Measurements')
plt.title('Daily Reading Hours and Book Sales Over Two Weeks', pad=30)
plt.legend(loc='upper left')
plt.grid(True)

plt.gcf().autofmt_xdate()

for i, txt in enumerate(reading_hours):
    plt.annotate(txt, (dates[i], reading_hours[i]), textcoords="offset points", xytext=(0,10), ha='center')

for i, txt in enumerate(book_sales):
    plt.annotate(txt, (dates[i], book_sales[i]), textcoords="offset points", xytext=(0,-15), ha='center', color='#ff7f0e')

plt.gca().invert_yaxis()

plt.show()