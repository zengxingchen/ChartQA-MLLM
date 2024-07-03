
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Date': ['2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01', '2024-05-01', '2024-06-01', 
             '2024-07-01', '2024-08-01', '2024-09-01', '2024-10-01', '2024-11-01', '2024-12-01',
             '2024-01-15', '2024-02-15', '2024-03-15', '2024-04-15', '2024-05-15', '2024-06-15',
             '2024-07-15', '2024-08-15', '2024-09-15', '2024-10-15', '2024-11-15', '2024-12-15'],
    'Revenue': [5000, 5200, 5300, 5500, 5800, 6000, 6200, 6300, 6100, 5900, 5700, 5600,
                5100, 5250, 5350, 5600, 5850, 6050, 6250, 6350, 6150, 5950, 5750, 5650]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(16, 9))
sns.set(style="whitegrid")

sns.lineplot(data=df, x='Date', y='Revenue', color="#4682B4")
plt.fill_between(df['Date'], df['Revenue'], alpha=0.3, color="#4682B4")

max_revenue = df['Revenue'].max()
max_revenue_date = df.loc[df['Revenue'] == max_revenue, 'Date'].iloc[0]
plt.text(x=max_revenue_date, y=max_revenue, s='Peak\n${:,} Revenue'.format(max_revenue), color="black",
         horizontalalignment='left', size='medium', style='italic')

plt.title("Monthly Revenue in 2024", fontsize=18, pad=20)
plt.xlabel("Date")
plt.ylabel("Revenue (in USD)")

plt.show()