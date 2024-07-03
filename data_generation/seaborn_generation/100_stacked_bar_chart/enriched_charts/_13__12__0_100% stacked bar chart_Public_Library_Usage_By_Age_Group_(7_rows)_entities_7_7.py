
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Year': [2018, 2019, 2020, 2021, 2022, 2023],
    'Calories': [2500, 2450, 2400, 2350, 2300, 2250],
    'BMI': [22, 23, 22.5, 21.8, 21.5, 21.2],
    'Workouts': [3, 3.5, 4, 4.2, 4.5, 5],
    'Steps': [8000, 8200, 7800, 8500, 8700, 9000]
}
df = pd.DataFrame(data)

df_pct = df.set_index('Year').apply(lambda x: x / x.sum() * 100, axis=1).reset_index()

fig, ax = plt.subplots(figsize=(10, 12))

colors = ['#3498db', '#e74c3c', '#2ecc71', '#f1c40f']

bottom = pd.Series([0] * len(df_pct))
for i, col in enumerate(df.columns[1:]):
    ax.bar(
        df_pct['Year'],
        df_pct[col],
        bottom=bottom,
        color=colors[i],
        edgecolor='white',
        width=0.8
    )
    bottom += df_pct[col]

ax.set_xlabel('Year')
ax.set_ylabel('Percentage (%)')
plt.title('Fitness and Nutrition Data Over Years')

ax.set_xticks(df_pct['Year'])
ax.set_xticklabels(df_pct['Year'], rotation=0)
ax.legend(df.columns[1:], loc='upper left')

plt.tight_layout()
plt.show()