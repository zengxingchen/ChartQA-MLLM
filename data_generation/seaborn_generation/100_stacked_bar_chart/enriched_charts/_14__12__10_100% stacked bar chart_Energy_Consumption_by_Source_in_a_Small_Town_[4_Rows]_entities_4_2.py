
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = [
    {'Year': 2019, 'Books (%)': 25, 'Video Games (%)': 30, 'Music (%)': 20, 'Movies (%)': 15, 'Sports (%)': 10},
    {'Year': 2020, 'Books (%)': 28, 'Video Games (%)': 25, 'Music (%)': 22, 'Movies (%)': 15, 'Sports (%)': 10},
    {'Year': 2021, 'Books (%)': 30, 'Video Games (%)': 20, 'Music (%)': 25, 'Movies (%)': 15, 'Sports (%)': 10},
    {'Year': 2022, 'Books (%)': 32, 'Video Games (%)': 18, 'Music (%)': 28, 'Movies (%)': 12, 'Sports (%)': 10},
    {'Year': 2023, 'Books (%)': 35, 'Video Games (%)': 15, 'Music (%)': 25, 'Movies (%)': 15, 'Sports (%)': 10}
]

df = pd.DataFrame(data)
df.set_index('Year', inplace=True)
df_normalized = df.div(df.sum(axis=1), axis=0) * 100

colors = ['#FF6347', '#4682B4', '#FFD700', '#6A5ACD', '#32CD32']

sns.set_style('whitegrid')

plt.figure(figsize=(8, 10))
bottom = None
bar_width = 0.8
for (columnName, columnData), color in zip(df_normalized.iteritems(), colors):
    plt.bar(df_normalized.index, columnData, bottom=bottom, color=color, label=columnName, edgecolor='white', width=bar_width)
    bottom = columnData if bottom is None else bottom + columnData

plt.legend(title="Leisure Activities", bbox_to_anchor=(1.05, 1))
plt.title('Leisure Activities Preference Over the Years', pad=20)
plt.xlabel('Year')
plt.ylabel('Activity Contribution (%)')
plt.yticks(range(0, 101, 10))
plt.xticks(df_normalized.index)
sns.despine()

plt.show()