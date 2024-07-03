
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import pandas as pd

data = [
    {'Date': '2023-04-10', 'Temperature': 21},
    {'Date': '2023-04-11', 'Temperature': 23},
    {'Date': '2023-04-12', 'Temperature': 18},
    {'Date': '2023-04-13', 'Temperature': 26},
    {'Date': '2023-04-14', 'Temperature': 22},
    {'Date': '2023-04-15', 'Temperature': 24},
    {'Date': '2023-04-16', 'Temperature': 19},
    {'Date': '2023-04-17', 'Temperature': 21},
    {'Date': '2023-04-18', 'Temperature': 25},
    {'Date': '2023-04-19', 'Temperature': 20},
    {'Date': '2023-04-20', 'Temperature': 22},
    {'Date': '2023-04-21', 'Temperature': 23},
    {'Date': '2023-04-22', 'Temperature': 21},
    {'Date': '2023-04-23', 'Temperature': 19},
    {'Date': '2023-04-24', 'Temperature': 26},
    {'Date': '2023-04-25', 'Temperature': 18},
    {'Date': '2023-04-26', 'Temperature': 25},
    {'Date': '2023-04-27', 'Temperature': 22},
    {'Date': '2023-04-28', 'Temperature': 21},
    {'Date': '2023-04-29', 'Temperature': 24},
    {'Date': '2023-04-30', 'Temperature': 23}
]

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values('Date', inplace=True)

plt.figure(figsize=(12, 8))
plt.plot(df['Date'], df['Temperature'], label='Daily Temperature', color='#FF5733', linestyle='-', marker='o')
plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
plt.gcf().autofmt_xdate()

plt.title('Daily Temperature in April 2023', fontsize=16, pad=20)
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend(loc='upper left')
plt.grid(True)

# Adding annotations for specific dates
annotations = {
    '2023-04-13': 'Highest temp',
    '2023-04-25': 'Lowest temp'
}
for date, label in annotations.items():
    plt.annotate(label, (pd.to_datetime(date), df[df['Date'] == pd.to_datetime(date)]['Temperature'].values[0]),
                 textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='red')

plt.show()