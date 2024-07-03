
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
    'Book_Sales': [
        400, 380, 350, 310, 290, 320, 305, 270, 290, 300, 250, 280,
        275, 285, 240, 230, 260, 220, 215, 295
    ]
}

df = pd.DataFrame(data)

sns.set(style="whitegrid")
plt.figure(figsize=(10, 12))

ax = sns.barplot(
    y="Country",
    x="Book_Sales",
    data=df,
    palette=[
        '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b',
        '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#9edae5', '#c49c94',
        '#f7b6d2', '#c5b0d5', '#ff9896', '#aec7e8', '#98df8a', '#ffbb78',
        '#ffbb78', '#c7c7c7'
    ]
)

ax.bar_label(ax.containers[0], fmt='%.0f', label_type='edge', padding=3)

ax.set(title='Book Sales by Country in 2023', xlabel='Book Sales (Thousands)', ylabel='Country')
ax.set_yticklabels(ax.get_yticklabels(), rotation=0)

plt.show()