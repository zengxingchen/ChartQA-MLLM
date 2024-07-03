
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Stargazing': [1200, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800],
    'Astronomy Clubs': [1400, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000],
    'Telescope Sales': [1600, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200]
}

df = pd.DataFrame(data)
df_melted = df.melt(id_vars='Month', var_name='Category', value_name='Values')
df_melted['Month'] = pd.Categorical(df_melted['Month'], categories=data['Month'], ordered=True)

plt.figure(figsize=(16, 12))
sns.set(style="whitegrid")

colors = ["#FF4500", "#1E90FF", "#32CD32"]  # Stargazing, Astronomy Clubs, Telescope Sales

sns.lineplot(data=df_melted, x='Month', y='Values', hue='Category', palette=colors, sort=False, lw=2)

plt.fill_between(data['Month'], df["Stargazing"], color="#FF4500", alpha=0.5)
plt.fill_between(data['Month'], df["Stargazing"], df["Stargazing"] + df["Astronomy Clubs"], color="#1E90FF", alpha=0.5)
plt.fill_between(data['Month'], df["Stargazing"] + df["Astronomy Clubs"], df["Stargazing"] + df["Astronomy Clubs"] + df["Telescope Sales"], color="#32CD32", alpha=0.5)

for idx, month in enumerate(data['Month']):
    if idx % 2 == 0:
        plt.text(x=idx, y=df.loc[idx, "Stargazing"]/2, s=df.loc[idx, "Stargazing"], ha='center', color='black')
        plt.text(x=idx, y=df.loc[idx, "Stargazing"] + df.loc[idx, "Astronomy Clubs"]/2, s=df.loc[idx, "Astronomy Clubs"], ha='center', color='black')
        plt.text(x=idx, y=df.loc[idx, "Stargazing"] + df.loc[idx, "Astronomy Clubs"] + df.loc[idx, "Telescope Sales"]/2, s=df.loc[idx, "Telescope Sales"], ha='center', color='black')

plt.xlabel('Month')
plt.ylabel('Activities')
plt.title('Monthly Trends in Astronomy & Space Exploration', pad=20)
plt.xticks(rotation=45)
plt.legend(loc='upper left')

plt.tight_layout()
plt.show()