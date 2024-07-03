import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = [
    {'Room': 'Breakfast', 'Protein (%)': 20, 'Carbohydrates (%)': 60, 'Fats (%)': 10, 'Vitamins (%)': 7, 'Minerals (%)': 3},
    {'Room': 'Lunch', 'Protein (%)': 18, 'Carbohydrates (%)': 52, 'Fats (%)': 20, 'Vitamins (%)': 7, 'Minerals (%)': 3},
    {'Room': 'Dinner', 'Protein (%)': 22, 'Carbohydrates (%)': 50, 'Fats (%)': 18, 'Vitamins (%)': 7, 'Minerals (%)': 3},
    {'Room': 'Snacks', 'Protein (%)': 15, 'Carbohydrates (%)': 40, 'Fats (%)': 30, 'Vitamins (%)': 10, 'Minerals (%)': 5},
    {'Room': 'Supper', 'Protein (%)': 25, 'Carbohydrates (%)': 45, 'Fats (%)': 20, 'Vitamins (%)': 5, 'Minerals (%)': 5}
]

df = pd.DataFrame(data)
df.set_index('Room', inplace=True)

df_percentage = df.div(df.sum(axis=1), axis=0) * 100

plt.figure(figsize=(10, 8))

bottom = np.zeros(len(df))

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#FFD700']

for i, col in enumerate(df.columns):
    plt.bar(df_percentage.index, df_percentage[col], bottom=bottom, label=col, color=colors[i], width=0.6)
    bottom += df_percentage[col]

plt.xlabel('Meals')
plt.ylabel('Percentage')
plt.title('Nutritional Breakdown by Meal (100% Stacked)', pad=30)
plt.legend(title='Nutrients', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()