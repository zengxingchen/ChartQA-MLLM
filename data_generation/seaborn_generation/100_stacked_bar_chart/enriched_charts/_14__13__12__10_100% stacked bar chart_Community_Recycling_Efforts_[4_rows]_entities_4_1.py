
import matplotlib.pyplot as plt
import pandas as pd

data = [
    {'Year': 2018, 'Forest Cover (%)': 30, 'Air Quality (%)': 25, 'Renewable Energy (%)': 20, 'Wildlife Population (%)': 15, 'Water Quality (%)': 10},
    {'Year': 2019, 'Forest Cover (%)': 28, 'Air Quality (%)': 27, 'Renewable Energy (%)': 22, 'Wildlife Population (%)': 13, 'Water Quality (%)': 10},
    {'Year': 2020, 'Forest Cover (%)': 27, 'Air Quality (%)': 30, 'Renewable Energy (%)': 24, 'Wildlife Population (%)': 12, 'Water Quality (%)': 7},
    {'Year': 2021, 'Forest Cover (%)': 26, 'Air Quality (%)': 32, 'Renewable Energy (%)': 26, 'Wildlife Population (%)': 11, 'Water Quality (%)': 5},
    {'Year': 2022, 'Forest Cover (%)': 25, 'Air Quality (%)': 35, 'Renewable Energy (%)': 28, 'Wildlife Population (%)': 10, 'Water Quality (%)': 2}
]

df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

cumulative_values = df.cumsum(axis=1)

colors = ['#007F66', '#A52A2A', '#4682B4', '#FFD700', '#8B4513']
fig, ax = plt.subplots(figsize=(14, 10))

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
ax.set_xticklabels(df.index, rotation=45)
ax.set_xlabel('Year')
ax.set_ylabel('Percentage')
ax.set_title('Environmental Changes Over Years', pad=20)
ax.legend(title='Indicator', bbox_to_anchor=(1.05, 1), loc='upper left')

yticks = ax.get_yticks()
ax.set_yticklabels(['{}%'.format(int(y)) for y in yticks])

plt.tight_layout()
plt.show()