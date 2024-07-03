
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import pandas as pd

data = [
    {'Date': '2023-04-01', 'Distance': 3},
    {'Date': '2023-04-02', 'Distance': 4},
    {'Date': '2023-04-03', 'Distance': 2},
    {'Date': '2023-04-04', 'Distance': 5},
    {'Date': '2023-04-05', 'Distance': 6},
    {'Date': '2023-04-06', 'Distance': 7},
    {'Date': '2023-04-07', 'Distance': 5},
    {'Date': '2023-04-08', 'Distance': 8},
    {'Date': '2023-04-09', 'Distance': 6},
    {'Date': '2023-04-10', 'Distance': 9},
    {'Date': '2023-04-11', 'Distance': 11},
    {'Date': '2023-04-12', 'Distance': 10},
    {'Date': '2023-04-13', 'Distance': 13},
    {'Date': '2023-04-14', 'Distance': 15},
    {'Date': '2023-04-15', 'Distance': 14},
    {'Date': '2023-04-16', 'Distance': 17},
    {'Date': '2023-04-17', 'Distance': 19},
    {'Date': '2023-04-18', 'Distance': 18},
    {'Date': '2023-04-19', 'Distance': 20},
    {'Date': '2023-04-20', 'Distance': 21},
    {'Date': '2023-04-21', 'Distance': 20},
    {'Date': '2023-04-22', 'Distance': 22},
    {'Date': '2023-04-23', 'Distance': 23},
    {'Date': '2023-04-24', 'Distance': 25},
    {'Date': '2023-04-25', 'Distance': 24},
    {'Date': '2023-04-26', 'Distance': 26},
    {'Date': '2023-04-27', 'Distance': 27},
    {'Date': '2023-04-28', 'Distance': 28},
    {'Date': '2023-04-29', 'Distance': 29},
    {'Date': '2023-04-30', 'Distance': 30}
]

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values('Date', inplace=True)

plt.figure(figsize=(12, 8))
plt.plot(df['Date'], df['Distance'], label='Daily Running Distance', color='#1f77b4', linestyle='-', marker='o')
plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
plt.gcf().autofmt_xdate()
plt.gca().invert_yaxis()

plt.title('Daily Running Distance in April 2023', fontsize=18, pad=20)
plt.xlabel('Date')
plt.ylabel('Distance (km)')
plt.legend(loc='upper right')
plt.grid(True)

annotations = {
    '2023-04-01': 'Start Running',
    '2023-04-19': 'Peak Distance'
}
for date, label in annotations.items():
    plt.annotate(label, (pd.to_datetime(date), df[df['Date'] == pd.to_datetime(date)]['Distance'].values[0]),
                 textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='red')

plt.show()