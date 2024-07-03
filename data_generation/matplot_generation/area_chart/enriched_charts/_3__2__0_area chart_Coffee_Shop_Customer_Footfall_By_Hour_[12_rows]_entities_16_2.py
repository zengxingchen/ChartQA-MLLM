
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Date': pd.date_range(start='2023-01-01', periods=31, freq='D'),
    'Steps': [
        5000, 5200, 5300, 4900, 5100, 5500, 5800, 6000, 6200, 5900,
        6100, 6300, 6500, 6800, 7000, 7200, 7500, 7700, 7800, 7400,
        7100, 7300, 7600, 7900, 8000, 8300, 8500, 8700, 8900, 9100, 9300
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 10))
area_chart = sns.lineplot(data=df, x='Date', y='Steps', color="#1f77b4")
plt.fill_between(df['Date'], df['Steps'], color="#87cefa")

for index in range(0, df.shape[0], 5):
    date = df.iloc[index]['Date']
    steps = df.iloc[index]['Steps']
    plt.text(date, steps + 300, str(steps), ha='center')

plt.title('Daily Steps Count in January 2023', pad=30)
plt.xlabel('Date')
plt.ylabel('Steps Count')
sns.despine()

plt.show()