
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = [
    {'Room': 'Breakfast', 'Protein (%)': 30, 'Carbohydrates (%)': 50, 'Fats (%)': 10, 'Vitamins (%)': 5, 'Minerals (%)': 5},
    {'Room': 'Lunch', 'Protein (%)': 25, 'Carbohydrates (%)': 45, 'Fats (%)': 15, 'Vitamins (%)': 10, 'Minerals (%)': 5},
    {'Room': 'Dinner', 'Protein (%)': 20, 'Carbohydrates (%)': 40, 'Fats (%)': 20, 'Vitamins (%)': 15, 'Minerals (%)': 5},
    {'Room': 'Snacks', 'Protein (%)': 10, 'Carbohydrates (%)': 30, 'Fats (%)': 30, 'Vitamins (%)': 20, 'Minerals (%)': 10}
]

df = pd.DataFrame(data)
df.set_index('Room', inplace=True)

df_percentage = df.div(df.sum(axis=1), axis=0) * 100

plt.figure(figsize=(10, 8))

bottom = np.zeros(len(df))

colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2']

for i, col in enumerate(df.columns):
    plt.bar(df_percentage.index, df_percentage[col], bottom=bottom, label=col, color=colors[i], width=0.7)
    bottom += df_percentage[col]

plt.xlabel('Meals')
plt.ylabel('Percentage')
plt.title('Meal Nutritional Breakdown (100% Stacked)', pad=20)
plt.legend(title='Nutrients', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()