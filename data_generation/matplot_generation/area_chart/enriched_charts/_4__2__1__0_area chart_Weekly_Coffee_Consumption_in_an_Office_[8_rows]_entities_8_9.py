
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
    'Stock_Price': [
        100, 105, 102, 108, 107, 111, 113, 115, 117, 120,
        122, 125, 128, 127, 130, 132, 135, 138, 137, 140,
        142, 144, 147, 150, 152, 155, 157, 160, 162, 165
    ]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

fig, ax = plt.subplots(figsize=(16, 9))

ax.fill_between(df['Date'], df['Stock_Price'], color='#3399FF', alpha=0.6)

ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
fig.autofmt_xdate()

for i, txt in enumerate(df['Stock_Price']):
    ax.annotate(txt, (df['Date'][i], df['Stock_Price'][i]), textcoords="offset points", xytext=(0,5), ha='center')

plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('Daily Stock Prices in June 2024', pad=20)
plt.grid(True)

plt.show()