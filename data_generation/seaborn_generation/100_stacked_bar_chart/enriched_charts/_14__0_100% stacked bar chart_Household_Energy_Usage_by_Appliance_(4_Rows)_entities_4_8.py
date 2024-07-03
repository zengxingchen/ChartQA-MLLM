
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Day": ["Monday"]*5 + ["Tuesday"]*5 + ["Wednesday"]*5 + ["Thursday"]*5 + ["Friday"]*5,
    "Exercise": ["Running", "Swimming", "Cycling", "Weightlifting", "Yoga"]*5,
    "Minutes": [30, 15, 10, 25, 20, 20, 25, 30, 10, 15, 25, 20, 15, 30, 10, 15, 30, 25, 20, 10, 20, 10, 30, 15, 25]
}
df = pd.DataFrame(data)

df_pivot = df.pivot("Day", "Exercise", "Minutes")

df_pivot_normalized = df_pivot.div(df_pivot.sum(axis=1), axis=0)

colors = ["#FF6347", "#4682B4", "#32CD32", "#FFD700", "#8A2BE2"]

f, ax = plt.subplots(figsize=(8, 10))

bar_sections = []
prev_values = np.zeros(len(df_pivot_normalized))

for i, col in enumerate(df_pivot_normalized.columns):
    values = df_pivot_normalized[col]
    bar_section = plt.bar(df_pivot_normalized.index, values, bottom=prev_values, 
                          color=colors[i], edgecolor='white', width=0.6)
    bar_sections.append(bar_section)
    prev_values += values

ax.legend(bar_sections, df_pivot_normalized.columns, loc="upper right", title="Exercises")
ax.set(ylim=(0, 1), xlabel="Day", ylabel="Percentage of Time Spent")

for bar in bar_sections:
    for rect in bar:
        height = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2
        label = f"{height:.0%}"
        plt.text(x_value, rect.get_y() + height/2, label, ha='center', va='center', color='black')

plt.title('Weekly Exercise Distribution', pad=20)
sns.despine(left=True, bottom=True)

plt.show()