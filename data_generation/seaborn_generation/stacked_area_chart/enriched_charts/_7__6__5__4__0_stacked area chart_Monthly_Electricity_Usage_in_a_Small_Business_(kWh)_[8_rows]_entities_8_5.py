
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Football': [800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350],
    'Basketball': [600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150],
    'Running': [400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950]
}

df = pd.DataFrame(data)
df_melted = df.melt(id_vars='Month', var_name='Category', value_name='Values')
df_melted['Month'] = pd.Categorical(df_melted['Month'], categories=data['Month'], ordered=True)

plt.figure(figsize=(16, 12))
sns.set(style="whitegrid")

colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]  # Football, Basketball, Running

sns.lineplot(data=df_melted, x='Month', y='Values', hue='Category', palette=colors, sort=False, lw=2)

plt.fill_between(data['Month'], df["Football"], color="#1f77b4", alpha=0.5)
plt.fill_between(data['Month'], df["Football"], df["Football"] + df["Basketball"], color="#ff7f0e", alpha=0.5)
plt.fill_between(data['Month'], df["Football"] + df["Basketball"], df["Football"] + df["Basketball"] + df["Running"], color="#2ca02c", alpha=0.5)

for idx, month in enumerate(data['Month']):
    plt.text(x=idx, y=df.loc[idx, "Football"]/2, s=df.loc[idx, "Football"], ha='center', color='black')
    plt.text(x=idx, y=df.loc[idx, "Football"] + df.loc[idx, "Basketball"]/2, s=df.loc[idx, "Basketball"], ha='center', color='black')
    plt.text(x=idx, y=df.loc[idx, "Football"] + df.loc[idx, "Basketball"] + df.loc[idx, "Running"]/2, s=df.loc[idx, "Running"], ha='center', color='black')

plt.xlabel('Month')
plt.ylabel('Participants')
plt.title('Monthly Participation in Sports Activities', pad=20)
plt.xticks(rotation=45)
plt.legend(loc='upper left')

plt.tight_layout()
plt.show()