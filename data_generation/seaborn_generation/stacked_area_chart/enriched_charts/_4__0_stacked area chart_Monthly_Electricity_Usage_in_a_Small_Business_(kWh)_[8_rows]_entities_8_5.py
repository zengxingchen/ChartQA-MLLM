
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Green Energy': [1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600],
    'Public Transportation': [3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100],
    'Recycling': [1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300]
}

df = pd.DataFrame(data)
df_melted = df.melt(id_vars='Month', var_name='Category', value_name='Values')
df_melted['Month'] = pd.Categorical(df_melted['Month'], categories=data['Month'], ordered=True)

plt.figure(figsize=(14, 10))
sns.set(style="whitegrid")

colors = ["#FF6347", "#4682B4", "#32CD32"]  # Green Energy, Public Transportation, Recycling

sns.lineplot(data=df_melted, x='Month', y='Values', hue='Category', palette=colors, sort=False, lw=2)

plt.fill_between(data['Month'], df["Green Energy"], color="#FF6347", alpha=0.5)
plt.fill_between(data['Month'], df["Green Energy"], df["Green Energy"] + df["Public Transportation"], color="#4682B4", alpha=0.5)
plt.fill_between(data['Month'], df["Green Energy"] + df["Public Transportation"], df["Green Energy"] + df["Public Transportation"] + df["Recycling"], color="#32CD32", alpha=0.5)

for idx, month in enumerate(data['Month']):
    if idx % 2 == 0:
        plt.text(x=idx, y=df.loc[idx, "Green Energy"]/2, s=df.loc[idx, "Green Energy"], ha='center', color='black')
        plt.text(x=idx, y=df.loc[idx, "Green Energy"] + df.loc[idx, "Public Transportation"]/2, s=df.loc[idx, "Public Transportation"], ha='center', color='black')
        plt.text(x=idx, y=df.loc[idx, "Green Energy"] + df.loc[idx, "Public Transportation"] + df.loc[idx, "Recycling"]/2, s=df.loc[idx, "Recycling"], ha='center', color='black')

plt.xlabel('Month')
plt.ylabel('Efforts')
plt.title('Monthly Efforts in Environmental Sustainability', pad=20)
plt.xticks(rotation=45)
plt.legend(loc='upper right')

plt.tight_layout()
plt.show()