
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December'],
    'Exercise': [1200, 1300, 1100, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200],
    'HealthyEating': [1500, 1600, 1400, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500],
    'StressManagement': [800, 850, 750, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300]
}

df = pd.DataFrame(data)
df = df.set_index('Month')

df_cum = df.cumsum(axis=1)

colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

plt.figure(figsize=(16, 10))

plt.fill_between(df.index, 0, df_cum['Exercise'], color=colors[0], alpha=0.6, label='Exercise')
plt.fill_between(df.index, df_cum['Exercise'], df_cum['Exercise'] + df_cum['HealthyEating'], color=colors[1], alpha=0.6, label='Healthy Eating')
plt.fill_between(df.index, df_cum['Exercise'] + df_cum['HealthyEating'], df_cum['Exercise'] + df_cum['HealthyEating'] + df_cum['StressManagement'], color=colors[2], alpha=0.6, label='Stress Management')

for category in ['Exercise', 'HealthyEating', 'StressManagement']:
    plt.text(df.index[-1], df_cum[category][-1] - (df_cum[category][-1] - df_cum[category].shift(1)[-1]) / 2, category, verticalalignment='center')

plt.title('Monthly Wellness Activities', pad=20)
plt.xlabel('Month')
plt.ylabel('Activities (Hours)')
plt.xticks(rotation=45)
plt.legend(loc='upper left')
plt.tight_layout()

plt.show()