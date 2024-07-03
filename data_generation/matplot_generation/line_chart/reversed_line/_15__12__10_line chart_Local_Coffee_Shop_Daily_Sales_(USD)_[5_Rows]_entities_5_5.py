
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

data = [
    {'Date': '2023-03-01', 'Average Rainfall (mm)': 72},
    {'Date': '2023-03-02', 'Average Rainfall (mm)': 70},
    {'Date': '2023-03-03', 'Average Rainfall (mm)': 68},
    {'Date': '2023-03-04', 'Average Rainfall (mm)': 65},
    {'Date': '2023-03-05', 'Average Rainfall (mm)': 62},
    {'Date': '2023-03-06', 'Average Rainfall (mm)': 60},
    {'Date': '2023-03-07', 'Average Rainfall (mm)': 58},
    {'Date': '2023-03-08', 'Average Rainfall (mm)': 55},
    {'Date': '2023-03-09', 'Average Rainfall (mm)': 53},
    {'Date': '2023-03-10', 'Average Rainfall (mm)': 52},
    {'Date': '2023-03-11', 'Average Rainfall (mm)': 50},
    {'Date': '2023-03-12', 'Average Rainfall (mm)': 48},
    {'Date': '2023-03-13', 'Average Rainfall (mm)': 45},
    {'Date': '2023-03-14', 'Average Rainfall (mm)': 43},
    {'Date': '2023-03-15', 'Average Rainfall (mm)': 42},
    {'Date': '2023-03-16', 'Average Rainfall (mm)': 40},
    {'Date': '2023-03-17', 'Average Rainfall (mm)': 38},
    {'Date': '2023-03-18', 'Average Rainfall (mm)': 35},
    {'Date': '2023-03-19', 'Average Rainfall (mm)': 33},
    {'Date': '2023-03-20', 'Average Rainfall (mm)': 30}
]

dates = [datetime.strptime(item['Date'], "%Y-%m-%d") for item in data]
rainfall = [item['Average Rainfall (mm)'] for item in data]

plt.figure(figsize=(16, 8))

plt.plot(dates, rainfall, 
         color='#1f77b4',         # Line color
         linestyle='-',           # Line style
         linewidth=3,             # Line width
         marker='s',              # Marker style
         markersize=10,           # Marker size
         markerfacecolor='#aec7e8', # Marker face color
         markeredgewidth=1,       # Marker edge width
         markeredgecolor='#ff7f0e') # Marker edge color

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

for date, rain in zip(dates, rainfall):
    plt.text(date, rain + 1, f'{rain} mm', ha='center', va='bottom')

plt.title('Average Rainfall Over Time', pad=20)
plt.xlabel('Date')
plt.ylabel('Rainfall (mm)')
plt.gca().invert_yaxis()

plt.gcf().autofmt_xdate()

plt.grid(True)
plt.show()