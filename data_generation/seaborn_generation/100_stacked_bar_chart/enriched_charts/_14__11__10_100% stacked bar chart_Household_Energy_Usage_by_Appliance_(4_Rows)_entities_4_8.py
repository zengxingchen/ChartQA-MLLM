
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = [
    {'Category': 'Fruits', 'Calories (kcal)': 200, 'Protein (g)': 3, 'Fat (g)': 1, 'Carbohydrates (g)': 50, 'Fiber (g)': 7},
    {'Category': 'Vegetables', 'Calories (kcal)': 150, 'Protein (g)': 5, 'Fat (g)': 1, 'Carbohydrates (g)': 30, 'Fiber (g)': 10},
    {'Category': 'Grains', 'Calories (kcal)': 300, 'Protein (g)': 8, 'Fat (g)': 4, 'Carbohydrates (g)': 60, 'Fiber (g)': 5},
    {'Category': 'Dairy', 'Calories (kcal)': 250, 'Protein (g)': 12, 'Fat (g)': 10, 'Carbohydrates (g)': 20, 'Fiber (g)': 0},
    {'Category': 'Meat', 'Calories (kcal)': 350, 'Protein (g)': 25, 'Fat (g)': 15, 'Carbohydrates (g)': 0, 'Fiber (g)': 0}
]

df = pd.DataFrame(data)
df.set_index('Category', inplace=True)

df_percentage = df.div(df.sum(axis=1), axis=0) * 100

plt.figure(figsize=(12, 10))

bottom = np.zeros(len(df))

colors = ['#FF5733', '#33FFBD', '#337BFF', '#FF33A1', '#A133FF']

for i, col in enumerate(df.columns):
    plt.bar(df_percentage.index, df_percentage[col], bottom=bottom, label=col, color=colors[i], width=0.6)
    bottom += df_percentage[col]

plt.xlabel('Category')
plt.ylabel('Percentage')
plt.title('Nutritional Composition Breakdown (100% Stacked)', pad=20)
plt.legend(title='Nutritional Metrics', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()