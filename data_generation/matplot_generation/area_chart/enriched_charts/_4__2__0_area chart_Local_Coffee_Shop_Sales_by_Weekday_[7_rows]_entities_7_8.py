
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Date': pd.date_range(start='2023-01-01', end='2023-01-31'),
    'Words_Written': [
        1500, 1600, 1580, 1650, 1700, 1750, 1800, 1850, 1900, 1950,
        2000, 2100, 2200, 2250, 2300, 2400, 2500, 2550, 2600, 2650,
        2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3150,
        3200
    ]
}
df = pd.DataFrame(data)

plt.figure(figsize=(16, 9))

sns.lineplot(data=df, x='Date', y='Words_Written', color="#3498db")
plt.fill_between(df['Date'], df['Words_Written'], color="#3498db", alpha=0.4)

max_words_written = df['Words_Written'].max()
max_date = df.loc[df['Words_Written'].idxmax(), 'Date']
plt.annotate(f'Peak: {max_words_written}', xy=(max_date, max_words_written),
             xytext=(max_date, max_words_written + 200), textcoords='data',
             arrowprops=dict(facecolor='#333333', shrink=0.05),
             horizontalalignment='center', verticalalignment='top')

plt.title('Daily Words Written in January 2023', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Words Written', fontsize=14)
sns.despine()
plt.show()