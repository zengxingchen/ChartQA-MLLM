import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

data = {
    'Date': [
        '2024-06-01', '2024-06-02', '2024-06-03', '2024-06-04', '2024-06-05',
        '2024-06-06', '2024-06-07', '2024-06-08', '2024-06-09', '2024-06-10',
        '2024-06-11', '2024-06-12', '2024-06-13', '2024-06-14', '2024-06-15',
        '2024-06-16', '2024-06-17', '2024-06-18', '2024-06-19', '2024-06-20',
        '2024-06-21', '2024-06-22', '2024-06-23', '2024-06-24', '2024-06-25',
        '2024-06-26', '2024-06-27', '2024-06-28', '2024-06-29', '2024-06-30'
    ],
    'Calories': [
        2100, 1950, 2200, 1850, 2000, 2250, 2050, 2150, 1900, 2000,
        2300, 2100, 2200, 1950, 2050, 2150, 1900, 2000, 2300, 2100,
        2200, 1850, 2000, 2250, 2050, 2150, 1900, 2000, 2300, 2100
    ]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

fig, ax = plt.subplots(figsize=(14, 7))

ax.fill_between(df['Date'], df['Calories'], color='#ff7f0e', alpha=0.6)

ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
fig.autofmt_xdate()

for i, txt in enumerate(df['Calories']):
    ax.annotate(txt, (df['Date'][i], df['Calories'][i]), textcoords="offset points", xytext=(0,5), ha='center')

plt.xlabel('Date')
plt.ylabel('Calories')
plt.title('Daily Calorie Intake in June 2024', pad=20)
plt.grid(True)

plt.show()