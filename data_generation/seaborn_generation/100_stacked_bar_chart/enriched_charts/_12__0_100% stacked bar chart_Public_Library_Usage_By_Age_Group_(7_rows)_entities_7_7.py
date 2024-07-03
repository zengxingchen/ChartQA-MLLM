
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [2018, 2019, 2020, 2021, 2022, 2023],
    'Stocks': [30, 35, 40, 45, 50, 55],
    'Bonds': [20, 18, 15, 12, 10, 8],
    'RealEstate': [25, 27, 30, 28, 25, 23],
    'Gold': [25, 20, 15, 15, 15, 14]
}
df = pd.DataFrame(data)

df_pct = df.set_index('Year').apply(lambda x: x / x.sum() * 100, axis=1).reset_index()

fig, ax = plt.subplots(figsize=(12, 8))

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

bottom = pd.Series([0] * len(df_pct))
for i, col in enumerate(df.columns[1:]):
    ax.bar(
        df_pct['Year'],
        df_pct[col],
        bottom=bottom,
        color=colors[i],
        edgecolor='white',
        width=0.6
    )
    bottom += df_pct[col]

ax.set_xlabel('Year')
ax.set_ylabel('Percentage (%)')
plt.title('Market Share of Investment Types Over Years')

ax.set_xticks(df_pct['Year'])
ax.set_xticklabels(df_pct['Year'], rotation=0)
ax.legend(df.columns[1:], loc='upper right')

plt.tight_layout()
plt.show()