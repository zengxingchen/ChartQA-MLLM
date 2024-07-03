
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Category': 'Fiction', 'Early Career': 15, 'Mid Career': 20, 'Late Career': 25, 'Senior Career': 30, 'Retired': 10},
    {'Category': 'Non-Fiction', 'Early Career': 25, 'Mid Career': 20, 'Late Career': 20, 'Senior Career': 20, 'Retired': 30},
    {'Category': 'Biography', 'Early Career': 20, 'Mid Career': 15, 'Late Career': 25, 'Senior Career': 20, 'Retired': 20},
    {'Category': 'Science Fiction', 'Early Career': 20, 'Mid Career': 25, 'Late Career': 15, 'Senior Career': 20, 'Retired': 10},
    {'Category': 'Fantasy', 'Early Career': 20, 'Mid Career': 20, 'Late Career': 15, 'Senior Career': 10, 'Retired': 30}
]

df = pd.DataFrame(data)
df.set_index('Category', inplace=True)

df_percentage = df.div(df.sum(axis=1), axis=0) * 100

fig, ax = plt.subplots(figsize=(10, 12))

bar_width = 0.8
categories = df_percentage.index
colors = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3']

bottom = [0] * len(df_percentage.columns)

for i, col in enumerate(df.columns):
    ax.barh(categories, df_percentage[col], bar_width, label=col, color=colors[i], left=bottom)
    bottom = bottom + df_percentage[col].values

ax.set_xlabel('Percentage')
ax.set_ylabel('Category')
ax.set_title('Distribution of Reading Preferences by Career Stage', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1), ncol=1)

for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy()
    if width > 0:
        ax.text(x + width / 2,
                y + height / 2,
                f"{width:.1f}%",
                ha='center',
                va='center')

plt.tight_layout()
plt.show()