
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Product A': [5000, 4800, 5100, 5300, 5200, 5400, 5600, 5500, 5700, 5900, 5800, 6000],
    'Product B': [4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900, 5000, 5100, 5200, 5300],
    'Product C': [3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100]
}

df = pd.DataFrame(data)
df_melted = df.melt(id_vars='Month', var_name='Product', value_name='Sales')
df_melted['Month'] = pd.Categorical(df_melted['Month'], categories=data['Month'], ordered=True)

plt.figure(figsize=(16, 10))
sns.set(style="whitegrid")

colors = ["#FF5733", "#33FF57", "#3357FF"]

sns.lineplot(data=df_melted, x='Month', y='Sales', hue='Product', palette=colors, sort=False, lw=2)

plt.fill_between(data['Month'], df["Product A"], color="#FF5733", alpha=0.5)
plt.fill_between(data['Month'], df["Product A"], df["Product A"] + df["Product B"], color="#33FF57", alpha=0.5)
plt.fill_between(data['Month'], df["Product A"] + df["Product B"], df["Product A"] + df["Product B"] + df["Product C"], color="#3357FF", alpha=0.5)

for idx, month in enumerate(data['Month']):
    plt.text(x=idx, y=df.loc[idx, "Product A"]/2, s=df.loc[idx, "Product A"], ha='center', color='w')
    plt.text(x=idx, y=df.loc[idx, "Product A"] + df.loc[idx, "Product B"]/2, s=df.loc[idx, "Product B"], ha='center', color='w')
    plt.text(x=idx, y=df.loc[idx, "Product A"] + df.loc[idx, "Product B"] + df.loc[idx, "Product C"]/2, s=df.loc[idx, "Product C"], ha='center', color='w')

plt.xlabel('Month')
plt.ylabel('Sales (in $1000)')
plt.title('Monthly Product Sales in a Store')
plt.xticks(rotation=45)
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()