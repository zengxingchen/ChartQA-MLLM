
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

data = {
    'Date': pd.date_range(start='2023-03-01', periods=31, freq='D'),
    'Pollution Level': [42, 35, 48, 55, 50, 62, 70, 65, 58, 72, 68, 75, 80, 85, 90, 95, 85, 78, 82, 88, 92, 97, 94, 99, 101, 104, 110, 115, 112, 118, 120]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 10))
sns.set_theme(style="whitegrid")
ax = sns.lineplot(x='Date', y='Pollution Level', data=df, color='#ff7f0e')
ax.fill_between(df['Date'], df['Pollution Level'], color="#ffbb78")
ax.set(title='Daily Air Pollution Levels in March 2023', xlabel='Date', ylabel='Pollution Level (AQI)')
date_form = DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(date_form)

for index, row in df.iterrows():
    ax.text(row['Date'], row['Pollution Level'], f'{row["Pollution Level"]}', 
            ha='center', va='bottom', fontsize=8, color='black')

plt.show()