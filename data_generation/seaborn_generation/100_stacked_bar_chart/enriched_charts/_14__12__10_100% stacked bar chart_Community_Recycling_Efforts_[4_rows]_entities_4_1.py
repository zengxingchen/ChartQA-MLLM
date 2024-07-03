
import matplotlib.pyplot as plt
import pandas as pd

data = [
    {'Year': 2018, 'Fruits (%)': 25, 'Vegetables (%)': 20, 'Grains (%)': 15, 'Protein (%)': 25, 'Dairy (%)': 15},
    {'Year': 2019, 'Fruits (%)': 27, 'Vegetables (%)': 18, 'Grains (%)': 17, 'Protein (%)': 23, 'Dairy (%)': 15},
    {'Year': 2020, 'Fruits (%)': 30, 'Vegetables (%)': 18, 'Grains (%)': 15, 'Protein (%)': 22, 'Dairy (%)': 15},
    {'Year': 2021, 'Fruits (%)': 32, 'Vegetables (%)': 17, 'Grains (%)': 16, 'Protein (%)': 20, 'Dairy (%)': 15},
    {'Year': 2022, 'Fruits (%)': 35, 'Vegetables (%)': 15, 'Grains (%)': 18, 'Protein (%)': 18, 'Dairy (%)': 14}
]

df = pd.DataFrame(data)
df.set_index('Year', inplace=True)
cumulative_values = df.cumsum(axis=1)

colors = ['#FF5733', '#33FF57', '#3357FF', '#FFC300', '#C70039']
fig, ax = plt.subplots(figsize=(12, 9))

bar_width = 0.7
for i, col in enumerate(df.columns):
    bottom_values = cumulative_values.iloc[:, i-1] if i > 0 else None
    ax.bar(
        df.index,
        df[col],
        bottom=bottom_values,
        color=colors[i],
        edgecolor='white',
        label=col,
        width=bar_width
    )

ax.set_xticks(df.index)
ax.set_xticklabels(df.index, rotation=0)
ax.set_xlabel('Year')
ax.set_ylabel('Percentage')
ax.set_title('Distribution of Food Preferences Over Years', pad=30)
ax.legend(title='Food Type', bbox_to_anchor=(1.05, 1), loc='upper left')

yticks = ax.get_yticks()
ax.set_yticklabels(['{}%'.format(int(y)) for y in yticks])

plt.tight_layout()
plt.show()