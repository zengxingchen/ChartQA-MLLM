
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

data = [
    {'Date': '2023-03-01', 'Happiness Level': 5},
    {'Date': '2023-03-02', 'Happiness Level': 6},
    {'Date': '2023-03-03', 'Happiness Level': 5.5},
    {'Date': '2023-03-04', 'Happiness Level': 7},
    {'Date': '2023-03-05', 'Happiness Level': 6.8},
    {'Date': '2023-03-06', 'Happiness Level': 7.5},
    {'Date': '2023-03-07', 'Happiness Level': 8},
    {'Date': '2023-03-08', 'Happiness Level': 9},
    {'Date': '2023-03-09', 'Happiness Level': 8.7},
    {'Date': '2023-03-10', 'Happiness Level': 9.5},
    {'Date': '2023-03-11', 'Happiness Level': 9.4},
    {'Date': '2023-03-12', 'Happiness Level': 10}
]

dates = [datetime.strptime(item['Date'], "%Y-%m-%d") for item in data]
levels = [item['Happiness Level'] for item in data]

plt.figure(figsize=(10, 6))

plt.plot(dates, levels, 
         color='#2ca02c',         # Line color
         linestyle='-',           # Line style
         linewidth=2,             # Line width
         marker='o',              # Marker style
         markersize=8,            # Marker size
         markerfacecolor='#ffbb78', # Marker face color
         markeredgewidth=1.5,       # Marker edge width
         markeredgecolor='#1f77b4') # Marker edge color

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

for date, level in zip(dates, levels):
    plt.text(date, level + 0.2, f'{level}', ha='center', va='bottom')

plt.title('Daily Happiness Levels Over a Week', pad=20, fontsize=14)
plt.xlabel('Date')
plt.ylabel('Happiness Level')

plt.gca().invert_yaxis()

plt.gcf().autofmt_xdate()

plt.grid(True)

plt.show()