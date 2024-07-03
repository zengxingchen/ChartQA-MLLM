
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [2018, 2019, 2020, 2021, 2022, 2023],
    'Solar': [10, 15, 20, 25, 30, 35],
    'Wind': [20, 25, 30, 35, 40, 45],
    'Hydro': [30, 35, 25, 20, 15, 20],
    'Nuclear': [40, 25, 25, 20, 15, 0]
}
df = pd.DataFrame(data)

df_pct = df.set_index('Year').apply(lambda x: x / x.sum() * 100, axis=1).reset_index()

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#FF7F50', '#6495ED', '#3CB371', '#FFD700']

bottom = pd.Series([0] * len(df_pct))
for i, col in enumerate(df.columns[1:]):
    ax.bar(
        df_pct['Year'],
        df_pct[col],
        bottom=bottom,
        color=colors[i],
        edgecolor='white',
        width=0.5,
    )
    bottom += df_pct[col]

ax.set_xlabel('Year')
ax.set_ylabel('Percentage (%)')
plt.title('Energy Source Distribution Over Years', pad=20)

ax.set_xticks(df_pct['Year'])
ax.set_xticklabels(df_pct['Year'], rotation=0)
ax.legend(df.columns[1:], loc='upper left')

plt.tight_layout()
plt.show()