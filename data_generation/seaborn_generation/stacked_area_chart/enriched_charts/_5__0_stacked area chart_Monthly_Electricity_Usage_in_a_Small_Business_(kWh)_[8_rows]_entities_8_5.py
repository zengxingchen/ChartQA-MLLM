
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Research & Development': [3200, 3100, 3000, 2900, 2800, 2700, 2600, 2500, 2400, 2300, 2200, 2100],
    'Marketing': [2200, 2300, 2500, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500],
    'Administration': [2700, 2600, 2500, 2400, 2300, 2200, 2100, 2000, 1900, 1800, 1700, 1600]
}

df = pd.DataFrame(data)
df_melted = df.melt(id_vars='Month', var_name='Department', value_name='Budget')
df_melted['Month'] = pd.Categorical(df_melted['Month'], categories=data['Month'], ordered=True)

plt.figure(figsize=(14, 9))
sns.set(style="whitegrid")

colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]

sns.lineplot(data=df_melted, x='Month', y='Budget', hue='Department', palette=colors, sort=False, lw=2)

plt.fill_between(data['Month'], df["Research & Development"], color="#1f77b4", alpha=0.5)
plt.fill_between(data['Month'], df["Research & Development"], df["Research & Development"] + df["Marketing"], color="#ff7f0e", alpha=0.5)
plt.fill_between(data['Month'], df["Research & Development"] + df["Marketing"], df["Research & Development"] + df["Marketing"] + df["Administration"], color="#2ca02c", alpha=0.5)

for idx, month in enumerate(data['Month']):
    plt.text(x=idx, y=df.loc[idx, "Research & Development"]/2, s=df.loc[idx, "Research & Development"], ha='center', color='w')
    plt.text(x=idx, y=df.loc[idx, "Research & Development"] + df.loc[idx, "Marketing"]/2, s=df.loc[idx, "Marketing"], ha='center', color='w')
    plt.text(x=idx, y=df.loc[idx, "Research & Development"] + df.loc[idx, "Marketing"] + df.loc[idx, "Administration"]/2, s=df.loc[idx, "Administration"], ha='center', color='w')

plt.xlabel('Month')
plt.ylabel('Budget (in $1000)')
plt.title('Monthly Departmental Budgets in a Company')
plt.xticks(rotation=45)
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()