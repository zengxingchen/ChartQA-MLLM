
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December'],
    'Temperature': [5.0, 6.5, 10.0, 14.0, 18.5, 22.0, 25.0, 24.0, 20.0, 15.0, 10.0, 6.0],
    'Precipitation': [78, 65, 54, 49, 43, 38, 35, 40, 55, 65, 75, 82],
    'WindSpeed': [15, 18, 22, 20, 25, 30, 28, 26, 22, 20, 18, 16]
}

df = pd.DataFrame(data)
df = df.set_index('Month')

df_cum = df.cumsum(axis=1)

colors = ['#FFA07A', '#20B2AA', '#778899']

plt.figure(figsize=(16, 10))

plt.fill_between(df.index, 0, df_cum['Temperature'], color=colors[0], alpha=0.7, label='Temperature')
plt.fill_between(df.index, df_cum['Temperature'], df_cum['Temperature'] + df_cum['Precipitation'], color=colors[1], alpha=0.7, label='Precipitation')
plt.fill_between(df.index, df_cum['Temperature'] + df_cum['Precipitation'], df_cum['Temperature'] + df_cum['Precipitation'] + df_cum['WindSpeed'], color=colors[2], alpha=0.7, label='WindSpeed')

for category in ['Temperature', 'Precipitation', 'WindSpeed']:
    plt.text(df.index[-1], df_cum[category][-1] - (df_cum[category][-1] - df_cum[category].shift(1)[-1]) / 2, category, verticalalignment='center')

plt.title('Monthly Weather Patterns')
plt.xlabel('Month')
plt.ylabel('Values')
plt.xticks(rotation=45)
plt.legend(loc='upper left')
plt.tight_layout()

plt.show()