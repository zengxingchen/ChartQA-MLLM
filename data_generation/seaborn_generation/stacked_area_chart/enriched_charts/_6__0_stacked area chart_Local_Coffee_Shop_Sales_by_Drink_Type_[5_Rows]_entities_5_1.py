
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December'],
    'Meditation': [300, 320, 310, 340, 360, 370, 380, 390, 400, 410, 420, 430],
    'Yoga': [250, 260, 255, 270, 280, 290, 300, 310, 320, 330, 340, 350],
    'Therapy': [400, 420, 410, 430, 440, 450, 460, 470, 480, 490, 500, 510]
}

df = pd.DataFrame(data)
df = df.set_index('Month')

df_cum = df.cumsum(axis=1)

colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

plt.figure(figsize=(16, 10))

plt.fill_between(df.index, 0, df_cum['Meditation'], color=colors[0], alpha=0.6, label='Meditation')
plt.fill_between(df.index, df_cum['Meditation'], df_cum['Meditation'] + df_cum['Yoga'], color=colors[1], alpha=0.6, label='Yoga')
plt.fill_between(df.index, df_cum['Meditation'] + df_cum['Yoga'], df_cum['Meditation'] + df_cum['Yoga'] + df_cum['Therapy'], color=colors[2], alpha=0.6, label='Therapy')

for category in ['Meditation', 'Yoga', 'Therapy']:
    plt.text(df.index[-1], df_cum[category][-1] - (df_cum[category][-1] - df_cum[category].shift(1)[-1]) / 2, category, verticalalignment='center')

plt.title('Monthly Participation in Mental Health Activities', fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Participants', fontsize=14)
plt.xticks(rotation=45)
plt.legend(loc='upper right')
plt.tight_layout()

plt.show()