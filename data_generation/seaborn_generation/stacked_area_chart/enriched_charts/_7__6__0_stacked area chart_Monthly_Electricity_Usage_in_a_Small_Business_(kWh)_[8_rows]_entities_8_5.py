
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Books': [3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100],
    'Music': [2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300],
    'Movies': [1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900]
}

df = pd.DataFrame(data)

df_melted = df.melt(id_vars='Month', var_name='Category', value_name='Consumption')
df_melted['Month'] = pd.Categorical(df_melted['Month'], categories=data['Month'], ordered=True)

plt.figure(figsize=(16, 12))
sns.set(style="whitegrid")

colors = ["#FF6347", "#87CEFA", "#32CD32"]

sns.lineplot(data=df_melted, x='Month', y='Consumption', hue='Category', palette=colors, sort=False, lw=2)

plt.fill_between(data['Month'], df["Books"], color="#FF6347", alpha=0.5)
plt.fill_between(data['Month'], df["Books"], df["Books"] + df["Music"], color="#87CEFA", alpha=0.5)
plt.fill_between(data['Month'], df["Books"] + df["Music"], df["Books"] + df["Music"] + df["Movies"], color="#32CD32", alpha=0.5)

for idx, month in enumerate(data['Month']):
    plt.text(x=idx, y=df.loc[idx, "Books"]/2, s=df.loc[idx, "Books"], ha='center', color='black')
    plt.text(x=idx, y=df.loc[idx, "Books"] + df.loc[idx, "Music"]/2, s=df.loc[idx, "Music"], ha='center', color='black')
    plt.text(x=idx, y=df.loc[idx, "Books"] + df.loc[idx, "Music"] + df.loc[idx, "Movies"]/2, s=df.loc[idx, "Movies"], ha='center', color='black')

plt.xlabel('Month')
plt.ylabel('Consumption')
plt.title('Monthly Consumption of Entertainment Categories', pad=20)
plt.xticks(rotation=45)
plt.legend(loc='upper left')

plt.tight_layout()
plt.show()