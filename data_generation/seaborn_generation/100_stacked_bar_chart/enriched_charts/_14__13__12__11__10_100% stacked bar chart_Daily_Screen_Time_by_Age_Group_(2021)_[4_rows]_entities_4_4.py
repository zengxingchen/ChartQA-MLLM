
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Category': 'Environment', 'Early Stage': 10, 'Middle Stage': 20, 'Late Stage': 30, 'Advanced Stage': 25, 'Post Career': 15},
    {'Category': 'Art', 'Early Stage': 20, 'Middle Stage': 15, 'Late Stage': 25, 'Advanced Stage': 20, 'Post Career': 20},
    {'Category': 'Music', 'Early Stage': 15, 'Middle Stage': 25, 'Late Stage': 20, 'Advanced Stage': 25, 'Post Career': 15},
    {'Category': 'Business', 'Early Stage': 30, 'Middle Stage': 20, 'Late Stage': 15, 'Advanced Stage': 25, 'Post Career': 10},
    {'Category': 'Science', 'Early Stage': 25, 'Middle Stage': 20, 'Late Stage': 20, 'Advanced Stage': 15, 'Post Career': 20}
]

df = pd.DataFrame(data)
df.set_index('Category', inplace=True)

df_percentage = df.div(df.sum(axis=1), axis=0) * 100

fig, ax = plt.subplots(figsize=(12, 10))

bar_width = 0.8
categories = df_percentage.index
colors = ['#3498db', '#2ecc71', '#e74c3c', '#f1c40f', '#9b59b6']

bottom = [0] * len(df_percentage.index)

for i, col in enumerate(df.columns):
    ax.bar(categories, df_percentage[col], bar_width, label=col, color=colors[i], bottom=bottom)
    bottom = bottom + df_percentage[col].values

ax.set_ylabel('Percentage')
ax.set_xlabel('Category')
ax.set_title('Distribution of Interest by Career Stage', pad=20)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), ncol=1)

for p in ax.patches:
    height = p.get_height()
    x, y = p.get_x(), p.get_y()
    if height > 0:
        ax.text(x + p.get_width() / 2,
                y + height / 2,
                f"{height:.1f}%",
                ha='center',
                va='center')

plt.tight_layout()
plt.show()