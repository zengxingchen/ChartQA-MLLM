
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

data = [
    {'Date': '2023-03-01', 'ProductA': 150, 'ProductB': 45, 'ProductC': 30, 'ProductD': 100},
    {'Date': '2023-03-02', 'ProductA': 155, 'ProductB': 47, 'ProductC': 33, 'ProductD': 105},
    {'Date': '2023-03-03', 'ProductA': 160, 'ProductB': 50, 'ProductC': 35, 'ProductD': 110},
    {'Date': '2023-03-04', 'ProductA': 165, 'ProductB': 48, 'ProductC': 37, 'ProductD': 115},
    {'Date': '2023-03-05', 'ProductA': 170, 'ProductB': 52, 'ProductC': 40, 'ProductD': 120},
    {'Date': '2023-03-06', 'ProductA': 175, 'ProductB': 55, 'ProductC': 42, 'ProductD': 125},
    {'Date': '2023-03-07', 'ProductA': 180, 'ProductB': 57, 'ProductC': 44, 'ProductD': 130},
    {'Date': '2023-03-08', 'ProductA': 185, 'ProductB': 60, 'ProductC': 47, 'ProductD': 135},
    {'Date': '2023-03-09', 'ProductA': 190, 'ProductB': 62, 'ProductC': 49, 'ProductD': 140},
    {'Date': '2023-03-10', 'ProductA': 195, 'ProductB': 64, 'ProductC': 51, 'ProductD': 145},
    {'Date': '2023-03-11', 'ProductA': 200, 'ProductB': 67, 'ProductC': 54, 'ProductD': 150},
    {'Date': '2023-03-12', 'ProductA': 205, 'ProductB': 70, 'ProductC': 56, 'ProductD': 155},
    {'Date': '2023-03-13', 'ProductA': 210, 'ProductB': 72, 'ProductC': 58, 'ProductD': 160},
    {'Date': '2023-03-14', 'ProductA': 215, 'ProductB': 75, 'ProductC': 61, 'ProductD': 165},
    {'Date': '2023-03-15', 'ProductA': 220, 'ProductB': 77, 'ProductC': 63, 'ProductD': 170}
]

dates = [datetime.strptime(d['Date'], '%Y-%m-%d') for d in data]
product_a_sales = [d['ProductA'] for d in data]
product_b_sales = [d['ProductB'] for d in data]
product_c_sales = [d['ProductC'] for d in data]
product_d_sales = [d['ProductD'] for d in data]

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(dates, product_a_sales, label='Product A', color='#1f77b4', linestyle='-', marker='o')
ax.plot(dates, product_b_sales, label='Product B', color='#ff7f0e', linestyle='--', marker='s')
ax.plot(dates, product_c_sales, label='Product C', color='#2ca02c', linestyle='-.', marker='^')
ax.plot(dates, product_d_sales, label='Product D', color='#d62728', linestyle=':', marker='x')

ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gcf().autofmt_xdate()

ax.legend()

plt.title('Sales Trend of Various Products')
plt.xlabel('Date')
plt.ylabel('Units Sold')

for i, txt in enumerate(product_a_sales):
    ax.annotate(txt, (dates[i], product_a_sales[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.grid(True)

plt.show()