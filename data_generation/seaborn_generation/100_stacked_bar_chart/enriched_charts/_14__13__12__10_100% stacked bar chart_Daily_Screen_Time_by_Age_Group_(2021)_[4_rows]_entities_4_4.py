
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Category': 'Art Gallery', 'Classical Music': 30, 'Rock Music': 20, 'Jazz Music': 25, 'Hip-Hop': 25},
    {'Category': 'Concert', 'Classical Music': 15, 'Rock Music': 35, 'Jazz Music': 25, 'Hip-Hop': 25},
    {'Category': 'Radio', 'Classical Music': 25, 'Rock Music': 25, 'Jazz Music': 30, 'Hip-Hop': 20},
    {'Category': 'Online Streaming', 'Classical Music': 20, 'Rock Music': 30, 'Jazz Music': 30, 'Hip-Hop': 20},
    {'Category': 'Night Club', 'Classical Music': 10, 'Rock Music': 25, 'Jazz Music': 20, 'Hip-Hop': 45},
    {'Category': 'Festival', 'Classical Music': 20, 'Rock Music': 25, 'Jazz Music': 30, 'Hip-Hop': 25}
]

df = pd.DataFrame(data)
df.set_index('Category', inplace=True)

df_percentage = df.div(df.sum(axis=1), axis=0) * 100

fig, ax = plt.subplots(figsize=(10, 8))

bar_width = 0.8
categories = df_percentage.index
colors = ['#3498db', '#e74c3c', '#2ecc71', '#9b59b6']

bottom = [0] * len(df_percentage)

for i, col in enumerate(df.columns):
    ax.bar(categories, df_percentage[col], bar_width, label=col, color=colors[i], bottom=bottom)
    bottom = bottom + df_percentage[col].values

ax.set_ylabel('Percentage')
ax.set_title('Music Preferences Across Different Settings')
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))

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