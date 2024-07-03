
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Mars Exploration': [1200, 1300, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400],
    'Space Tourism': [1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900],
    'Moon Mission': [2200, 2100, 2000, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100]
}

df = pd.DataFrame(data)
df_melted = df.melt(id_vars='Month', var_name='Mission', value_name='Budget')
df_melted['Month'] = pd.Categorical(df_melted['Month'], categories=data['Month'], ordered=True)

plt.figure(figsize=(16, 10))
sns.set(style="whitegrid")

colors = ["#5DA5DA", "#FAA43A", "#60BD68"]

sns.lineplot(data=df_melted, x='Month', y='Budget', hue='Mission', palette=colors, sort=False, lw=2)

plt.fill_between(data['Month'], df["Mars Exploration"], color="#5DA5DA", alpha=0.5)
plt.fill_between(data['Month'], df["Mars Exploration"], df["Mars Exploration"] + df["Space Tourism"], color="#FAA43A", alpha=0.5)
plt.fill_between(data['Month'], df["Mars Exploration"] + df["Space Tourism"], df["Mars Exploration"] + df["Space Tourism"] + df["Moon Mission"], color="#60BD68", alpha=0.5)

for idx, month in enumerate(data['Month']):
    plt.text(x=idx, y=df.loc[idx, "Mars Exploration"]/2, s=df.loc[idx, "Mars Exploration"], ha='center', color='w')
    plt.text(x=idx, y=df.loc[idx, "Mars Exploration"] + df.loc[idx, "Space Tourism"]/2, s=df.loc[idx, "Space Tourism"], ha='center', color='w')
    plt.text(x=idx, y=df.loc[idx, "Mars Exploration"] + df.loc[idx, "Space Tourism"] + df.loc[idx, "Moon Mission"]/2, s=df.loc[idx, "Moon Mission"], ha='center', color='w')

plt.xlabel('Month')
plt.ylabel('Budget (in $1000)')
plt.title('Monthly Budgets for Space Missions')
plt.xticks(rotation=45)
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()