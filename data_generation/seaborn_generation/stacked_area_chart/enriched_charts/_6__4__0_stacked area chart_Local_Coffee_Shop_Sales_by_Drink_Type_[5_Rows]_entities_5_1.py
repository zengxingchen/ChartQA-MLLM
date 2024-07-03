
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December'],
    'Temperature': [30, 32, 50, 65, 70, 75, 80, 78, 70, 60, 50, 35],
    'Precipitation': [78, 65, 54, 49, 43, 38, 35, 40, 55, 65, 75, 82],
    'Humidity': [85, 80, 70, 65, 60, 55, 50, 55, 60, 70, 75, 80]
}

df = pd.DataFrame(data)
df = df.set_index('Month')

df_cum = df.cumsum(axis=1)

colors = ['#FF5733', '#33FF57', '#3357FF']

plt.figure(figsize=(14, 8))

plt.fill_between(df.index, 0, df_cum['Temperature'], color=colors[0], alpha=0.7, label='Temperature')
plt.fill_between(df.index, df_cum['Temperature'], df_cum['Temperature'] + df_cum['Precipitation'], color=colors[1], alpha=0.7, label='Precipitation')
plt.fill_between(df.index, df_cum['Temperature'] + df_cum['Precipitation'], df_cum['Temperature'] + df_cum['Precipitation'] + df_cum['Humidity'], color=colors[2], alpha=0.7, label='Humidity')

for category in ['Temperature', 'Precipitation', 'Humidity']:
    plt.text(df.index[-1], df_cum[category][-1] - (df_cum[category][-1] - df_cum[category].shift(1)[-1]) / 2, category, verticalalignment='center')

plt.title('Monthly Weather Data Analysis', pad=20)
plt.xlabel('Month')
plt.ylabel('Values')
plt.xticks(rotation=45)
plt.legend(loc='upper left')
plt.tight_layout()

plt.show()