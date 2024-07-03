
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import pandas as pd

data = [
    {'Date': '2023-04-01', 'Value': 15},
    {'Date': '2023-04-02', 'Value': 17},
    {'Date': '2023-04-03', 'Value': 16},
    {'Date': '2023-04-04', 'Value': 18},
    {'Date': '2023-04-05', 'Value': 20},
    {'Date': '2023-04-06', 'Value': 19},
    {'Date': '2023-04-07', 'Value': 21},
    {'Date': '2023-04-08', 'Value': 22},
    {'Date': '2023-04-09', 'Value': 20},
    {'Date': '2023-04-10', 'Value': 23},
    {'Date': '2023-04-11', 'Value': 21},
    {'Date': '2023-04-12', 'Value': 22},
    {'Date': '2023-04-13', 'Value': 24},
    {'Date': '2023-04-14', 'Value': 23},
    {'Date': '2023-04-15', 'Value': 25},
    {'Date': '2023-04-16', 'Value': 27},
    {'Date': '2023-04-17', 'Value': 26},
    {'Date': '2023-04-18', 'Value': 28},
    {'Date': '2023-04-19', 'Value': 29},
    {'Date': '2023-04-20', 'Value': 28},
    {'Date': '2023-04-21', 'Value': 27},
    {'Date': '2023-04-22', 'Value': 25},
    {'Date': '2023-04-23', 'Value': 24},
    {'Date': '2023-04-24', 'Value': 22},
    {'Date': '2023-04-25', 'Value': 21},
    {'Date': '2023-04-26', 'Value': 23},
    {'Date': '2023-04-27', 'Value': 22},
    {'Date': '2023-04-28', 'Value': 24},
    {'Date': '2023-04-29', 'Value': 23},
    {'Date': '2023-04-30', 'Value': 26}
]

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values('Date', inplace=True)

plt.figure(figsize=(14, 9))
plt.plot(df['Date'], df['Value'], label='Daily Humidity', color='#1f77b4', linestyle='-', marker='o')
plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
plt.gcf().autofmt_xdate()

plt.title('Daily Humidity in April 2023', fontsize=18, pad=20)
plt.xlabel('Date')
plt.ylabel('Humidity (%)')
plt.legend(loc='upper right')
plt.grid(True)

annotations = {
    '2023-04-19': 'Peak Humidity',
    '2023-04-01': 'Lowest Humidity'
}
for date, label in annotations.items():
    plt.annotate(label, (pd.to_datetime(date), df[df['Date'] == pd.to_datetime(date)]['Value'].values[0]),
                 textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='red')

plt.show()