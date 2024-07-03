
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Age Group': '0-8', 'Reading': 10, 'Writing': 10, 'Studying': 40, 'Resting': 40},
    {'Age Group': '9-18', 'Reading': 15, 'Writing': 15, 'Studying': 35, 'Resting': 35},
    {'Age Group': '19-34', 'Reading': 20, 'Writing': 25, 'Studying': 30, 'Resting': 25},
    {'Age Group': '35-50', 'Reading': 25, 'Writing': 20, 'Studying': 25, 'Resting': 30},
    {'Age Group': '51-65', 'Reading': 20, 'Writing': 20, 'Studying': 30, 'Resting': 30},
    {'Age Group': '66+', 'Reading': 15, 'Writing': 15, 'Studying': 35, 'Resting': 35}
]

df = pd.DataFrame(data)
df.set_index('Age Group', inplace=True)

df_percentage = df.div(df.sum(axis=1), axis=0) * 100

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.7
categories = df_percentage.index
colors = ['#4daf4a', '#377eb8', '#ff7f00', '#984ea3']

bottom = [0] * len(df_percentage)

for i, col in enumerate(df.columns):
    ax.bar(categories, df_percentage[col], bar_width, label=col, color=colors[i], bottom=bottom)
    bottom = bottom + df_percentage[col].values

ax.set_ylabel('Percentage')
ax.set_xlabel('Age Group')
ax.set_title('Percentage of Time Spent on Educational Activities by Age Group', pad=20)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

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