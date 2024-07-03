
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

data = {
    'Date': pd.date_range(start='2023-03-01', periods=31, freq='D'),
    'Products Sold': [50, 60, 55, 65, 70, 75, 80, 85, 90, 95, 100, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 8))
sns.set_theme(style="whitegrid")
ax = sns.lineplot(x='Date', y='Products Sold', data=df, color='#FF6347')
ax.fill_between(df['Date'], df['Products Sold'], color="#FFD700")
ax.set(title='Daily Product Sales in March 2023', xlabel='Date', ylabel='Number of Products Sold')
date_form = DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(date_form)

for index, row in df.iterrows():
    ax.text(row['Date'], row['Products Sold'], f'{row["Products Sold"]}', 
            ha='center', va='bottom', fontsize=8, color='black')

plt.show()