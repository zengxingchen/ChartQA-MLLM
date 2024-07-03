
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {
    'Department': ['Engineering', 'Design', 'Marketing', 'Sales', 'HR', 'R&D', 'IT', 'Finance', 'Operations', 'Legal'],
    'AI Research': [30, 10, 15, 20, 25, 35, 20, 15, 10, 5],
    'Quantum Computing': [25, 10, 10, 15, 20, 30, 20, 10, 15, 10],
    'Robotics': [20, 30, 25, 10, 15, 20, 30, 20, 25, 20],
    'Blockchain': [15, 20, 30, 25, 10, 10, 15, 25, 30, 25],
    'IoT': [10, 30, 20, 30, 30, 5, 15, 30, 20, 40]
}

df = pd.DataFrame(data)

df_percentage = df.drop('Department', axis=1).div(df.drop('Department', axis=1).sum(axis=1), axis=0) * 100

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#F3FF33']

fig, ax = plt.subplots(figsize=(12, 10))

bar_width = 0.8

departments = df['Department']
indices = np.arange(len(departments))

previous_values = np.zeros(len(df))
for col, color in zip(df_percentage.columns, colors):
    values = df_percentage[col]
    ax.bar(indices, values, color=color, edgecolor='white', width=bar_width, bottom=previous_values, label=col)
    previous_values += values

ax.set_ylabel('Percentage of Weekly Time Spent (%)', fontsize=12)
ax.set_title('Time Spent on Different Future Technology Research Areas in Various Departments', fontsize=16, pad=20)
ax.set_xticks(indices)
ax.set_xticklabels(departments, rotation=45, ha="right")
ax.set_ylim(0, 100)
ax.legend(title='Research Areas', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()