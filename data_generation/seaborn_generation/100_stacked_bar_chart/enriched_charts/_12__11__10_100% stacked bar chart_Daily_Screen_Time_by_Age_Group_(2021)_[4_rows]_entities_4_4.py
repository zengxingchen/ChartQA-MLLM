
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Age Group': 'Early Career', 'Research': 20, 'Teaching': 30, 'Administration': 35, 'Outreach': 15},
    {'Age Group': 'Mid Career', 'Research': 25, 'Teaching': 25, 'Administration': 30, 'Outreach': 20},
    {'Age Group': 'Late Career', 'Research': 30, 'Teaching': 20, 'Administration': 25, 'Outreach': 25},
    {'Age Group': 'Senior Career', 'Research': 35, 'Teaching': 15, 'Administration': 20, 'Outreach': 30},
    {'Age Group': 'Retired', 'Research': 10, 'Teaching': 10, 'Administration': 20, 'Outreach': 60}
]

df = pd.DataFrame(data)
df.set_index('Age Group', inplace=True)

df_percentage = df.div(df.sum(axis=1), axis=0) * 100

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.7
categories = df_percentage.index
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

bottom = [0] * len(df_percentage)

for i, col in enumerate(df.columns):
    ax.bar(categories, df_percentage[col], bar_width, label=col, color=colors[i], bottom=bottom)
    bottom = bottom + df_percentage[col].values

ax.set_ylabel('Percentage')
ax.set_xlabel('Age Group')
ax.set_title('Percentage of Time Spent on Academic Activities by Career Stage', pad=20)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=4)

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