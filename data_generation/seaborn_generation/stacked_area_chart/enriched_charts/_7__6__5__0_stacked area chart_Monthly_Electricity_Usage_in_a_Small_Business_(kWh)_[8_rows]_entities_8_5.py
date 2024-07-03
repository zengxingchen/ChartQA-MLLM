
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Organic Food': [1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400],
    'Processed Food': [1300, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600],
    'Beverages': [1500, 1700, 1900, 2100, 2300, 2500, 2700, 2900, 3100, 3300, 3500, 3700]
}

df = pd.DataFrame(data)
df_melted = df.melt(id_vars='Month', var_name='Category', value_name='Sales')
df_melted['Month'] = pd.Categorical(df_melted['Month'], categories=data['Month'], ordered=True)

plt.figure(figsize=(18, 12))
sns.set(style="whitegrid")

colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]

sns.lineplot(data=df_melted, x='Month', y='Sales', hue='Category', palette=colors, sort=False, lw=2)

plt.fill_between(data['Month'], df["Organic Food"], color="#1f77b4", alpha=0.5)
plt.fill_between(data['Month'], df["Organic Food"], df["Organic Food"] + df["Processed Food"], color="#ff7f0e", alpha=0.5)
plt.fill_between(data['Month'], df["Organic Food"] + df["Processed Food"], df["Organic Food"] + df["Processed Food"] + df["Beverages"], color="#2ca02c", alpha=0.5)

for idx, month in enumerate(data['Month']):
    plt.text(x=idx, y=df.loc[idx, "Organic Food"]/2, s=df.loc[idx, "Organic Food"], ha='center', color='w')
    plt.text(x=idx, y=df.loc[idx, "Organic Food"] + df.loc[idx, "Processed Food"]/2, s=df.loc[idx, "Processed Food"], ha='center', color='w')
    plt.text(x=idx, y=df.loc[idx, "Organic Food"] + df.loc[idx, "Processed Food"] + df.loc[idx, "Beverages"]/2, s=df.loc[idx, "Beverages"], ha='center', color='w')

plt.xlabel('Month')
plt.ylabel('Sales (in $1000)')
plt.title('Monthly Sales for Food Categories')
plt.xticks(rotation=45)
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()