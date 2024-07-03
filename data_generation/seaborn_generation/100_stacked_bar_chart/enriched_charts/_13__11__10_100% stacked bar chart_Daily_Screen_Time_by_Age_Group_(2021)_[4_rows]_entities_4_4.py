
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Category': 'Electronics', 'Research & Development': 20, 'Marketing': 25, 'Manufacturing': 30, 'Sales': 25},
    {'Category': 'Automobile', 'Research & Development': 35, 'Marketing': 15, 'Manufacturing': 40, 'Sales': 10},
    {'Category': 'Pharmaceutical', 'Research & Development': 25, 'Marketing': 20, 'Manufacturing': 35, 'Sales': 20},
    {'Category': 'Textiles', 'Research & Development': 15, 'Marketing': 30, 'Manufacturing': 35, 'Sales': 20},
    {'Category': 'Food & Beverages', 'Research & Development': 10, 'Marketing': 30, 'Manufacturing': 40, 'Sales': 20},
    {'Category': 'Technology', 'Research & Development': 30, 'Marketing': 20, 'Manufacturing': 25, 'Sales': 25}
]

df = pd.DataFrame(data)
df.set_index('Category', inplace=True)

df_percentage = df.div(df.sum(axis=1), axis=0) * 100

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.75
categories = df_percentage.index
colors = ['#4B0082', '#FF4500', '#4682B4', '#32CD32']

bottom = [0] * len(df_percentage)

for i, col in enumerate(df.columns):
    ax.bar(categories, df_percentage[col], bar_width, label=col, color=colors[i], bottom=bottom)
    bottom = bottom + df_percentage[col].values

ax.set_ylabel('Percentage')
ax.set_xlabel('Business Category')
ax.set_title('Percentage Allocation of Company Resources by Business Category', pad=20)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=2)

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