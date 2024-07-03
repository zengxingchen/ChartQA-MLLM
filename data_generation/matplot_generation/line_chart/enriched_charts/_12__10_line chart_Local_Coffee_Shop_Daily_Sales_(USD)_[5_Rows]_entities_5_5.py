
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

data = [
    {'Date': '2023-03-01', 'New Technologies Adoption Rate': 5},
    {'Date': '2023-03-02', 'New Technologies Adoption Rate': 15},
    {'Date': '2023-03-03', 'New Technologies Adoption Rate': 10},
    {'Date': '2023-03-04', 'New Technologies Adoption Rate': 20},
    {'Date': '2023-03-05', 'New Technologies Adoption Rate': 25},
    {'Date': '2023-03-06', 'New Technologies Adoption Rate': 22},
    {'Date': '2023-03-07', 'New Technologies Adoption Rate': 28},
    {'Date': '2023-03-08', 'New Technologies Adoption Rate': 35},
    {'Date': '2023-03-09', 'New Technologies Adoption Rate': 32},
    {'Date': '2023-03-10', 'New Technologies Adoption Rate': 40},
    {'Date': '2023-03-11', 'New Technologies Adoption Rate': 38},
    {'Date': '2023-03-12', 'New Technologies Adoption Rate': 45},
    {'Date': '2023-03-13', 'New Technologies Adoption Rate': 50},
    {'Date': '2023-03-14', 'New Technologies Adoption Rate': 55},
    {'Date': '2023-03-15', 'New Technologies Adoption Rate': 52},
    {'Date': '2023-03-16', 'New Technologies Adoption Rate': 60},
    {'Date': '2023-03-17', 'New Technologies Adoption Rate': 62},
    {'Date': '2023-03-18', 'New Technologies Adoption Rate': 65},
    {'Date': '2023-03-19', 'New Technologies Adoption Rate': 70},
    {'Date': '2023-03-20', 'New Technologies Adoption Rate': 72}
]

dates = [datetime.strptime(item['Date'], "%Y-%m-%d") for item in data]
adoption_rates = [item['New Technologies Adoption Rate'] for item in data]

plt.figure(figsize=(14, 10))

plt.plot(dates, adoption_rates, 
         color='#2ca02c',         # Line color
         linestyle='-',           # Line style
         linewidth=3,             # Line width
         marker='o',              # Marker style
         markersize=8,            # Marker size
         markerfacecolor='#ffbb78', # Marker face color
         markeredgewidth=1,       # Marker edge width
         markeredgecolor='#ff7f0e') # Marker edge color

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

for date, rate in zip(dates, adoption_rates):
    plt.text(date, rate + 1, f'{rate}%', ha='center', va='bottom')

plt.title('New Technologies Adoption Rate Over Time', pad=30)
plt.xlabel('Date')
plt.ylabel('Adoption Rate (%)')

plt.gcf().autofmt_xdate()

plt.grid(True)
plt.show()