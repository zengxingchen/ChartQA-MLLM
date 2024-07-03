
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December'],
    'RenewableEnergy': [1000, 1100, 1050, 1150, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600],
    'GreenTransport': [800, 900, 870, 950, 1020, 1050, 1100, 1150, 1200, 1250, 1300, 1350],
    'Recycling': [600, 650, 620, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100]
}

df = pd.DataFrame(data)
df = df.set_index('Month')

df_cum = df.cumsum(axis=1)

colors = ['#003f5c', '#7a5195', '#ef5675']

plt.figure(figsize=(18, 12))

plt.fill_between(df.index, 0, df_cum['RenewableEnergy'], color=colors[0], alpha=0.7, label='Renewable Energy')
plt.fill_between(df.index, df_cum['RenewableEnergy'], df_cum['RenewableEnergy'] + df_cum['GreenTransport'], color=colors[1], alpha=0.7, label='Green Transport')
plt.fill_between(df.index, df_cum['RenewableEnergy'] + df_cum['GreenTransport'], df_cum['RenewableEnergy'] + df_cum['GreenTransport'] + df_cum['Recycling'], color=colors[2], alpha=0.7, label='Recycling')

for category in ['RenewableEnergy', 'GreenTransport', 'Recycling']:
    plt.text(df.index[-1], df_cum[category][-1] - (df_cum[category][-1] - df_cum[category].shift(1)[-1]) / 2, category.replace("RenewableEnergy", "Renewable Energy").replace("GreenTransport", "Green Transport"), verticalalignment='center')

plt.title('Monthly Environmental Efforts', pad=30)
plt.xlabel('Month')
plt.ylabel('Hours Dedicated')
plt.xticks(rotation=45)
plt.legend(loc='upper right')
plt.tight_layout()

plt.show()