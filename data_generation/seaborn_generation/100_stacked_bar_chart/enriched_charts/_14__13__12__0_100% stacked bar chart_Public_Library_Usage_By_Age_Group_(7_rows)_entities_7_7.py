
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [2018, 2019, 2020, 2021, 2022, 2023],
    'Books': [10, 8, 9, 7, 11, 12],
    'Articles': [5, 6, 7, 8, 9, 10],
    'Papers': [3, 4, 2, 6, 5, 7],
    'Websites': [2, 3, 4, 3, 4, 5]
}
df = pd.DataFrame(data)

df_pct = df.set_index('Year').apply(lambda x: x / x.sum() * 100, axis=1).reset_index()

fig, ax = plt.subplots(figsize=(12, 8))

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']

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
plt.title('Research and Reading Data Over Years')

ax.set_xticks(df_pct['Year'])
ax.set_xticklabels(df_pct['Year'], rotation=0)
ax.legend(df.columns[1:], loc='upper left')

plt.tight_layout()
plt.show()