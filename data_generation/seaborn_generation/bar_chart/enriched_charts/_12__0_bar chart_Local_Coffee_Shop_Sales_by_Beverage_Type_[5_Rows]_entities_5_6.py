
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
    'Life_Expectancy': [
        78.5, 76.9, 84.5, 81.1, 69.7, 81.2, 82.4, 75.5, 83.2, 82.3, 72.6,
        83.0, 83.4, 82.8, 75.0, 71.7, 81.7, 75.0, 77.4, 83.6
    ]
}

df = pd.DataFrame(data)

sns.set(style="whitegrid")
plt.figure(figsize=(14, 8))

ax = sns.barplot(
    x="Country",
    y="Life_Expectancy",
    data=df,
    palette=[ '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', 
              '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#aec7e8', '#ffbb78', 
              '#98df8a', '#ff9896', '#c5b0d5', '#c49c94', '#f7b6d2', '#c7c7c7', 
              '#dbdb8d', '#9edae5']
)

ax.bar_label(ax.containers[0], fmt='%.1f', label_type='edge', padding=3)
ax.set(title='Life Expectancy by Country', xlabel='Country', ylabel='Life Expectancy (Years)')

plt.xticks(rotation=90)
plt.show()