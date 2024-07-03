
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Date': pd.date_range(start='2023-01-01', periods=31, freq='D'),
    'Steps': [5000, 5500, 5800, 6100, 6300, 6700, 7200, 7500, 8000, 8300, 7900, 8500, 9000, 9400, 9700,
              10000, 10500, 10800, 11200, 11500, 11800, 12000, 12300, 12500, 12800, 13000, 13500, 13800, 14000, 14200, 14500]
}

df = pd.DataFrame(data)

plt.figure(figsize=(16, 8))
sns.lineplot(data=df, x='Date', y='Steps', color='#2e8b57', lw=2)
plt.fill_between(df['Date'], 0, df['Steps'], color='#98fb98', alpha=0.3)
plt.title('Daily Step Count for January 2023', fontsize=18, pad=20)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Steps', fontsize=14)
plt.text(x=df['Date'][30], y=df['Steps'][30], s="Peak", color='#d2691e', va='bottom', ha='right', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()