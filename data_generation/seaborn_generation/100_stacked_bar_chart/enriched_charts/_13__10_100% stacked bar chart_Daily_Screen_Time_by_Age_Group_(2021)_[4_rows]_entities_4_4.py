
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Age Group': '0-8', 'Fruits': 18, 'Vegetables': 22, 'Grains': 35, 'Protein': 25},
    {'Age Group': '9-18', 'Fruits': 20, 'Vegetables': 30, 'Grains': 25, 'Protein': 25},
    {'Age Group': '19-34', 'Fruits': 15, 'Vegetables': 25, 'Grains': 35, 'Protein': 25},
    {'Age Group': '35-50', 'Fruits': 22, 'Vegetables': 18, 'Grains': 30, 'Protein': 30},
    {'Age Group': '51-65', 'Fruits': 28, 'Vegetables': 15, 'Grains': 30, 'Protein': 27},
    {'Age Group': '66+', 'Fruits': 24, 'Vegetables': 20, 'Grains': 32, 'Protein': 24}
]

df = pd.DataFrame(data)
df.set_index('Age Group', inplace=True)

df_percentage = df.div(df.sum(axis=1), axis=0) * 100

fig, ax = plt.subplots(figsize=(10, 10))

bar_width = 0.6
categories = df_percentage.index
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9']

bottom = [0] * len(df_percentage)

for i, col in enumerate(df.columns):
    ax.bar(categories, df_percentage[col], bar_width, label=col, color=colors[i], bottom=bottom)
    bottom = bottom + df_percentage[col].values

ax.set_ylabel('Percentage')
ax.set_title('Percentage of Macronutrient Consumption by Age Group')
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