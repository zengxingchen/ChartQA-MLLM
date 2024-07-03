
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Philosophy': [15, 18, 20, 25, 30],
    'Ethics': [20, 22, 25, 28, 35],
    'Logic': [35, 32, 30, 27, 20],
    'Metaphysics': [30, 28, 25, 20, 15]
}
df = pd.DataFrame(data)

df_pct = df.set_index('Year').apply(lambda x: x / x.sum() * 100, axis=1).reset_index()

fig, ax = plt.subplots(figsize=(10, 14))

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6']

bottom = pd.Series([0] * len(df_pct))
for i, col in enumerate(df.columns[1:]):
    ax.bar(
        df_pct['Year'],
        df_pct[col],
        bottom=bottom,
        color=colors[i],
        edgecolor='white',
        width=0.6,
    )
    bottom += df_pct[col]

ax.set_xlabel('Year')
ax.set_ylabel('Percentage (%)')
plt.title('Study Fields Share Over Years', pad=20, loc='right')

ax.set_xticks(df_pct['Year'])
ax.set_xticklabels(df_pct['Year'], rotation=45)
ax.legend(df.columns[1:], loc='lower right')

plt.tight_layout()
plt.show()