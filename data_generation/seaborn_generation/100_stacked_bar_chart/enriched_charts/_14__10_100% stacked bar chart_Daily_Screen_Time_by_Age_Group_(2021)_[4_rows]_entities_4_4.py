
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Age Group': '0-8', 'Exercise': 10, 'Healthy Diet': 50, 'Stress Management': 30, 'Sleep Quality': 10},
    {'Age Group': '9-18', 'Exercise': 20, 'Healthy Diet': 40, 'Stress Management': 25, 'Sleep Quality': 15},
    {'Age Group': '19-34', 'Exercise': 25, 'Healthy Diet': 35, 'Stress Management': 20, 'Sleep Quality': 20},
    {'Age Group': '35-50', 'Exercise': 20, 'Healthy Diet': 30, 'Stress Management': 30, 'Sleep Quality': 20},
    {'Age Group': '51-65', 'Exercise': 15, 'Healthy Diet': 25, 'Stress Management': 40, 'Sleep Quality': 20},
    {'Age Group': '66+', 'Exercise': 10, 'Healthy Diet': 20, 'Stress Management': 50, 'Sleep Quality': 20}
]

df = pd.DataFrame(data)
df.set_index('Age Group', inplace=True)

df_percentage = df.div(df.sum(axis=1), axis=0) * 100

fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.6
categories = df_percentage.index
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']

bottom = [0] * len(df_percentage)

for i, col in enumerate(df.columns):
    ax.bar(categories, df_percentage[col], bar_width, label=col, color=colors[i], bottom=bottom)
    bottom = bottom + df_percentage[col].values

ax.set_ylabel('Percentage')
ax.set_title('Health and Well-being Practices by Age Group')
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1.0))

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