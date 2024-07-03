
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Date': pd.date_range(start='2023-01-01', end='2023-01-31'),
    'Visitor_Count': [
        120, 130, 125, 140, 145, 150, 160, 155, 170, 165,
        175, 180, 185, 190, 200, 210, 215, 220, 225, 230,
        235, 240, 245, 250, 255, 260, 265, 270, 275, 280,
        285
    ]
}
df = pd.DataFrame(data)

plt.figure(figsize=(14, 8))

sns.lineplot(data=df, x='Date', y='Visitor_Count', color="#2ecc71")
plt.fill_between(df['Date'], df['Visitor_Count'], color="#2ecc71", alpha=0.4)

max_visitor_count = df['Visitor_Count'].max()
max_date = df.loc[df['Visitor_Count'].idxmax(), 'Date']
plt.annotate(f'Peak: {max_visitor_count}', xy=(max_date, max_visitor_count),
             xytext=(max_date, max_visitor_count + 10), textcoords='data',
             arrowprops=dict(facecolor='#333333', shrink=0.05),
             horizontalalignment='center', verticalalignment='top')

plt.title('Daily Visitors in January 2023')
plt.xlabel('Date')
plt.ylabel('Visitor Count')
sns.despine()
plt.show()