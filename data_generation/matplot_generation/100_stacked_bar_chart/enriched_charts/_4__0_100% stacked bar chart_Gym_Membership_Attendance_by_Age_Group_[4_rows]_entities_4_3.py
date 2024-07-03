
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = {
    'Country': ['France', 'Italy', 'Spain', 'Australia', 'Brazil', 'India', 'China', 'South Korea', 'South Africa', 'Russia'],
    'Reading': [25, 30, 20, 15, 10, 35, 20, 25, 15, 20],
    'Movies': [35, 20, 30, 25, 30, 25, 30, 20, 25, 25],
    'Exercise': [15, 25, 20, 30, 25, 15, 25, 25, 20, 15],
    'Music': [10, 15, 20, 20, 20, 15, 15, 15, 25, 20],
    'Travel': [15, 10, 10, 10, 15, 10, 10, 15, 15, 20]
}

df = pd.DataFrame(data)
df.set_index('Country', inplace=True)
df_percentage = df.div(df.sum(axis=1), axis=0) * 100

colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#6A5ACD']
barWidth = 0.5

fig, ax = plt.subplots(figsize=(10, 12))

bars = np.add(df_percentage['Reading'], df_percentage['Movies']).tolist()

ax.bar(df.index, df_percentage['Reading'], color=colors[0], edgecolor='grey', width=barWidth, label='Reading')
ax.bar(df.index, df_percentage['Movies'], bottom=df_percentage['Reading'], color=colors[1], edgecolor='grey', width=barWidth, label='Movies')
ax.bar(df.index, df_percentage['Exercise'], bottom=bars, color=colors[2], edgecolor='grey', width=barWidth, label='Exercise')
ax.bar(df.index, df_percentage['Music'], bottom=np.add(bars, df_percentage['Exercise']).tolist(), color=colors[3], edgecolor='grey', width=barWidth, label='Music')
ax.bar(df.index, df_percentage['Travel'], bottom=np.add(bars, np.add(df_percentage['Exercise'], df_percentage['Music'])).tolist(), color=colors[4], edgecolor='grey', width=barWidth, label='Travel')

ax.set_ylabel('Percentage')
ax.set_title('Leisure Activity Preferences by Country')
ax.set_ylim(0, 100)
ax.set_yticks(np.arange(0, 101, 10))

ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), shadow=True, ncol=1)

for index, value in enumerate(df_percentage.index):
    for col in df_percentage.columns:
        bar_value = df_percentage.at[value, col]
        sum_previous = df_percentage.loc[value, :col].sum() - bar_value
        ax.text(index, sum_previous + bar_value / 2, f'{bar_value:.1f}%', va='center', ha='center')

plt.show()