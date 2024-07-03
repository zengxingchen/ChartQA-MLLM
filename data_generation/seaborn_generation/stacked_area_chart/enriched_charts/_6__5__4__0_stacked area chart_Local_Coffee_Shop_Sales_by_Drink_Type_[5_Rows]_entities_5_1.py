
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December'],
    'Steps': [10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000],
    'CaloriesBurned': [2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100],
    'HeartRate': [70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92]
}

df = pd.DataFrame(data)
df = df.set_index('Month')

df_cum = df.cumsum(axis=1)

colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

plt.figure(figsize=(16, 10))

plt.fill_between(df.index, 0, df_cum['Steps'], color=colors[0], alpha=0.7, label='Steps')
plt.fill_between(df.index, df_cum['Steps'], df_cum['Steps'] + df_cum['CaloriesBurned'], color=colors[1], alpha=0.7, label='Calories Burned')
plt.fill_between(df.index, df_cum['Steps'] + df_cum['CaloriesBurned'], df_cum['Steps'] + df_cum['CaloriesBurned'] + df_cum['HeartRate'], color=colors[2], alpha=0.7, label='Heart Rate')

for category in ['Steps', 'CaloriesBurned', 'HeartRate']:
    plt.text(df.index[-1], df_cum[category][-1] - (df_cum[category][-1] - df_cum[category].shift(1)[-1]) / 2, category.replace('Burned', ' Burned').replace('Rate', ' Rate'), verticalalignment='center')

plt.title('Monthly Fitness Tracker Data', fontsize=18, pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Values', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.legend(loc='upper left', fontsize=12)
plt.tight_layout()

plt.show()