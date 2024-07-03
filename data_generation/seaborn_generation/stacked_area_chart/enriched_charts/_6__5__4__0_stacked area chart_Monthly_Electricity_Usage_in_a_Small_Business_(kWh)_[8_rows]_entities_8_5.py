
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Streaming': [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600],
    'Social Media': [900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],
    'Video Games': [1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400]
}

df = pd.DataFrame(data)
df_melted = df.melt(id_vars='Month', var_name='Category', value_name='Values')
df_melted['Month'] = pd.Categorical(df_melted['Month'], categories=data['Month'], ordered=True)

plt.figure(figsize=(14, 10))
sns.set(style="whitegrid")

colors = ["#FF5733", "#33FFBD", "#335BFF"]  # Streaming, Social Media, Video Games

sns.lineplot(data=df_melted, x='Month', y='Values', hue='Category', palette=colors, sort=False, lw=2)

plt.fill_between(data['Month'], df["Streaming"], color="#FF5733", alpha=0.5)
plt.fill_between(data['Month'], df["Streaming"], df["Streaming"] + df["Social Media"], color="#33FFBD", alpha=0.5)
plt.fill_between(data['Month'], df["Streaming"] + df["Social Media"], df["Streaming"] + df["Social Media"] + df["Video Games"], color="#335BFF", alpha=0.5)

for idx, month in enumerate(data['Month']):
    if idx % 2 == 0:
        plt.text(x=idx, y=df.loc[idx, "Streaming"]/2, s=df.loc[idx, "Streaming"], ha='center', color='black')
        plt.text(x=idx, y=df.loc[idx, "Streaming"] + df.loc[idx, "Social Media"]/2, s=df.loc[idx, "Social Media"], ha='center', color='black')
        plt.text(x=idx, y=df.loc[idx, "Streaming"] + df.loc[idx, "Social Media"] + df.loc[idx, "Video Games"]/2, s=df.loc[idx, "Video Games"], ha='center', color='black')

plt.xlabel('Month')
plt.ylabel('Activities')
plt.title('Monthly Trends in Entertainment & Leisure', pad=20)
plt.xticks(rotation=45)
plt.legend(loc='upper right')

plt.tight_layout()
plt.show()