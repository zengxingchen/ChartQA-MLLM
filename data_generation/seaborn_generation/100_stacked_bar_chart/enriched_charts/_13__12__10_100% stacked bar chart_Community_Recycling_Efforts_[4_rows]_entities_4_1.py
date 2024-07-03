
import matplotlib.pyplot as plt
import pandas as pd

data = [
    {'Year': 2018, 'Painting (%)': 15, 'Sculpture (%)': 20, 'Photography (%)': 25, 'Drawing (%)': 20, 'Crafts (%)': 20},
    {'Year': 2019, 'Painting (%)': 18, 'Sculpture (%)': 18, 'Photography (%)': 22, 'Drawing (%)': 22, 'Crafts (%)': 20},
    {'Year': 2020, 'Painting (%)': 20, 'Sculpture (%)': 17, 'Photography (%)': 20, 'Drawing (%)': 23, 'Crafts (%)': 20},
    {'Year': 2021, 'Painting (%)': 22, 'Sculpture (%)': 16, 'Photography (%)': 18, 'Drawing (%)': 24, 'Crafts (%)': 20},
    {'Year': 2022, 'Painting (%)': 25, 'Sculpture (%)': 15, 'Photography (%)': 16, 'Drawing (%)': 24, 'Crafts (%)': 20}
]

df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

cumulative_values = df.cumsum(axis=1)

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FFA533']
fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.6
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
ax.set_title('Trends in Art & Design Preferences Over Years', pad=20)
ax.legend(title='Art Form', bbox_to_anchor=(1.05, 1), loc='upper left')

yticks = ax.get_yticks()
ax.set_yticklabels(['{}%'.format(int(y)) for y in yticks])

plt.tight_layout()
plt.show()