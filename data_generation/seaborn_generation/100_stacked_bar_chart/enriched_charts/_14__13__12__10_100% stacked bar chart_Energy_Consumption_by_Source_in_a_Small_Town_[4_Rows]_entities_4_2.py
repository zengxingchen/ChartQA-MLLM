
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = [
    {'Year': 2019, 'Public Health (%)': 35, 'Education (%)': 25, 'Environment (%)': 20, 'Technology (%)': 20},
    {'Year': 2020, 'Public Health (%)': 40, 'Education (%)': 20, 'Environment (%)': 25, 'Technology (%)': 15},
    {'Year': 2021, 'Public Health (%)': 38, 'Education (%)': 22, 'Environment (%)': 18, 'Technology (%)': 22},
    {'Year': 2022, 'Public Health (%)': 30, 'Education (%)': 30, 'Environment (%)': 25, 'Technology (%)': 15},
    {'Year': 2023, 'Public Health (%)': 32, 'Education (%)': 28, 'Environment (%)': 20, 'Technology (%)': 20},
    {'Year': 2024, 'Public Health (%)': 34, 'Education (%)': 24, 'Environment (%)': 22, 'Technology (%)': 20}
]

df = pd.DataFrame(data)
df.set_index('Year', inplace=True)
df_normalized = df.div(df.sum(axis=1), axis=0) * 100

colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3']
sns.set_style('whitegrid')
plt.figure(figsize=(10, 6))

bottom = None
bar_width = 0.4
for (columnName, columnData), color in zip(df_normalized.iteritems(), colors):
    plt.bar(df_normalized.index, columnData, bottom=bottom, color=color, label=columnName, edgecolor='white', width=bar_width)
    bottom = columnData if bottom is None else bottom + columnData

plt.legend(title="Public Interest Areas", loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2)
plt.title('Public Interest Areas Over the Years', pad=20)
plt.xlabel('Year')
plt.ylabel('Interest Contribution (%)')
plt.yticks(range(0, 101, 10))
plt.xticks(df_normalized.index)
sns.despine()

plt.show()