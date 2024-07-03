
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Age Group': '0-8', 'Work': 5, 'Exercise': 15, 'Leisure': 30, 'Sleep': 50},
    {'Age Group': '9-18', 'Work': 15, 'Exercise': 20, 'Leisure': 30, 'Sleep': 35},
    {'Age Group': '19-34', 'Work': 30, 'Exercise': 10, 'Leisure': 30, 'Sleep': 30},
    {'Age Group': '35-50', 'Work': 40, 'Exercise': 10, 'Leisure': 25, 'Sleep': 25},
    {'Age Group': '51-65', 'Work': 25, 'Exercise': 10, 'Leisure': 25, 'Sleep': 40},
    {'Age Group': '66+', 'Work': 10, 'Exercise': 10, 'Leisure': 30, 'Sleep': 50}
]

df = pd.DataFrame(data)
df.set_index('Age Group', inplace=True)

df_percentage = df.div(df.sum(axis=1), axis=0) * 100

fig, ax = plt.subplots(figsize=(10, 12))

bar_width = 0.85
categories = df_percentage.index
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

bottom = [0] * len(df_percentage)

for i, col in enumerate(df.columns):
    ax.bar(categories, df_percentage[col], bar_width, label=col, color=colors[i], bottom=bottom)
    bottom = bottom + df_percentage[col].values

ax.set_ylabel('Percentage')
ax.set_title('Percentage of Time Spent on Activities by Age Group')
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.05))

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