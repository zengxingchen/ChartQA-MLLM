
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Date': ['2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01', '2021-05-01',
             '2021-06-01', '2021-07-01', '2021-08-01', '2021-09-01', '2021-10-01',
             '2021-11-01', '2021-12-01', '2022-01-01', '2022-02-01', '2022-03-01',
             '2022-04-01', '2022-05-01', '2022-06-01', '2022-07-01', '2022-08-01',
             '2022-09-01', '2022-10-01', '2022-11-01', '2022-12-01'],
    'Revenue': [2000, 2500, 1800, 2200, 2700, 3000, 3200, 3500, 3700, 3900, 4100, 4300,
                4500, 4700, 4900, 5100, 5300, 5500, 5700, 5900, 6100, 6300, 6500, 6700]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(18, 10))
ax = sns.lineplot(x='Date', y='Revenue', data=df, color='#1F77B4', label='Monthly Revenue ($)')
ax.fill_between(df['Date'], df['Revenue'], color='#1F77B4', alpha=0.3)

for index, value in df.iterrows():
    ax.text(value['Date'], value['Revenue'], str(value['Revenue']), verticalalignment='bottom',
            horizontalalignment='left', color='#333333', fontsize=8)

plt.title('Monthly Revenue Over Two Years', fontsize=20)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Revenue ($)', fontsize=14)
sns.despine(trim=True)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()