
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [2018, 2019, 2020, 2021, 2022, 2023],
    'Category_A': [25, 30, 20, 35, 30, 25],
    'Category_B': [35, 30, 25, 20, 30, 35],
    'Category_C': [15, 20, 30, 25, 25, 30],
    'Category_D': [25, 20, 25, 20, 15, 10]
}
df = pd.DataFrame(data)

df_pct = df.set_index('Year').apply(lambda x: x / x.sum() * 100, axis=1).reset_index()

fig, ax = plt.subplots(figsize=(10, 12))

colors = ['#FFA07A', '#20B2AA', '#778899', '#DAA520']

bottom = pd.Series([0] * len(df_pct))
for i, col in enumerate(df.columns[1:]):
    ax.barh(
        df_pct['Year'],
        df_pct[col],
        left=bottom,
        color=colors[i],
        edgecolor='white',
        height=0.6,
    )
    bottom += df_pct[col]

ax.set_ylabel('Year')
ax.set_xlabel('Percentage (%)')
plt.title('Category Distribution Over Years', pad=20)

ax.set_yticks(df_pct['Year'])
ax.set_yticklabels(df_pct['Year'], rotation=0)
ax.legend(df.columns[1:], loc='lower right')

plt.tight_layout()
plt.show()