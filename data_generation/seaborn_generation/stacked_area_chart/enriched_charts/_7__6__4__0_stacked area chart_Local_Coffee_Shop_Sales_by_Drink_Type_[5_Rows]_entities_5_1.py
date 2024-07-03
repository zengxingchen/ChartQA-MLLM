
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December'],
    'Running Distance': [50, 55, 60, 70, 75, 80, 85, 90, 95, 100, 105, 110],
    'Cycling Distance': [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310],
    'Swimming Distance': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
}

df = pd.DataFrame(data)
df = df.set_index('Month')

df_cum = df.cumsum(axis=1)

colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

plt.figure(figsize=(16, 10))

plt.fill_between(df.index, 0, df_cum['Running Distance'], color=colors[0], alpha=0.7, label='Running Distance')
plt.fill_between(df.index, df_cum['Running Distance'], df_cum['Running Distance'] + df_cum['Cycling Distance'], color=colors[1], alpha=0.7, label='Cycling Distance')
plt.fill_between(df.index, df_cum['Running Distance'] + df_cum['Cycling Distance'], df_cum['Running Distance'] + df_cum['Cycling Distance'] + df_cum['Swimming Distance'], color=colors[2], alpha=0.7, label='Swimming Distance')

for category in ['Running Distance', 'Cycling Distance', 'Swimming Distance']:
    plt.text(df.index[-1], df_cum[category][-1] - (df_cum[category][-1] - df_cum[category].shift(1)[-1]) / 2, category, verticalalignment='center')

plt.title('Monthly Athletic Performance Metrics', pad=20)
plt.xlabel('Month')
plt.ylabel('Distance (km)')
plt.xticks(rotation=45)
plt.legend(loc='upper right')
plt.tight_layout()

plt.show()