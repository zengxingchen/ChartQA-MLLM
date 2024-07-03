
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import pandas as pd

data = [
    {'Date': '2023-05-01', 'Views': 5000},
    {'Date': '2023-05-02', 'Views': 4800},
    {'Date': '2023-05-03', 'Views': 4500},
    {'Date': '2023-05-04', 'Views': 4700},
    {'Date': '2023-05-05', 'Views': 4300},
    {'Date': '2023-05-06', 'Views': 4100},
    {'Date': '2023-05-07', 'Views': 4200},
    {'Date': '2023-05-08', 'Views': 3900},
    {'Date': '2023-05-09', 'Views': 3800},
    {'Date': '2023-05-10', 'Views': 3600},
    {'Date': '2023-05-11', 'Views': 3500},
    {'Date': '2023-05-12', 'Views': 3300},
    {'Date': '2023-05-13', 'Views': 3100},
    {'Date': '2023-05-14', 'Views': 3000},
    {'Date': '2023-05-15', 'Views': 3200},
    {'Date': '2023-05-16', 'Views': 3400},
    {'Date': '2023-05-17', 'Views': 3600},
    {'Date': '2023-05-18', 'Views': 3800},
    {'Date': '2023-05-19', 'Views': 3500},
    {'Date': '2023-05-20', 'Views': 3400},
    {'Date': '2023-05-21', 'Views': 3300},
    {'Date': '2023-05-22', 'Views': 3100},
    {'Date': '2023-05-23', 'Views': 2900},
    {'Date': '2023-05-24', 'Views': 2700},
    {'Date': '2023-05-25', 'Views': 2600},
    {'Date': '2023-05-26', 'Views': 2500},
    {'Date': '2023-05-27', 'Views': 2300},
    {'Date': '2023-05-28', 'Views': 2200},
    {'Date': '2023-05-29', 'Views': 2000},
    {'Date': '2023-05-30', 'Views': 1900},
    {'Date': '2023-05-31', 'Views': 1800}
]

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values('Date', inplace=True)

plt.figure(figsize=(16, 12))
plt.plot(df['Date'], df['Views'], label='Daily Views', color='#ff5733', linestyle='-', marker='o')
plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
plt.gcf().autofmt_xdate()
plt.gca().invert_yaxis()

plt.title('Daily Video Views in May 2023', fontsize=18, pad=25)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Views', fontsize=14)
plt.legend(loc='upper left')
plt.grid(True)

annotations = {
    '2023-05-01': 'Highest views',
    '2023-05-31': 'Lowest views'
}
for date, label in annotations.items():
    plt.annotate(label, (pd.to_datetime(date), df[df['Date'] == pd.to_datetime(date)]['Views'].values[0]),
                 textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, color='blue')

plt.show()