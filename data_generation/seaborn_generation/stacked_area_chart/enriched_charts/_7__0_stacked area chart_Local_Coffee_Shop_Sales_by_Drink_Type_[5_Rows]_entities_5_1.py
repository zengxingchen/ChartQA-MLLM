
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December'],
    'Medicine': [1200, 1300, 1250, 1400, 1350, 1450, 1500, 1550, 1600, 1650, 1700, 1750],
    'Therapy': [800, 850, 820, 900, 870, 920, 950, 980, 1000, 1050, 1080, 1100],
    'Supplements': [500, 550, 540, 600, 580, 620, 650, 670, 700, 750, 780, 800]
}

df = pd.DataFrame(data)
df = df.set_index('Month')

df_cum = df.cumsum(axis=1)

colors = ['#FF6347', '#4682B4', '#32CD32']

plt.figure(figsize=(16, 10))

plt.fill_between(df.index, 0, df_cum['Medicine'], color=colors[0], alpha=0.6, label='Medicine')
plt.fill_between(df.index, df_cum['Medicine'], df_cum['Medicine'] + df_cum['Therapy'], color=colors[1], alpha=0.6, label='Therapy')
plt.fill_between(df.index, df_cum['Medicine'] + df_cum['Therapy'], df_cum['Medicine'] + df_cum['Therapy'] + df_cum['Supplements'], color=colors[2], alpha=0.6, label='Supplements')

for category in ['Medicine', 'Therapy', 'Supplements']:
    plt.text(df.index[-1], df_cum[category][-1] - (df_cum[category][-1] - df_cum[category].shift(1)[-1]) / 2, category, verticalalignment='center')

plt.title('Monthly Health Expenditure by Category', loc='center', pad=20)
plt.xlabel('Month')
plt.ylabel('Expenditure (In Thousands)')
plt.xticks(rotation=45)
plt.legend(loc='upper right')
plt.tight_layout()

plt.show()