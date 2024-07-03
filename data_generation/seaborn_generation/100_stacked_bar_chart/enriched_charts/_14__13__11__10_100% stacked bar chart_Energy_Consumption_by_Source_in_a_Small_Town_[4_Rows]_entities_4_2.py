
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = [
    {'Year': 2019, 'Reading (%)': 20, 'Gaming (%)': 25, 'Sleeping (%)': 30, 'Eating (%)': 15, 'Other (%)': 10},
    {'Year': 2020, 'Reading (%)': 22, 'Gaming (%)': 27, 'Sleeping (%)': 28, 'Eating (%)': 13, 'Other (%)': 10},
    {'Year': 2021, 'Reading (%)': 19, 'Gaming (%)': 30, 'Sleeping (%)': 32, 'Eating (%)': 11, 'Other (%)': 8},
    {'Year': 2022, 'Reading (%)': 25, 'Gaming (%)': 28, 'Sleeping (%)': 27, 'Eating (%)': 12, 'Other (%)': 8},
    {'Year': 2023, 'Reading (%)': 28, 'Gaming (%)': 25, 'Sleeping (%)': 25, 'Eating (%)': 15, 'Other (%)': 7}
]

df = pd.DataFrame(data)
df.set_index('Year', inplace=True)
df_normalized = df.div(df.sum(axis=1), axis=0) * 100

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

sns.set_style('whitegrid')
plt.figure(figsize=(10, 6))

bottom = None
bar_width = 0.7
for (columnName, columnData), color in zip(df_normalized.iteritems(), colors):
    plt.bar(df_normalized.index, columnData, bottom=bottom, color=color, label=columnName, edgecolor='white', width=bar_width)
    bottom = columnData if bottom is None else bottom + columnData

plt.legend(title="Daily Activity", bbox_to_anchor=(1.05, 1), loc='upper left')

plt.title('Leisure Activity Distribution Over the Years', pad=20)
plt.xlabel('Year')
plt.ylabel('Activity Contribution (%)')
plt.yticks(range(0, 101, 10))
plt.xticks(df_normalized.index)
sns.despine()

plt.show()