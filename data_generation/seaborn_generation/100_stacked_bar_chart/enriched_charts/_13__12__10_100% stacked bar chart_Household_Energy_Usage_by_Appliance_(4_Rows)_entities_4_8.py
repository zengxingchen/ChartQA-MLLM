
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = [
    {'Room': 'Breakfast', 'Protein (%)': 25, 'Carbohydrates (%)': 55, 'Fats (%)': 8, 'Vitamins (%)': 7, 'Minerals (%)': 5},
    {'Room': 'Lunch', 'Protein (%)': 20, 'Carbohydrates (%)': 50, 'Fats (%)': 15, 'Vitamins (%)': 10, 'Minerals (%)': 5},
    {'Room': 'Dinner', 'Protein (%)': 15, 'Carbohydrates (%)': 45, 'Fats (%)': 25, 'Vitamins (%)': 10, 'Minerals (%)': 5},
    {'Room': 'Snacks', 'Protein (%)': 12, 'Carbohydrates (%)': 35, 'Fats (%)': 30, 'Vitamins (%)': 15, 'Minerals (%)': 8}
]

df = pd.DataFrame(data)
df.set_index('Room', inplace=True)

df_percentage = df.div(df.sum(axis=1), axis=0) * 100

plt.figure(figsize=(8, 12))

bottom = np.zeros(len(df))

colors = ['#1E90FF', '#FF4500', '#32CD32', '#FFD700', '#8A2BE2']

for i, col in enumerate(df.columns):
    plt.bar(df_percentage.index, df_percentage[col], bottom=bottom, label=col, color=colors[i], width=0.5)
    bottom += df_percentage[col]

plt.xlabel('Meals')
plt.ylabel('Percentage')
plt.title('Nutritional Breakdown by Meal (100% Stacked)', pad=20)
plt.legend(title='Nutrients', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()