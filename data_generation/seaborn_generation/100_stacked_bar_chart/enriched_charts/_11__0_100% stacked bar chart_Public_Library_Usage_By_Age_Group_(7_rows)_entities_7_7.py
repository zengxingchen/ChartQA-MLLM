
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Solar': [5, 10, 15, 20, 25],
    'Wind': [15, 18, 22, 25, 28],
    'Hydro': [30, 28, 26, 24, 22],
    'Nuclear': [50, 44, 37, 31, 25]
}
df = pd.DataFrame(data)

df_pct = df.set_index('Year').apply(lambda x: x / x.sum() * 100, axis=1).reset_index()

fig, ax = plt.subplots(figsize=(8, 10))

colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']

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
plt.title('Energy Source Share Over Years', pad=20)

ax.set_xticks(df_pct['Year'])
ax.set_xticklabels(df_pct['Year'], rotation=0)
ax.legend(df.columns[1:], loc='upper right')

plt.tight_layout()
plt.show()