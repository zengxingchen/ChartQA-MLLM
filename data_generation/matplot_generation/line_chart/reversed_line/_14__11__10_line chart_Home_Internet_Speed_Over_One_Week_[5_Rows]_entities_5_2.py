
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

data = [
    {'Date': '2023-04-01', 'Reading Time (minutes)': 45, 'Stress Level': 6},
    {'Date': '2023-04-02', 'Reading Time (minutes)': 50, 'Stress Level': 5},
    {'Date': '2023-04-03', 'Reading Time (minutes)': 55, 'Stress Level': 4},
    {'Date': '2023-04-04', 'Reading Time (minutes)': 60, 'Stress Level': 3},
    {'Date': '2023-04-05', 'Reading Time (minutes)': 65, 'Stress Level': 2},
    {'Date': '2023-04-06', 'Reading Time (minutes)': 70, 'Stress Level': 1},
    {'Date': '2023-04-07', 'Reading Time (minutes)': 75, 'Stress Level': 0},
    {'Date': '2023-04-08', 'Reading Time (minutes)': 80, 'Stress Level': 1},
    {'Date': '2023-04-09', 'Reading Time (minutes)': 85, 'Stress Level': 2},
    {'Date': '2023-04-10', 'Reading Time (minutes)': 90, 'Stress Level': 3},
    {'Date': '2023-04-11', 'Reading Time (minutes)': 95, 'Stress Level': 4},
    {'Date': '2023-04-12', 'Reading Time (minutes)': 100, 'Stress Level': 5},
    {'Date': '2023-04-13', 'Reading Time (minutes)': 105, 'Stress Level': 6},
    {'Date': '2023-04-14', 'Reading Time (minutes)': 110, 'Stress Level': 7}
]

dates = [datetime.strptime(item['Date'], '%Y-%m-%d') for item in data]
reading_time = [item['Reading Time (minutes)'] for item in data]
stress_level = [item['Stress Level'] for item in data]

plt.figure(figsize=(16, 9))

plt.plot(dates, reading_time, marker='o', linestyle='-', color='#1f77b4', label='Reading Time (minutes)')
plt.plot(dates, stress_level, marker='s', linestyle='--', color='#ff7f0e', label='Stress Level')

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Daily Reading Time and Stress Level Over Two Weeks', pad=20)
plt.legend(loc='upper left')
plt.grid(True)
plt.gcf().autofmt_xdate()

for i, txt in enumerate(reading_time):
    plt.annotate(txt, (dates[i], reading_time[i]), textcoords="offset points", xytext=(0,10), ha='center')

for i, txt in enumerate(stress_level):
    plt.annotate(txt, (dates[i], stress_level[i]), textcoords="offset points", xytext=(0,-15), ha='center', color='#ff7f0e')

plt.gca().invert_yaxis()

plt.show()