import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Date': pd.date_range(start='2023-01-01', periods=31, freq='D'),
    'Steps': [5200, 5800, 6200, 5900, 6400, 6800, 7200, 7600, 7900, 8200, 8500, 8800, 9100, 9400, 9700, 10000, 10300, 10600, 10900, 11200, 11500, 11800, 12100, 12400, 12700, 13000, 13300, 13600, 13900, 14200, 14500]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 7))

sns.lineplot(data=df, x='Date', y='Steps', color='#2ca02c', lw=2)
plt.fill_between(data['Date'], 0, data['Steps'], color='#2ca02c', alpha=0.3)

plt.title('Daily Steps Count for January 2023', fontsize=16, loc='center')
plt.xlabel('Date')
plt.ylabel('Steps')

plt.text(x=df['Date'][30], y=df['Steps'][30], s="Peak", color='#d62728', va='bottom', ha='right')

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()