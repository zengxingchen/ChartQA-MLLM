
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = [
    {'Year': 2019, 'Math (%)': 25, 'Science (%)': 20, 'English (%)': 25, 'History (%)': 15, 'Physical Education (%)': 15},
    {'Year': 2020, 'Math (%)': 28, 'Science (%)': 18, 'English (%)': 22, 'History (%)': 17, 'Physical Education (%)': 15},
    {'Year': 2021, 'Math (%)': 30, 'Science (%)': 15, 'English (%)': 25, 'History (%)': 20, 'Physical Education (%)': 10},
    {'Year': 2022, 'Math (%)': 27, 'Science (%)': 22, 'English (%)': 20, 'History (%)': 18, 'Physical Education (%)': 13},
    {'Year': 2023, 'Math (%)': 29, 'Science (%)': 19, 'English (%)': 23, 'History (%)': 17, 'Physical Education (%)': 12}
]

df = pd.DataFrame(data)
df.set_index('Year', inplace=True)
df_normalized = df.div(df.sum(axis=1), axis=0) * 100

colors = ['#4daf4a', '#377eb8', '#ff7f00', '#e41a1c', '#984ea3']

sns.set_style('whitegrid')

plt.figure(figsize=(8, 12))

bottom = None
bar_width = 0.7
for (columnName, columnData), color in zip(df_normalized.iteritems(), colors):
    plt.bar(df_normalized.index, columnData, bottom=bottom, color=color, label=columnName, edgecolor='white', width=bar_width)
    bottom = columnData if bottom is None else bottom + columnData

plt.legend(title="Subject Contribution", loc='upper left', bbox_to_anchor=(1,1))
plt.title('Subject Distribution Over the Years')
plt.xlabel('Year')
plt.ylabel('Contribution (%)')
plt.xticks(df_normalized.index)
plt.yticks(range(0, 101, 10))
sns.despine()

plt.show()