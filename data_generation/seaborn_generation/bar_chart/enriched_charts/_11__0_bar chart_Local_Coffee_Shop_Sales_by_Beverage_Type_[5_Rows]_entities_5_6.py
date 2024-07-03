
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Country': [
        'France', 'Spain', 'United States', 'China', 'Italy', 'Turkey', 'Mexico',
        'Germany', 'Thailand', 'United Kingdom', 'Japan', 'Austria', 'Greece',
        'Russia', 'Canada', 'Malaysia', 'Hong Kong', 'Portugal', 'Netherlands',
        'Saudi Arabia'
    ],
    'International_Tourists': [
        89000000, 82000000, 79000000, 65000000, 64000000, 51000000, 45000000,
        39000000, 38000000, 36000000, 32000000, 30000000, 29000000, 28000000,
        27000000, 25000000, 25000000, 24000000, 22000000, 21000000
    ]
}

df = pd.DataFrame(data)

sns.set(style="whitegrid")
plt.figure(figsize=(14, 8))

ax = sns.barplot(
    x="Country",
    y="International_Tourists",
    data=df,
    palette=[ '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', 
              '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#aec7e8', '#ffbb78', 
              '#98df8a', '#ff9896', '#c5b0d5', '#c49c94', '#f7b6d2', '#c7c7c7', 
              '#dbdb8d', '#9edae5']
)

ax.bar_label(ax.containers[0], fmt='%.0f', label_type='edge', padding=3)

ax.set(title='Number of International Tourists by Country', xlabel='Country', ylabel='International Tourists (in millions)')

plt.xticks(rotation=90)
plt.show()