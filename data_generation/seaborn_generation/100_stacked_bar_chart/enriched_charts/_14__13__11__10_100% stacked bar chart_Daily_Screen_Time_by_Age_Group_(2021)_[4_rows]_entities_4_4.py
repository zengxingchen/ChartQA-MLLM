import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Category': 'Primary Education', 'Research & Development': 18, 'Marketing': 22, 'Manufacturing': 30, 'Sales': 30},
    {'Category': 'Higher Education', 'Research & Development': 40, 'Marketing': 10, 'Manufacturing': 35, 'Sales': 15},
    {'Category': 'Online Courses', 'Research & Development': 25, 'Marketing': 25, 'Manufacturing': 30, 'Sales': 20},
    {'Category': 'Vocational Training', 'Research & Development': 20, 'Marketing': 30, 'Manufacturing': 30, 'Sales': 20},
    {'Category': 'Special Education', 'Research & Development': 15, 'Marketing': 25, 'Manufacturing': 40, 'Sales': 20},
    {'Category': 'Adult Learning', 'Research & Development': 30, 'Marketing': 20, 'Manufacturing': 25, 'Sales': 25}
]

df = pd.DataFrame(data)
df.set_index('Category', inplace=True)

df_percentage = df.div(df.sum(axis=1), axis=0) * 100

fig, ax = plt.subplots(figsize=(10, 14))

bar_width = 0.5
categories = df_percentage.index
colors = ['#FF6347', '#1E90FF', '#3CB371', '#FFD700']

bottom = [0] * len(df_percentage)

for i, col in enumerate(df.columns):
    ax.bar(categories, df_percentage[col], bar_width, label=col, color=colors[i], bottom=bottom)
    bottom = bottom + df_percentage[col].values

ax.set_ylabel('Percentage')
ax.set_xlabel('Education Category')
ax.set_title('Percentage Allocation of Educational Resources by Category', pad=20)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1)

for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy()
    if height > 0:
        ax.text(x + width / 2,
                y + height / 2,
                f"{height:.1f}%",
                ha='center',
                va='center')

plt.tight_layout()
plt.show()