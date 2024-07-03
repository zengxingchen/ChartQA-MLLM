
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December'],
    'ArticlesPublished': [5, 8, 12, 15, 20, 25, 30, 35, 40, 45, 50, 55],
    'AuthorsActive': [3, 4, 6, 7, 10, 12, 15, 18, 20, 22, 25, 28],
    'Citations': [15, 20, 30, 35, 45, 55, 60, 70, 80, 90, 100, 110]
}

df = pd.DataFrame(data)
df = df.set_index('Month')

df_cum = df.cumsum(axis=1)

colors = ['#003f5c', '#bc5090', '#ffa600']

plt.figure(figsize=(18, 12))

plt.fill_between(df.index, 0, df_cum['ArticlesPublished'], color=colors[0], alpha=0.7, label='Articles Published')
plt.fill_between(df.index, df_cum['ArticlesPublished'], df_cum['ArticlesPublished'] + df_cum['AuthorsActive'], color=colors[1], alpha=0.7, label='Authors Active')
plt.fill_between(df.index, df_cum['ArticlesPublished'] + df_cum['AuthorsActive'], df_cum['ArticlesPublished'] + df_cum['AuthorsActive'] + df_cum['Citations'], color=colors[2], alpha=0.7, label='Citations')

for category in ['ArticlesPublished', 'AuthorsActive', 'Citations']:
    plt.text(df.index[-1], df_cum[category][-1] - (df_cum[category][-1] - df_cum[category].shift(1)[-1]) / 2, category.replace('Published', ' Published').replace('Active', ' Active').replace('Citations', ' Citations'), verticalalignment='center')

plt.title('Monthly Research Activity Tracker Data', fontsize=18, pad=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Values', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.legend(loc='upper left', fontsize=12)
plt.tight_layout()

plt.show()