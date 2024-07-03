
import matplotlib.pyplot as plt
import pandas as pd

data = [
    {'Year': 2018, 'Clothing (%)': 15, 'Footwear (%)': 25, 'Accessories (%)': 20, 'Beauty Products (%)': 30, 'Jewelry (%)': 10},
    {'Year': 2019, 'Clothing (%)': 20, 'Footwear (%)': 20, 'Accessories (%)': 25, 'Beauty Products (%)': 25, 'Jewelry (%)': 10},
    {'Year': 2020, 'Clothing (%)': 25, 'Footwear (%)': 15, 'Accessories (%)': 30, 'Beauty Products (%)': 20, 'Jewelry (%)': 10},
    {'Year': 2021, 'Clothing (%)': 30, 'Footwear (%)': 10, 'Accessories (%)': 35, 'Beauty Products (%)': 15, 'Jewelry (%)': 10},
    {'Year': 2022, 'Clothing (%)': 35, 'Footwear (%)': 5, 'Accessories (%)': 40, 'Beauty Products (%)': 10, 'Jewelry (%)': 10},
    {'Year': 2023, 'Clothing (%)': 40, 'Footwear (%)': 5, 'Accessories (%)': 35, 'Beauty Products (%)': 15, 'Jewelry (%)': 5}
]

df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

cumulative_values = df.cumsum(axis=1)

colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00']
fig, ax = plt.subplots(figsize=(14, 10))

bar_width = 0.5
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
ax.set_xticklabels(df.index)
ax.set_xlabel('Year')
ax.set_ylabel('Percentage')
ax.set_title('Investment Distribution in Fashion & Beauty Over Years', pad=20)
ax.legend(title='Fashion & Beauty Segment', bbox_to_anchor=(1.05, 1), loc='upper left')

xticks = ax.get_yticks()
ax.set_yticklabels(['{}%'.format(int(x)) for x in xticks])

plt.tight_layout()
plt.show()