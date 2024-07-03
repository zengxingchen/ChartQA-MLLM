
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import DateFormatter

data = [
    {'Date': '2023-06-01', 'Hours Studied': 2, 'Pages Read': 30},
    {'Date': '2023-06-02', 'Hours Studied': 3, 'Pages Read': 40},
    {'Date': '2023-06-03', 'Hours Studied': 1.5, 'Pages Read': 25},
    {'Date': '2023-06-04', 'Hours Studied': 4, 'Pages Read': 60},
    {'Date': '2023-06-05', 'Hours Studied': 2.5, 'Pages Read': 35},
    {'Date': '2023-06-06', 'Hours Studied': 3.5, 'Pages Read': 50},
    {'Date': '2023-06-07', 'Hours Studied': 2, 'Pages Read': 30},
    {'Date': '2023-06-08', 'Hours Studied': 4.5, 'Pages Read': 70},
    {'Date': '2023-06-09', 'Hours Studied': 2, 'Pages Read': 28},
    {'Date': '2023-06-10', 'Hours Studied': 3, 'Pages Read': 45},
    {'Date': '2023-06-11', 'Hours Studied': 2.5, 'Pages Read': 32},
    {'Date': '2023-06-12', 'Hours Studied': 1.5, 'Pages Read': 20},
    {'Date': '2023-06-13', 'Hours Studied': 3, 'Pages Read': 48},
    {'Date': '2023-06-14', 'Hours Studied': 2, 'Pages Read': 34},
    {'Date': '2023-06-15', 'Hours Studied': 4, 'Pages Read': 60},
]

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(df['Date'], df['Hours Studied'], color='#1f77b4', marker='o', linestyle='-', linewidth=2, label='Hours Studied')
ax.plot(df['Date'], df['Pages Read'], color='#ff7f0e', marker='s', linestyle='--', linewidth=2, label='Pages Read')

ax.set_title('Daily Study Hours and Pages Read', pad=20)
ax.set_xlabel('Date')
ax.set_ylabel('Count')

date_form = DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(date_form)

plt.xticks(rotation=45)

ax.legend(loc='upper right')

for i, txt in enumerate(df['Hours Studied']):
    ax.annotate(txt, (df['Date'][i], df['Hours Studied'][i]), textcoords="offset points", xytext=(0,10), ha='center')

for i, txt in enumerate(df['Pages Read']):
    ax.annotate(txt, (df['Date'][i], df['Pages Read'][i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()

plt.show()