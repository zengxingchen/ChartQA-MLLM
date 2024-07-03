
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Category": ["Urban"]*4 + ["Suburban"]*4 + ["Rural"]*4 + ["Coastal"]*4,
    "Item": ["Museums", "Parks", "Theaters", "Restaurants"]*4,
    "Percentage": [30, 25, 20, 25, 15, 35, 20, 30, 20, 40, 10, 30, 25, 30, 25, 20]
}
df = pd.DataFrame(data)

df_pivot = df.pivot("Category", "Item", "Percentage")
df_pivot_normalized = df_pivot.div(df_pivot.sum(axis=1), axis=0)

colors = ["#4c72b0", "#55a868", "#c44e52", "#8172b2"]

f, ax = plt.subplots(figsize=(10, 8))

bar_sections = []
prev_values = np.zeros(len(df_pivot_normalized))

for i, col in enumerate(df_pivot_normalized.columns):
    values = df_pivot_normalized[col]
    bar_section = plt.bar(df_pivot_normalized.index, values, bottom=prev_values, 
                          color=colors[i], edgecolor='white', width=0.5)
    bar_sections.append(bar_section)
    prev_values += values

ax.legend(bar_sections, df_pivot_normalized.columns, loc="upper left", title="Leisure Activities")
ax.set(ylim=(0, 1), xlabel="Region", ylabel="Percentage of Leisure Time Allocation")

for bar in bar_sections:
    for rect in bar:
        height = rect.get_height()
        y_value = rect.get_y() + height / 2
        label = f"{height:.0%}"
        plt.text(rect.get_x() + rect.get_width() / 2, y_value, label, va='center', ha='center', color='black')

plt.title('Leisure Time Allocation by Region', pad=20)

sns.despine(left=True, bottom=True)

plt.show()