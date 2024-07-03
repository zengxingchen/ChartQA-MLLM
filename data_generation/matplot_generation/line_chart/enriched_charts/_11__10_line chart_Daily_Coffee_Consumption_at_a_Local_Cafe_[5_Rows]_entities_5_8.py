
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import DateFormatter

data = [
    {'Date': '2023-06-01', 'Daily Active Minutes': 65, 'Calories Burned': 345},
    {'Date': '2023-06-02', 'Daily Active Minutes': 70, 'Calories Burned': 330},
    {'Date': '2023-06-03', 'Daily Active Minutes': 55, 'Calories Burned': 360},
    {'Date': '2023-06-04', 'Daily Active Minutes': 40, 'Calories Burned': 310},
    {'Date': '2023-06-05', 'Daily Active Minutes': 80, 'Calories Burned': 375},
    {'Date': '2023-06-06', 'Daily Active Minutes': 90, 'Calories Burned': 390},
    {'Date': '2023-06-07', 'Daily Active Minutes': 60, 'Calories Burned': 335},
    {'Date': '2023-06-08', 'Daily Active Minutes': 85, 'Calories Burned': 380},
    {'Date': '2023-06-09', 'Daily Active Minutes': 45, 'Calories Burned': 320},
    {'Date': '2023-06-10', 'Daily Active Minutes': 50, 'Calories Burned': 340},
    {'Date': '2023-06-11', 'Daily Active Minutes': 75, 'Calories Burned': 370},
    {'Date': '2023-06-12', 'Daily Active Minutes': 95, 'Calories Burned': 400},
    {'Date': '2023-06-13', 'Daily Active Minutes': 85, 'Calories Burned': 390},
    {'Date': '2023-06-14', 'Daily Active Minutes': 65, 'Calories Burned': 350},
]

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(df['Date'], df['Daily Active Minutes'], color='#1f77b4', marker='o', linestyle='-', linewidth=2, label='Daily Active Minutes')
ax.plot(df['Date'], df['Calories Burned'], color='#ff7f0e', marker='s', linestyle='--', linewidth=2, label='Calories Burned')

ax.set_title('Daily Active Minutes and Calories Burned Over Time', pad=20)
ax.set_xlabel('Date')
ax.set_ylabel('Count')

date_form = DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(date_form)

plt.xticks(rotation=45)

ax.legend(loc='upper right')

for i, txt in enumerate(df['Daily Active Minutes']):
    ax.annotate(txt, (df['Date'][i], df['Daily Active Minutes'][i]), textcoords="offset points", xytext=(0,10), ha='center')

for i, txt in enumerate(df['Calories Burned']):
    ax.annotate(txt, (df['Date'][i], df['Calories Burned'][i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.show()