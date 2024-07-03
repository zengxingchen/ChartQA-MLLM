
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import DateFormatter

data = [
    {'Date': '2023-06-01', 'Daily Steps': 10000, 'Calories Consumed': 2200},
    {'Date': '2023-06-02', 'Daily Steps': 8500, 'Calories Consumed': 2000},
    {'Date': '2023-06-03', 'Daily Steps': 9200, 'Calories Consumed': 2100},
    {'Date': '2023-06-04', 'Daily Steps': 11000, 'Calories Consumed': 2300},
    {'Date': '2023-06-05', 'Daily Steps': 12000, 'Calories Consumed': 2400},
    {'Date': '2023-06-06', 'Daily Steps': 9500, 'Calories Consumed': 2150},
    {'Date': '2023-06-07', 'Daily Steps': 7000, 'Calories Consumed': 1900},
    {'Date': '2023-06-08', 'Daily Steps': 8000, 'Calories Consumed': 1950},
    {'Date': '2023-06-09', 'Daily Steps': 13000, 'Calories Consumed': 2450},
    {'Date': '2023-06-10', 'Daily Steps': 15000, 'Calories Consumed': 2600},
    {'Date': '2023-06-11', 'Daily Steps': 12500, 'Calories Consumed': 2350},
    {'Date': '2023-06-12', 'Daily Steps': 13500, 'Calories Consumed': 2500},
    {'Date': '2023-06-13', 'Daily Steps': 14000, 'Calories Consumed': 2550},
    {'Date': '2023-06-14', 'Daily Steps': 11000, 'Calories Consumed': 2250},
]

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(df['Date'], df['Daily Steps'], color='#4CAF50', marker='o', linestyle='-', linewidth=2, label='Daily Steps')
ax.plot(df['Date'], df['Calories Consumed'], color='#E91E63', marker='s', linestyle='--', linewidth=2, label='Calories Consumed')

ax.set_title('Daily Steps and Calories Consumed Over Time', pad=20)
ax.set_xlabel('Date')
ax.set_ylabel('Count')

date_form = DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(date_form)

plt.xticks(rotation=45)

ax.legend(loc='upper left')

for i, txt in enumerate(df['Daily Steps']):
    ax.annotate(txt, (df['Date'][i], df['Daily Steps'][i]), textcoords="offset points", xytext=(0,10), ha='center')

for i, txt in enumerate(df['Calories Consumed']):
    ax.annotate(txt, (df['Date'][i], df['Calories Consumed'][i]), textcoords="offset points", xytext=(0,10), ha='center')

ax.invert_yaxis()
plt.tight_layout()
plt.show()