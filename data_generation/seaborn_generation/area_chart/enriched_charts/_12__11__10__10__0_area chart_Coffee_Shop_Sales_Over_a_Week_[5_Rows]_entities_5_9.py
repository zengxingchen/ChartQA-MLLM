
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Date': ['2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01', '2021-05-01',
             '2021-06-01', '2021-07-01', '2021-08-01', '2021-09-01', '2021-10-01',
             '2021-11-01', '2021-12-01', '2022-01-01', '2022-02-01', '2022-03-01',
             '2022-04-01', '2022-05-01', '2022-06-01', '2022-07-01', '2022-08-01',
             '2022-09-01', '2022-10-01', '2022-11-01', '2022-12-01'],
    'Steps': [5000, 7000, 6000, 8000, 7500, 9000, 10000, 9500, 10500, 11000, 11500, 12000,
              12500, 13000, 13500, 14000, 14500, 15000, 15500, 16000, 16500, 17000, 17500, 18000]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(20, 12))
ax = sns.lineplot(x='Date', y='Steps', data=df, color='#FF5733', label='Daily Steps')
ax.fill_between(df['Date'], df['Steps'], color='#FF5733', alpha=0.3)

for index, value in df.iterrows():
    ax.text(value['Date'], value['Steps'], str(value['Steps']), verticalalignment='bottom',
            horizontalalignment='left', color='#333333', fontsize=8)

plt.title('Daily Steps Over Two Years', fontsize=20)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Steps', fontsize=14)
sns.despine(trim=True)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()