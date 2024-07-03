
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = [
    {'Room': 'Breakfast', 'Calories (%)': 40, 'Protein (%)': 25, 'Fat (%)': 15, 'Carbs (%)': 10, 'Fiber (%)': 10},
    {'Room': 'Lunch', 'Calories (%)': 35, 'Protein (%)': 20, 'Fat (%)': 25, 'Carbs (%)': 10, 'Fiber (%)': 10},
    {'Room': 'Dinner', 'Calories (%)': 30, 'Protein (%)': 15, 'Fat (%)': 20, 'Carbs (%)': 25, 'Fiber (%)': 10},
    {'Room': 'Snacks', 'Calories (%)': 20, 'Protein (%)': 10, 'Fat (%)': 30, 'Carbs (%)': 30, 'Fiber (%)': 10}
]

df = pd.DataFrame(data)
df.set_index('Room', inplace=True)

df_percentage = df.div(df.sum(axis=1), axis=0) * 100

plt.figure(figsize=(12, 10))

bottom = np.zeros(len(df))

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

for i, col in enumerate(df.columns):
    plt.bar(df_percentage.index, df_percentage[col], bottom=bottom, label=col, color=colors[i], width=0.5)
    bottom += df_percentage[col]

plt.xlabel('Meals')
plt.ylabel('Percentage')
plt.title('Meal Component Breakdown by Percentage', pad=30)
plt.legend(title='Nutrients', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()