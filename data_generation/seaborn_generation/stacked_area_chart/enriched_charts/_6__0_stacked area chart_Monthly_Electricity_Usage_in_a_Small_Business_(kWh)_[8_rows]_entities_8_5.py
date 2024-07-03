
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Fruits': [1800, 1900, 2100, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100],
    'Vegetables': [2500, 2300, 2400, 2200, 2100, 2000, 1900, 1800, 1700, 1600, 1500, 1400],
    'Dairy': [2200, 2000, 2100, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700]
}

df = pd.DataFrame(data)

df_melted = df.melt(id_vars='Month', var_name='Category', value_name='Sales')
df_melted['Month'] = pd.Categorical(df_melted['Month'], categories=data['Month'], ordered=True)

plt.figure(figsize=(14, 10))
sns.set(style="whitegrid")

colors = ["#FFA07A", "#98FB98", "#4682B4"]

sns.lineplot(data=df_melted, x='Month', y='Sales', hue='Category', palette=colors, sort=False, lw=2)

plt.fill_between(data['Month'], df["Fruits"], color="#FFA07A", alpha=0.5)
plt.fill_between(data['Month'], df["Fruits"], df["Fruits"] + df["Vegetables"], color="#98FB98", alpha=0.5)
plt.fill_between(data['Month'], df["Fruits"] + df["Vegetables"], df["Fruits"] + df["Vegetables"] + df["Dairy"], color="#4682B4", alpha=0.5)

for idx, month in enumerate(data['Month']):
    plt.text(x=idx, y=df.loc[idx, "Fruits"]/2, s=df.loc[idx, "Fruits"], ha='center', color='black')
    plt.text(x=idx, y=df.loc[idx, "Fruits"] + df.loc[idx, "Vegetables"]/2, s=df.loc[idx, "Vegetables"], ha='center', color='black')
    plt.text(x=idx, y=df.loc[idx, "Fruits"] + df.loc[idx, "Vegetables"] + df.loc[idx, "Dairy"]/2, s=df.loc[idx, "Dairy"], ha='center', color='black')

plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales of Food Categories')
plt.xticks(rotation=45)
plt.legend(loc='upper right')

plt.tight_layout()
plt.show()