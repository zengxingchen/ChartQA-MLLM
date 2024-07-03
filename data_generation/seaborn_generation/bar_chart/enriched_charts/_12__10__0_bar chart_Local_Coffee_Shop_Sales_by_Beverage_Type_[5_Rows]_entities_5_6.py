
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
    'Happiness_Index': [
        7.0, 5.8, 5.9, 6.9, 4.3, 7.2, 6.5, 6.3, 6.7, 7.4, 5.5, 5.4,
        6.3, 7.3, 6.6, 5.1, 7.6, 6.4, 4.8, 7.8
    ]
}

df = pd.DataFrame(data)

sns.set(style="whitegrid")
plt.figure(figsize=(10, 12))

ax = sns.barplot(
    y="Country",
    x="Happiness_Index",
    data=df,
    palette=[
        '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6',
        '#c4e17f', '#76D7C4', '#F7DC6F', '#85C1E9', '#E59866', '#AF7AC5',
        '#F5B7B1', '#D7BDE2', '#A2D9CE', '#D5DBDB', '#E74C3C', '#16A085',
        '#F1948A', '#5499C7'
    ]
)

ax.bar_label(ax.containers[0], fmt='%.1f', label_type='edge', padding=3)

ax.set(title='Happiness Index by Country in 2023', xlabel='Happiness Index', ylabel='Country')
ax.set_yticklabels(ax.get_yticklabels(), rotation=0, ha="right")

plt.show()