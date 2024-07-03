
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

data = {
    'Date': pd.date_range(start='2023-03-01', periods=31, freq='D'),
    'Visitors': [120, 150, 130, 160, 170, 200, 180, 190, 210, 230, 220, 250, 240, 270, 260, 280, 300, 290, 310, 320, 330, 340, 360, 370, 380, 390, 400, 410, 420, 430, 440]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 7))
sns.set_theme(style="whitegrid")
ax = sns.lineplot(x='Date', y='Visitors', data=df, color='#1f77b4')
ax.fill_between(df['Date'], df['Visitors'], color="#87ceeb")
ax.set(title='Daily Visitors to the Museum in March 2023', xlabel='Date', ylabel='Number of Visitors')
date_form = DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(date_form)

for index, row in df.iterrows():
    ax.text(row['Date'], row['Visitors'], f'{row["Visitors"]}', 
            ha='center', va='bottom', fontsize=8, color='black')

plt.show()