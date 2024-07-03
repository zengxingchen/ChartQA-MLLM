
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import pandas as pd

data = [
    {'Date': '2023-05-01', 'Steps': 5000},
    {'Date': '2023-05-02', 'Steps': 7000},
    {'Date': '2023-05-03', 'Steps': 8000},
    {'Date': '2023-05-04', 'Steps': 6500},
    {'Date': '2023-05-05', 'Steps': 9000},
    {'Date': '2023-05-06', 'Steps': 7200},
    {'Date': '2023-05-07', 'Steps': 8500},
    {'Date': '2023-05-08', 'Steps': 7800},
    {'Date': '2023-05-09', 'Steps': 9500},
    {'Date': '2023-05-10', 'Steps': 6800},
    {'Date': '2023-05-11', 'Steps': 8800},
    {'Date': '2023-05-12', 'Steps': 9300},
    {'Date': '2023-05-13', 'Steps': 8200},
    {'Date': '2023-05-14', 'Steps': 7800},
    {'Date': '2023-05-15', 'Steps': 7000},
    {'Date': '2023-05-16', 'Steps': 8900},
    {'Date': '2023-05-17', 'Steps': 9500},
    {'Date': '2023-05-18', 'Steps': 9900},
    {'Date': '2023-05-19', 'Steps': 8700},
    {'Date': '2023-05-20', 'Steps': 6500},
    {'Date': '2023-05-21', 'Steps': 9300},
    {'Date': '2023-05-22', 'Steps': 8100},
    {'Date': '2023-05-23', 'Steps': 7700},
    {'Date': '2023-05-24', 'Steps': 9000},
    {'Date': '2023-05-25', 'Steps': 7500},
    {'Date': '2023-05-26', 'Steps': 9400},
    {'Date': '2023-05-27', 'Steps': 8800},
    {'Date': '2023-05-28', 'Steps': 8100},
    {'Date': '2023-05-29', 'Steps': 7900},
    {'Date': '2023-05-30', 'Steps': 8300},
    {'Date': '2023-05-31', 'Steps': 9200}
]

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values('Date', inplace=True)

plt.figure(figsize=(14, 10))
plt.plot(df['Date'], df['Steps'], label='Daily Steps', color='#1f77b4', linestyle='-', marker='o')
plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
plt.gcf().autofmt_xdate()

plt.title('Daily Steps in May 2023', fontsize=18, pad=25)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Steps', fontsize=14)
plt.legend(loc='upper right')
plt.grid(True)

annotations = {
    '2023-05-18': 'Highest steps',
    '2023-05-01': 'Lowest steps'
}
for date, label in annotations.items():
    plt.annotate(label, (pd.to_datetime(date), df[df['Date'] == pd.to_datetime(date)]['Steps'].values[0]),
                 textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, color='green')

plt.show()