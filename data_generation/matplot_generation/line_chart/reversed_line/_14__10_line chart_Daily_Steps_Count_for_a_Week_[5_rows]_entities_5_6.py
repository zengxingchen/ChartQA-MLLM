
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import pandas as pd

data = [
    {'Date': '2023-04-10', 'Productivity': 80},
    {'Date': '2023-04-11', 'Productivity': 85},
    {'Date': '2023-04-12', 'Productivity': 75},
    {'Date': '2023-04-13', 'Productivity': 90},
    {'Date': '2023-04-14', 'Productivity': 82},
    {'Date': '2023-04-15', 'Productivity': 88},
    {'Date': '2023-04-16', 'Productivity': 78},
    {'Date': '2023-04-17', 'Productivity': 81},
    {'Date': '2023-04-18', 'Productivity': 89},
    {'Date': '2023-04-19', 'Productivity': 76},
    {'Date': '2023-04-20', 'Productivity': 83},
    {'Date': '2023-04-21', 'Productivity': 84},
    {'Date': '2023-04-22', 'Productivity': 80},
    {'Date': '2023-04-23', 'Productivity': 77},
    {'Date': '2023-04-24', 'Productivity': 90},
    {'Date': '2023-04-25', 'Productivity': 74},
    {'Date': '2023-04-26', 'Productivity': 88},
    {'Date': '2023-04-27', 'Productivity': 83},
    {'Date': '2023-04-28', 'Productivity': 80},
    {'Date': '2023-04-29', 'Productivity': 86},
    {'Date': '2023-04-30', 'Productivity': 85}
]

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values('Date', inplace=True)

plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Productivity'], label='Daily Productivity', color='#1E90FF', linestyle='-', marker='o')
plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
plt.gcf().autofmt_xdate()

plt.title('Daily Productivity in April 2023', fontsize=16, pad=20)
plt.xlabel('Date')
plt.ylabel('Productivity Index')
plt.legend(loc='lower right')
plt.grid(True)

plt.gca().invert_yaxis()

annotations = {
    '2023-04-13': 'Peak productivity',
    '2023-04-25': 'Lowest productivity'
}
for date, label in annotations.items():
    plt.annotate(label, (pd.to_datetime(date), df[df['Date'] == pd.to_datetime(date)]['Productivity'].values[0]),
                 textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='red')

plt.show()