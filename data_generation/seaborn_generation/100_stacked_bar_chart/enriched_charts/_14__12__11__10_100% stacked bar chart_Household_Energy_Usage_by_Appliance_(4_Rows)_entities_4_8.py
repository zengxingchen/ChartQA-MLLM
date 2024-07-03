
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = [
    {'Sport': 'Soccer', 'Training Sessions': 25, 'Hours Practiced': 45, 'Competitions Won': 8, 'Injuries Sustained': 2, 'Attendance': 85},
    {'Sport': 'Basketball', 'Training Sessions': 22, 'Hours Practiced': 38, 'Competitions Won': 10, 'Injuries Sustained': 1, 'Attendance': 90},
    {'Sport': 'Tennis', 'Training Sessions': 20, 'Hours Practiced': 40, 'Competitions Won': 7, 'Injuries Sustained': 1, 'Attendance': 88},
    {'Sport': 'Swimming', 'Training Sessions': 18, 'Hours Practiced': 42, 'Competitions Won': 5, 'Injuries Sustained': 0, 'Attendance': 92},
    {'Sport': 'Running', 'Training Sessions': 30, 'Hours Practiced': 50, 'Competitions Won': 12, 'Injuries Sustained': 0, 'Attendance': 80}
]

df = pd.DataFrame(data)
df.set_index('Sport', inplace=True)

df_percentage = df.div(df.sum(axis=1), axis=0) * 100

plt.figure(figsize=(10, 12))

bottom = np.zeros(len(df))

colors = ['#4CAF50', '#FFC107', '#2196F3', '#FF5722', '#9C27B0']

for i, col in enumerate(df.columns):
    plt.bar(df_percentage.index, df_percentage[col], bottom=bottom, label=col, color=colors[i], width=0.5)
    bottom += df_percentage[col]

plt.xlabel('Sports')
plt.ylabel('Percentage')
plt.title('Sports Training and Performance Breakdown (100% Stacked)', pad=20)
plt.legend(title='Metrics', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()