
import matplotlib.pyplot as plt
import pandas as pd

data = [
    {'Year': 2018, 'TV Shows (%)': 20, 'Movies (%)': 25, 'Video Games (%)': 15, 'Music (%)': 25, 'Reading (%)': 15},
    {'Year': 2019, 'TV Shows (%)': 25, 'Movies (%)': 20, 'Video Games (%)': 20, 'Music (%)': 20, 'Reading (%)': 15},
    {'Year': 2020, 'TV Shows (%)': 30, 'Movies (%)': 15, 'Video Games (%)': 25, 'Music (%)': 15, 'Reading (%)': 15},
    {'Year': 2021, 'TV Shows (%)': 35, 'Movies (%)': 10, 'Video Games (%)': 30, 'Music (%)': 15, 'Reading (%)': 10},
    {'Year': 2022, 'TV Shows (%)': 40, 'Movies (%)': 10, 'Video Games (%)': 25, 'Music (%)': 15, 'Reading (%)': 10},
    {'Year': 2023, 'TV Shows (%)': 45, 'Movies (%)': 10, 'Video Games (%)': 20, 'Music (%)': 15, 'Reading (%)': 10}
]

df = pd.DataFrame(data)
df.set_index('Year', inplace=True)
cumulative_values = df.cumsum(axis=1)

colors = ['#4B0082', '#FF4500', '#00FF7F', '#1E90FF', '#FFD700']
fig, ax = plt.subplots(figsize=(10, 10))

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
ax.set_title('Time Spent on Entertainment Activities Over Years', pad=20)
ax.legend(title='Entertainment Activity', bbox_to_anchor=(1.05, 1), loc='upper left')

yticks = ax.get_yticks()
ax.set_yticklabels(['{}%'.format(int(y)) for y in yticks])

plt.tight_layout()
plt.show()