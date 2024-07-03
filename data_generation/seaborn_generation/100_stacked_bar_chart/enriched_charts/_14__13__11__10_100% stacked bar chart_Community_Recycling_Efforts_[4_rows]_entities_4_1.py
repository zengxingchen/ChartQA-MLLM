
import matplotlib.pyplot as plt
import pandas as pd

data = [
    {'Year': 2018, 'Math (%)': 10, 'Science (%)': 20, 'English (%)': 30, 'History (%)': 25, 'Physical Education (%)': 15},
    {'Year': 2019, 'Math (%)': 15, 'Science (%)': 25, 'English (%)': 25, 'History (%)': 20, 'Physical Education (%)': 15},
    {'Year': 2020, 'Math (%)': 20, 'Science (%)': 30, 'English (%)': 20, 'History (%)': 15, 'Physical Education (%)': 15},
    {'Year': 2021, 'Math (%)': 25, 'Science (%)': 35, 'English (%)': 15, 'History (%)': 10, 'Physical Education (%)': 15},
    {'Year': 2022, 'Math (%)': 30, 'Science (%)': 40, 'English (%)': 10, 'History (%)': 5, 'Physical Education (%)': 15},
    {'Year': 2023, 'Math (%)': 35, 'Science (%)': 35, 'English (%)': 10, 'History (%)': 5, 'Physical Education (%)': 15}
]

df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

cumulative_values = df.cumsum(axis=1)

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
fig, ax = plt.subplots(figsize=(10, 12))

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
ax.set_xticklabels(df.index)
ax.set_xlabel('Year')
ax.set_ylabel('Percentage')
ax.set_title('Subject Distribution in Education Over Years', pad=20)
ax.legend(title='Subject', bbox_to_anchor=(1.05, 1), loc='upper left')

xticks = ax.get_yticks()
ax.set_yticklabels(['{}%'.format(int(x)) for x in xticks])

plt.tight_layout()
plt.show()