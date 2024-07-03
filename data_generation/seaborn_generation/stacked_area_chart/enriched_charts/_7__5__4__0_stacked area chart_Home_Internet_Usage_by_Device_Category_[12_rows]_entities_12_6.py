
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Revenue from Tickets': [120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230],
    'Revenue from Merchandise': [80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135],
    'Revenue from Sponsorships': [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210]
}

df = pd.DataFrame(data)
df_melted = df.melt('Month', var_name='Revenue Type', value_name='Revenue')

df_melted['Month'] = pd.Categorical(df_melted['Month'],
                                    categories=data['Month'],
                                    ordered=True)

plt.figure(figsize=(18, 12))

colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]

plt.stackplot(df['Month'], df.iloc[:, 1:].values.T, labels=df.columns[1:], colors=colors, alpha=0.8)

plt.title('Monthly Revenue from Different Sources in Entertainment Industry', fontsize=22, loc='center', pad=25)
plt.ylabel('Revenue (in $ thousands)', fontsize=18)
plt.xlabel('Month', fontsize=18)
plt.xticks(rotation=45)
plt.legend(title='Revenue Type', loc='upper left')

for i, row in df.iterrows():
    total_revenue = row['Revenue from Tickets'] + row['Revenue from Merchandise'] + row['Revenue from Sponsorships']
    plt.text(row['Month'], total_revenue, f'{total_revenue}', ha='center', va='bottom')

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.tight_layout()
plt.show()