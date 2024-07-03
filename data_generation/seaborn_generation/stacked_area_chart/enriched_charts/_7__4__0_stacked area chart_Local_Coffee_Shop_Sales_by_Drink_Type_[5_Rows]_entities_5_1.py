
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December'],
    'Painting': [5, 10, 15, 20, 30, 40, 35, 45, 38, 42, 30, 25],
    'Drawing': [20, 15, 25, 22, 18, 20, 15, 25, 28, 35, 40, 30],
    'Sculpture': [7, 8, 12, 18, 25, 30, 28, 35, 30, 38, 42, 40]
}

df = pd.DataFrame(data)
df = df.set_index('Month')

df_cum = df.cumsum(axis=1)

colors = ['#FF6347', '#4682B4', '#32CD32']

plt.figure(figsize=(18, 12))

plt.fill_between(df.index, 0, df_cum['Painting'], color=colors[0], alpha=0.7, label='Painting')
plt.fill_between(df.index, df_cum['Painting'], df_cum['Painting'] + df_cum['Drawing'], color=colors[1], alpha=0.7, label='Drawing')
plt.fill_between(df.index, df_cum['Painting'] + df_cum['Drawing'], df_cum['Painting'] + df_cum['Drawing'] + df_cum['Sculpture'], color=colors[2], alpha=0.7, label='Sculpture')

for category in ['Painting', 'Drawing', 'Sculpture']:
    plt.text(df.index[-1], df_cum[category][-1] - (df_cum[category][-1] - df_cum[category].shift(1)[-1]) / 2, category, verticalalignment='center')

plt.title('Monthly Art Creation Trends', fontsize=16, pad=20)
plt.xlabel('Month')
plt.ylabel('Number of Art Pieces')
plt.xticks(rotation=45)
plt.legend(loc='upper right')
plt.tight_layout()

plt.show()