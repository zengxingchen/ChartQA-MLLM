
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = [
    {'Year': 2019, 'Strength Training (%)': 25, 'Cardio (%)': 40, 'Flexibility (%)': 20, 'Balance (%)': 15},
    {'Year': 2020, 'Strength Training (%)': 28, 'Cardio (%)': 35, 'Flexibility (%)': 22, 'Balance (%)': 15},
    {'Year': 2021, 'Strength Training (%)': 30, 'Cardio (%)': 33, 'Flexibility (%)': 25, 'Balance (%)': 12},
    {'Year': 2022, 'Strength Training (%)': 26, 'Cardio (%)': 38, 'Flexibility (%)': 24, 'Balance (%)': 12},
    {'Year': 2023, 'Strength Training (%)': 29, 'Cardio (%)': 32, 'Flexibility (%)': 26, 'Balance (%)': 13}
]

df = pd.DataFrame(data)
df.set_index('Year', inplace=True)
df_normalized = df.div(df.sum(axis=1), axis=0) * 100

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
sns.set_style('whitegrid')
plt.figure(figsize=(8, 12))

bottom = None
bar_width = 0.5
for (columnName, columnData), color in zip(df_normalized.iteritems(), colors):
    plt.bar(df_normalized.index, columnData, bottom=bottom, color=color, label=columnName, edgecolor='white', width=bar_width)
    bottom = columnData if bottom is None else bottom + columnData

plt.legend(title="Exercise Composition", loc='upper left')
plt.title('Exercise Composition in Fitness Regimes Over the Years', pad=20)
plt.xlabel('Year')
plt.ylabel('Exercise Contribution (%)')
plt.yticks(range(0, 101, 10))
plt.xticks(df_normalized.index)
sns.despine()

plt.show()