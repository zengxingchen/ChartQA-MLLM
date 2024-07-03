
import matplotlib.pyplot as plt
import pandas as pd

data = [
    {'Year': 2018, 'Adventure (%)': 20, 'Relaxation (%)': 25, 'Cultural (%)': 15, 'Food (%)': 25, 'Shopping (%)': 15},
    {'Year': 2019, 'Adventure (%)': 22, 'Relaxation (%)': 20, 'Cultural (%)': 18, 'Food (%)': 20, 'Shopping (%)': 20},
    {'Year': 2020, 'Adventure (%)': 18, 'Relaxation (%)': 30, 'Cultural (%)': 10, 'Food (%)': 25, 'Shopping (%)': 17},
    {'Year': 2021, 'Adventure (%)': 25, 'Relaxation (%)': 15, 'Cultural (%)': 20, 'Food (%)': 20, 'Shopping (%)': 20},
    {'Year': 2022, 'Adventure (%)': 30, 'Relaxation (%)': 10, 'Cultural (%)': 25, 'Food (%)': 15, 'Shopping (%)': 20}
]

df = pd.DataFrame(data)
df.set_index('Year', inplace=True)
cumulative_values = df.cumsum(axis=1)

colors = ['#6baed6', '#fd8d3c', '#74c476', '#e377c2', '#ff9896']
fig, ax = plt.subplots(figsize=(10, 14))

bar_width = 0.8
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
ax.set_title('Travel Preferences Over Years', pad=30)
ax.legend(title='Type of Travel', bbox_to_anchor=(1.05, 1), loc='upper left')

yticks = ax.get_yticks()
ax.set_yticklabels(['{}%'.format(int(y)) for y in yticks])

plt.tight_layout()
plt.show()