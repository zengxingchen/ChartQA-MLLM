
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Date': ['2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01', '2024-05-01', '2024-06-01', 
             '2024-07-01', '2024-08-01', '2024-09-01', '2024-10-01', '2024-11-01', '2024-12-01'],
    'Subscribers': [100, 150, 200, 300, 400, 600, 800, 900, 850, 750, 650, 550]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(16, 10))
sns.set(style="whitegrid")

sns.lineplot(data=df, x='Date', y='Subscribers', color="#1E90FF")
plt.fill_between(df['Date'], df['Subscribers'], alpha=0.3, color="#1E90FF")

max_subscribers = df['Subscribers'].max()
max_subscribers_date = df.loc[df['Subscribers'] == max_subscribers, 'Date'].iloc[0]
plt.text(x=max_subscribers_date, y=max_subscribers, s='Peak\n{} Subscribers'.format(max_subscribers), color="black",
         horizontalalignment='left', size='medium', style='italic')

plt.title("Monthly Newsletter Subscribers in 2024", fontsize=16, pad=20)
plt.xlabel("Date")
plt.ylabel("Subscribers")

plt.show()