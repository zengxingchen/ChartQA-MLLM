
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Satellite Launches': [5, 7, 8, 10, 12, 15, 18, 20, 22, 25, 28, 30],
    'Space Missions': [10, 12, 15, 18, 20, 25, 30, 35, 38, 40, 45, 50],
    'Research Publications': [3, 4, 5, 6, 8, 10, 12, 14, 15, 18, 20, 22]
}

df = pd.DataFrame(data)
df_melted = df.melt(id_vars='Month', var_name='Category', value_name='Values')
df_melted['Month'] = pd.Categorical(df_melted['Month'], categories=data['Month'], ordered=True)

plt.figure(figsize=(16, 12))
sns.set(style="whitegrid")

colors = ["#1E90FF", "#32CD32", "#FFD700"]  # Satellite Launches, Space Missions, Research Publications

sns.lineplot(data=df_melted, x='Month', y='Values', hue='Category', palette=colors, sort=False, lw=2)

plt.fill_between(data['Month'], df["Satellite Launches"], color="#1E90FF", alpha=0.5)
plt.fill_between(data['Month'], df["Satellite Launches"], df["Satellite Launches"] + df["Space Missions"], color="#32CD32", alpha=0.5)
plt.fill_between(data['Month'], df["Satellite Launches"] + df["Space Missions"], df["Satellite Launches"] + df["Space Missions"] + df["Research Publications"], color="#FFD700", alpha=0.5)

for idx, month in enumerate(data['Month']):
    if idx % 2 == 0:
        plt.text(x=idx, y=df.loc[idx, "Satellite Launches"]/2, s=df.loc[idx, "Satellite Launches"], ha='center', color='black')
        plt.text(x=idx, y=df.loc[idx, "Satellite Launches"] + df.loc[idx, "Space Missions"]/2, s=df.loc[idx, "Space Missions"], ha='center', color='black')
        plt.text(x=idx, y=df.loc[idx, "Satellite Launches"] + df.loc[idx, "Space Missions"] + df.loc[idx, "Research Publications"]/2, s=df.loc[idx, "Research Publications"], ha='center', color='black')

plt.xlabel('Month')
plt.ylabel('Activities')
plt.title('Monthly Progress in Astronomy & Space Exploration', pad=20)
plt.xticks(rotation=45)
plt.legend(loc='upper left')

plt.tight_layout()
plt.show()