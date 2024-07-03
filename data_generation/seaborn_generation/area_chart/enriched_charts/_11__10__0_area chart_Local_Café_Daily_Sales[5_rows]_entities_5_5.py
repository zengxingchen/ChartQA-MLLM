
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

data = {
    'Date': pd.date_range(start='2023-03-01', periods=31, freq='D'),
    'Stock Price': [120, 155, 135, 162, 178, 210, 185, 195, 205, 225, 215, 255, 235, 275, 265, 290, 310, 300, 320, 330, 345, 355, 375, 365, 385, 395, 405, 415, 425, 435, 445]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 8))
sns.set_theme(style="whitegrid")
ax = sns.lineplot(x='Date', y='Stock Price', data=df, color='#2ca02c')
ax.fill_between(df['Date'], df['Stock Price'], color="#98df8a")
ax.set(title='Daily Stock Prices in March 2023', xlabel='Date', ylabel='Stock Price')
date_form = DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(date_form)

for index, row in df.iterrows():
    ax.text(row['Date'], row['Stock Price'], f'{row["Stock Price"]}', 
            ha='center', va='bottom', fontsize=8, color='black')

plt.show()