
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Country': [
        'United States', 'China', 'Japan', 'Germany', 'India', 'United Kingdom',
        'France', 'Brazil', 'Italy', 'Canada', 'Russia', 'South Korea',
        'Spain', 'Australia', 'Mexico', 'Indonesia', 'Netherlands', 'Saudi Arabia',
        'Turkey', 'Switzerland'
    ],
    'Internet_Usage': [
        87, 65, 84, 90, 55, 92, 88, 75, 80, 91, 73, 95,
        86, 94, 72, 50, 93, 70, 68, 89
    ]
}

df = pd.DataFrame(data)

sns.set(style="whitegrid")
plt.figure(figsize=(12, 8))

ax = sns.barplot(
    x="Country",
    y="Internet_Usage",
    data=df,
    palette=[
        '#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', '#ffff33',
        '#a65628', '#f781bf', '#999999', '#a6cee3', '#1f78b4', '#b2df8a',
        '#33a02c', '#fb9a99', '#e31a1c', '#fdbf6f', '#ff7f00', '#cab2d6',
        '#6a3d9a', '#b15928'
    ],
    width=0.6
)

ax.bar_label(ax.containers[0], fmt='%.0f', label_type='edge', padding=3)

ax.set(title='Internet Usage by Country in 2023', xlabel='Country', ylabel='Internet Usage (%)')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

plt.show()