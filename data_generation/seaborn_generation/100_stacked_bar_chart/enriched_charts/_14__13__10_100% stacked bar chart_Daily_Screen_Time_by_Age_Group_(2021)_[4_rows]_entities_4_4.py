
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Age Group': '0-8', 'Cardio': 10, 'Strength Training': 20, 'Yoga': 5, 'Other': 65},
    {'Age Group': '9-18', 'Cardio': 15, 'Strength Training': 25, 'Yoga': 10, 'Other': 50},
    {'Age Group': '19-34', 'Cardio': 20, 'Strength Training': 30, 'Yoga': 15, 'Other': 35},
    {'Age Group': '35-50', 'Cardio': 25, 'Strength Training': 20, 'Yoga': 20, 'Other': 35},
    {'Age Group': '51-65', 'Cardio': 30, 'Strength Training': 15, 'Yoga': 25, 'Other': 30},
    {'Age Group': '66+', 'Cardio': 35, 'Strength Training': 10, 'Yoga': 30, 'Other': 25}
]

df = pd.DataFrame(data)
df.set_index('Age Group', inplace=True)

df_percentage = df.div(df.sum(axis=1), axis=0) * 100

fig, ax = plt.subplots(figsize=(12, 8))

bar_height = 0.6
categories = df_percentage.index
colors = ['#3498db', '#e74c3c', '#2ecc71', '#9b59b6']

left = [0] * len(df_percentage)

for i, col in enumerate(df.columns):
    ax.barh(categories, df_percentage[col], bar_height, label=col, color=colors[i], left=left)
    left = left + df_percentage[col].values

ax.set_xlabel('Percentage')
ax.set_title('Percentage of Different Types of Physical Activities by Age Group')
ax.legend(loc='lower right', bbox_to_anchor=(1, 0))

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