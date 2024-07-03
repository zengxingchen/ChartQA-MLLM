
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Electronics': [500, 520, 530, 550, 560, 580, 600, 620, 630, 640, 660, 680],
    'Furniture': [300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410],
    'Clothing': [400, 420, 430, 450, 460, 470, 480, 490, 500, 510, 520, 530],
    'Toys': [250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360]
}

df = pd.DataFrame(data)
df.index = df['Month']
df.drop('Month', axis=1, inplace=True)

plt.figure(figsize=(18, 10))
pal = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

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

for i, value in enumerate(df_cum['Toys']):
    plt.text(i, value + 10, f"{value}", ha='center', va='bottom', fontsize=9)

plt.title('Monthly Sales by Product Category', fontsize=18, pad=30)
plt.xticks(rotation=45)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Number of Sales', fontsize=14)
plt.legend(title='Product Categories', labels=df.columns, loc='upper left')
plt.tight_layout()
plt.show()