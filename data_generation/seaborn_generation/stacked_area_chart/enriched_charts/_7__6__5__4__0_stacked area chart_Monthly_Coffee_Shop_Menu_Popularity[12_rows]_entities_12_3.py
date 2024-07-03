
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'North America': [90, 110, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220],
    'Europe': [120, 130, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240],
    'Asia': [80, 100, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210],
    'Africa': [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]
}

df = pd.DataFrame(data)
df.index = df['Month']
df.drop('Month', axis=1, inplace=True)

plt.figure(figsize=(14, 8))
pal = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

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

for i, value in enumerate(df_cum['Africa']):
    plt.text(i, value + 10, f"{value}", ha='center', va='bottom', fontsize=9)

plt.title('Monthly Rainfall by Region', fontsize=18, pad=30)
plt.xticks(rotation=45)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Rainfall (mm)', fontsize=14)
plt.legend(title='Regions', labels=df.columns, loc='upper left')
plt.tight_layout()
plt.show()