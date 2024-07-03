
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import DateFormatter

data = [
    {'Date': '2023-06-01', 'Energy Generated (kWh)': 150, 'Energy Consumed (kWh)': 130},
    {'Date': '2023-06-02', 'Energy Generated (kWh)': 145, 'Energy Consumed (kWh)': 125},
    {'Date': '2023-06-03', 'Energy Generated (kWh)': 155, 'Energy Consumed (kWh)': 135},
    {'Date': '2023-06-04', 'Energy Generated (kWh)': 160, 'Energy Consumed (kWh)': 140},
    {'Date': '2023-06-05', 'Energy Generated (kWh)': 158, 'Energy Consumed (kWh)': 138},
    {'Date': '2023-06-06', 'Energy Generated (kWh)': 162, 'Energy Consumed (kWh)': 142},
    {'Date': '2023-06-07', 'Energy Generated (kWh)': 165, 'Energy Consumed (kWh)': 145},
    {'Date': '2023-06-08', 'Energy Generated (kWh)': 170, 'Energy Consumed (kWh)': 150},
    {'Date': '2023-06-09', 'Energy Generated (kWh)': 168, 'Energy Consumed (kWh)': 148},
    {'Date': '2023-06-10', 'Energy Generated (kWh)': 175, 'Energy Consumed (kWh)': 155},
    {'Date': '2023-06-11', 'Energy Generated (kWh)': 172, 'Energy Consumed (kWh)': 152},
    {'Date': '2023-06-12', 'Energy Generated (kWh)': 180, 'Energy Consumed (kWh)': 160},
    {'Date': '2023-06-13', 'Energy Generated (kWh)': 178, 'Energy Consumed (kWh)': 158},
    {'Date': '2023-06-14', 'Energy Generated (kWh)': 185, 'Energy Consumed (kWh)': 165},
    {'Date': '2023-06-15', 'Energy Generated (kWh)': 183, 'Energy Consumed (kWh)': 163},
]

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

fig, ax = plt.subplots(figsize=(16, 10))

ax.plot(df['Date'], df['Energy Generated (kWh)'], color='#2ca02c', marker='o', linestyle='-', linewidth=2, label='Energy Generated (kWh)')
ax.plot(df['Date'], df['Energy Consumed (kWh)'], color='#d62728', marker='s', linestyle='--', linewidth=2, label='Energy Consumed (kWh)')

ax.set_title('Daily Energy Generation and Consumption', pad=20)
ax.set_xlabel('Date')
ax.set_ylabel('kWh')
ax.invert_yaxis()

date_form = DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(date_form)

plt.xticks(rotation=45)

ax.legend(loc='lower right')

for i, txt in enumerate(df['Energy Generated (kWh)']):
    ax.annotate(txt, (df['Date'][i], df['Energy Generated (kWh)'][i]), textcoords="offset points", xytext=(0,10), ha='center')

for i, txt in enumerate(df['Energy Consumed (kWh)']):
    ax.annotate(txt, (df['Date'][i], df['Energy Consumed (kWh)'][i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()

plt.show()