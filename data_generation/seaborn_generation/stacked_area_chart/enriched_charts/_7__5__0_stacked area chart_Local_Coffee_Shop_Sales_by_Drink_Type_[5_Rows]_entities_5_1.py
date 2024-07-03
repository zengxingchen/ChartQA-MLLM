
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December'],
    'Revenue': [3000, 3200, 3400, 3600, 3800, 4000, 4200, 4400, 4600, 4800, 5000, 5200],
    'Expenses': [2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100],
    'Profit': [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100]
}

df = pd.DataFrame(data)
df = df.set_index('Month')

df_cum = df.cumsum(axis=1)

colors = ['#ff9999', '#66b3ff', '#99ff99']

plt.figure(figsize=(18, 12))

plt.fill_between(df.index, 0, df_cum['Revenue'], color=colors[0], alpha=0.6, label='Revenue')
plt.fill_between(df.index, df_cum['Revenue'], df_cum['Revenue'] + df_cum['Expenses'], color=colors[1], alpha=0.6, label='Expenses')
plt.fill_between(df.index, df_cum['Revenue'] + df_cum['Expenses'], df_cum['Revenue'] + df_cum['Expenses'] + df_cum['Profit'], color=colors[2], alpha=0.6, label='Profit')

for category in ['Revenue', 'Expenses', 'Profit']:
    plt.text(df.index[-1], df_cum[category][-1] - (df_cum[category][-1] - df_cum[category].shift(1)[-1]) / 2, category, verticalalignment='center')

plt.title('Monthly Financial Overview', pad=20)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.xticks(rotation=45)
plt.legend(loc='upper left')
plt.tight_layout()

plt.show()