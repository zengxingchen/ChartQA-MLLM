
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Region A': [300, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420],
    'Region B': [450, 470, 480, 500, 510, 520, 530, 540, 550, 560, 570, 580],
    'Region C': [350, 370, 360, 380, 390, 400, 410, 420, 430, 440, 450, 460],
    'Region D': [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310]
}

df = pd.DataFrame(data)
df.index = df['Month']
df.drop('Month', axis=1, inplace=True)

plt.figure(figsize=(18, 10))
pal = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']

df_cum = df.cumsum(axis=1)
category_names = df.columns[::-1]
for i, column in enumerate(category_names):
    sns.lineplot(data=df_cum, x=df.index, y=column, color=pal[i])

for i, column in enumerate(category_names):
    if i == 0:
        sns.lineplot(data=df_cum, x=df.index, y=column, color=pal[i])
        plt.fill_between(df.index, 0, df_cum[column], facecolor=pal[i], alpha=0.5)
    else:
        sns.lineplot(data=df_cum, x=df.index, y=column, color=pal[i])
        plt.fill_between(df.index, df_cum[category_names[i - 1]], df_cum[column], facecolor=pal[i], alpha=0.5)

for i, value in enumerate(df_cum['Region D']):
    plt.text(i, value + 10, f"{value}", ha='center', va='bottom', fontsize=9)

plt.title('Monthly Internet Traffic by Region', fontsize=18, pad=20)
plt.xticks(rotation=45)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Data Usage (TB)', fontsize=14)
plt.legend(title='Regions', labels=df.columns, loc='upper left')
plt.tight_layout()
plt.show()