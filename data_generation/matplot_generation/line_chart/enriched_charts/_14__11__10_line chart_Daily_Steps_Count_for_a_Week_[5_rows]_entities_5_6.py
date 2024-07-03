
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import pandas as pd

data = [
    {'Date': '2023-04-01', 'Value': 35},
    {'Date': '2023-04-02', 'Value': 36},
    {'Date': '2023-04-03', 'Value': 38},
    {'Date': '2023-04-04', 'Value': 40},
    {'Date': '2023-04-05', 'Value': 37},
    {'Date': '2023-04-06', 'Value': 39},
    {'Date': '2023-04-07', 'Value': 41},
    {'Date': '2023-04-08', 'Value': 42},
    {'Date': '2023-04-09', 'Value': 40},
    {'Date': '2023-04-10', 'Value': 43},
    {'Date': '2023-04-11', 'Value': 41},
    {'Date': '2023-04-12', 'Value': 43},
    {'Date': '2023-04-13', 'Value': 45},
    {'Date': '2023-04-14', 'Value': 44},
    {'Date': '2023-04-15', 'Value': 47},
    {'Date': '2023-04-16', 'Value': 49},
    {'Date': '2023-04-17', 'Value': 50},
    {'Date': '2023-04-18', 'Value': 52},
    {'Date': '2023-04-19', 'Value': 51},
    {'Date': '2023-04-20', 'Value': 53},
    {'Date': '2023-04-21', 'Value': 52},
    {'Date': '2023-04-22', 'Value': 54},
    {'Date': '2023-04-23', 'Value': 55},
    {'Date': '2023-04-24', 'Value': 53},
    {'Date': '2023-04-25', 'Value': 52},
    {'Date': '2023-04-26', 'Value': 54},
    {'Date': '2023-04-27', 'Value': 55},
    {'Date': '2023-04-28', 'Value': 56},
    {'Date': '2023-04-29', 'Value': 58},
    {'Date': '2023-04-30', 'Value': 60}
]

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values('Date', inplace=True)

plt.figure(figsize=(16, 10))
plt.plot(df['Date'], df['Value'], label='Daily Blood Pressure', color='#FF5733', linestyle='-', marker='o')
plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
plt.gcf().autofmt_xdate()

plt.title('Daily Blood Pressure in April 2023', fontsize=18, pad=20)
plt.xlabel('Date')
plt.ylabel('Blood Pressure (mmHg)')
plt.legend(loc='upper left')
plt.grid(True)
plt.gca().invert_yaxis()

annotations = {
    '2023-04-01': 'Starting Point',
    '2023-04-19': 'Fluctuation Peak'
}
for date, label in annotations.items():
    plt.annotate(label, (pd.to_datetime(date), df[df['Date'] == pd.to_datetime(date)]['Value'].values[0]),
                 textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='blue')

plt.show()