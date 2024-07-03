
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = [
    {'Year': 2019, 'Tech Research (%)': 35, 'Product Development (%)': 25, 'Marketing (%)': 20, 'Customer Support (%)': 15, 'Other (%)': 5},
    {'Year': 2020, 'Tech Research (%)': 38, 'Product Development (%)': 22, 'Marketing (%)': 18, 'Customer Support (%)': 17, 'Other (%)': 5},
    {'Year': 2021, 'Tech Research (%)': 40, 'Product Development (%)': 20, 'Marketing (%)': 15, 'Customer Support (%)': 20, 'Other (%)': 5},
    {'Year': 2022, 'Tech Research (%)': 42, 'Product Development (%)': 18, 'Marketing (%)': 12, 'Customer Support (%)': 23, 'Other (%)': 5},
    {'Year': 2023, 'Tech Research (%)': 45, 'Product Development (%)': 15, 'Marketing (%)': 10, 'Customer Support (%)': 25, 'Other (%)': 5}
]

df = pd.DataFrame(data)
df.set_index('Year', inplace=True)
df_normalized = df.div(df.sum(axis=1), axis=0) * 100

colors = ['#1F77B4', '#FF7F0E', '#2CA02C', '#D62728', '#9467BD']

sns.set_style('whitegrid')

plt.figure(figsize=(10, 8))

bottom = None
bar_width = 0.6
for (columnName, columnData), color in zip(df_normalized.iteritems(), colors):
    plt.bar(df_normalized.index, columnData, bottom=bottom, color=color, label=columnName, edgecolor='white', width=bar_width)
    bottom = columnData if bottom is None else bottom + columnData

plt.legend(title="Business Operations")
plt.title('Business Operations Distribution Over the Years', pad=20)
plt.xlabel('Year')
plt.ylabel('Percentage Contribution (%)')
plt.yticks(range(0, 101, 10))
plt.xticks(df_normalized.index)
sns.despine()

plt.show()