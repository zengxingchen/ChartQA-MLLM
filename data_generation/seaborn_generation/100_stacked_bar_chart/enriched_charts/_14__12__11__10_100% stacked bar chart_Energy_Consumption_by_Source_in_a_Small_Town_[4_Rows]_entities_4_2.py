
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = [
    {'Year': 2019, 'Pop': 25, 'Rock': 20, 'Jazz': 15, 'Classical': 30, 'Electronic': 10},
    {'Year': 2020, 'Pop': 28, 'Rock': 18, 'Jazz': 20, 'Classical': 25, 'Electronic': 9},
    {'Year': 2021, 'Pop': 30, 'Rock': 22, 'Jazz': 18, 'Classical': 20, 'Electronic': 10},
    {'Year': 2022, 'Pop': 27, 'Rock': 25, 'Jazz': 20, 'Classical': 18, 'Electronic': 10},
    {'Year': 2023, 'Pop': 29, 'Rock': 24, 'Jazz': 19, 'Classical': 22, 'Electronic': 6}
]

df = pd.DataFrame(data)
df.set_index('Year', inplace=True)
df_normalized = df.div(df.sum(axis=1), axis=0) * 100

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

sns.set_style('whitegrid')
plt.figure(figsize=(10, 14))

bottom = None
bar_width = 0.7
for (columnName, columnData), color in zip(df_normalized.iteritems(), colors):
    plt.bar(df_normalized.index, columnData, bottom=bottom, color=color, label=columnName, edgecolor='white', width=bar_width)
    bottom = columnData if bottom is None else bottom + columnData

plt.legend(title="Music Genre", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.title('Music Genre Popularity Over the Years', pad=20)
plt.xlabel('Year')
plt.ylabel('Genre Contribution (%)')
plt.yticks(range(0, 101, 10))
plt.xticks(df_normalized.index)
sns.despine()

plt.show()