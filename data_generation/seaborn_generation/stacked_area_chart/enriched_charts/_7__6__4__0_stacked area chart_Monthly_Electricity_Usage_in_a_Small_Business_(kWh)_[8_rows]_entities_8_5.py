
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Stars': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105],
    'Planets': [60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115],
    'Galaxies': [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
}

df = pd.DataFrame(data)
df_melted = df.melt(id_vars='Month', var_name='Celestial Object', value_name='Values')
df_melted['Month'] = pd.Categorical(df_melted['Month'], categories=data['Month'], ordered=True)

plt.figure(figsize=(18, 10))
sns.set(style="whitegrid")

colors = ["#FF6347", "#4682B4", "#32CD32"]  # Stars, Planets, Galaxies

sns.lineplot(data=df_melted, x='Month', y='Values', hue='Celestial Object', palette=colors, sort=False, lw=2)

plt.fill_between(data['Month'], df["Stars"], color="#FF6347", alpha=0.5)
plt.fill_between(data['Month'], df["Stars"], df["Stars"] + df["Planets"], color="#4682B4", alpha=0.5)
plt.fill_between(data['Month'], df["Stars"] + df["Planets"], df["Stars"] + df["Planets"] + df["Galaxies"], color="#32CD32", alpha=0.5)

for idx, month in enumerate(data['Month']):
    if idx % 2 == 0:
        plt.text(x=idx, y=df.loc[idx, "Stars"]/2, s=df.loc[idx, "Stars"], ha='center', color='black')
        plt.text(x=idx, y=df.loc[idx, "Stars"] + df.loc[idx, "Planets"]/2, s=df.loc[idx, "Planets"], ha='center', color='black')
        plt.text(x=idx, y=df.loc[idx, "Stars"] + df.loc[idx, "Planets"] + df.loc[idx, "Galaxies"]/2, s=df.loc[idx, "Galaxies"], ha='center', color='black')

plt.xlabel('Month')
plt.ylabel('Observation Hours')
plt.title('Monthly Observation Hours of Celestial Objects', pad=20, loc='left')
plt.xticks(rotation=45)
plt.legend(loc='upper left')

plt.tight_layout()
plt.show()