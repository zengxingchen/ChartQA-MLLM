
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December'],
    'Football': [500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720],
    'Basketball': [300, 310, 330, 350, 370, 390, 410, 430, 450, 470, 490, 510],
    'Running': [400, 420, 430, 450, 470, 490, 510, 530, 550, 570, 590, 610]
}

df = pd.DataFrame(data)
df = df.set_index('Month')

df_cum = df.cumsum(axis=1)

colors = ['#FF5733', '#33FF57', '#3357FF']

plt.figure(figsize=(14, 8))

plt.fill_between(df.index, 0, df_cum['Football'], color=colors[0], alpha=0.6, label='Football')
plt.fill_between(df.index, df_cum['Football'], df_cum['Football'] + df_cum['Basketball'], color=colors[1], alpha=0.6, label='Basketball')
plt.fill_between(df.index, df_cum['Football'] + df_cum['Basketball'], df_cum['Football'] + df_cum['Basketball'] + df_cum['Running'], color=colors[2], alpha=0.6, label='Running')

for category in ['Football', 'Basketball', 'Running']:
    plt.text(df.index[-1], df_cum[category][-1] - (df_cum[category][-1] - df_cum[category].shift(1)[-1]) / 2, category, verticalalignment='center')

plt.title('Monthly Participation in Sports Activities', fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Participants', fontsize=14)
plt.xticks(rotation=45)
plt.legend(loc='upper left')
plt.tight_layout()

plt.show()