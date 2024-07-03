
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = [
    {'Room': 'Gym', 'Calories Burned (kcal)': 500, 'Workout Duration (min)': 60, 'Hydration (ml)': 750, 'Heart Rate (bpm)': 140, 'Steps Count (steps)': 8000},
    {'Room': 'Park', 'Calories Burned (kcal)': 400, 'Workout Duration (min)': 50, 'Hydration (ml)': 600, 'Heart Rate (bpm)': 130, 'Steps Count (steps)': 7000},
    {'Room': 'Home', 'Calories Burned (kcal)': 300, 'Workout Duration (min)': 40, 'Hydration (ml)': 500, 'Heart Rate (bpm)': 120, 'Steps Count (steps)': 6000},
    {'Room': 'Beach', 'Calories Burned (kcal)': 600, 'Workout Duration (min)': 70, 'Hydration (ml)': 800, 'Heart Rate (bpm)': 150, 'Steps Count (steps)': 9000},
    {'Room': 'Trail', 'Calories Burned (kcal)': 550, 'Workout Duration (min)': 65, 'Hydration (ml)': 700, 'Heart Rate (bpm)': 145, 'Steps Count (steps)': 8500}
]

df = pd.DataFrame(data)
df.set_index('Room', inplace=True)

df_percentage = df.div(df.sum(axis=1), axis=0) * 100

plt.figure(figsize=(10, 8))

bottom = np.zeros(len(df))

colors = ['#FF5733', '#33FFBD', '#337BFF', '#FF33A1', '#A133FF']

for i, col in enumerate(df.columns):
    plt.bar(df_percentage.index, df_percentage[col], bottom=bottom, label=col, color=colors[i], width=0.5)
    bottom += df_percentage[col]

plt.ylabel('Rooms')
plt.xlabel('Percentage')
plt.title('Workout Activity Breakdown (100% Stacked)', pad=20)
plt.legend(title='Metrics', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()