
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = [
    {'Food': 'Apple', 'Proteins (%)': 2, 'Fats (%)': 1, 'Carbohydrates (%)': 12, 'Fiber (%)': 2, 'Vitamins (%)': 83},
    {'Food': 'Beef', 'Proteins (%)': 26, 'Fats (%)': 20, 'Carbohydrates (%)': 0, 'Fiber (%)': 0, 'Vitamins (%)': 54},
    {'Food': 'Bread', 'Proteins (%)': 9, 'Fats (%)': 4, 'Carbohydrates (%)': 50, 'Fiber (%)': 3, 'Vitamins (%)': 34},
    {'Food': 'Cheese', 'Proteins (%)': 25, 'Fats (%)': 33, 'Carbohydrates (%)': 1, 'Fiber (%)': 0, 'Vitamins (%)': 41},
    {'Food': 'Broccoli', 'Proteins (%)': 3, 'Fats (%)': 0, 'Carbohydrates (%)': 7, 'Fiber (%)': 2, 'Vitamins (%)': 88}
]

df = pd.DataFrame(data)
df.set_index('Food', inplace=True)

df_percentage = df.div(df.sum(axis=1), axis=0) * 100

plt.figure(figsize=(10, 6))

bottom = np.zeros(len(df))

colors = ['#FF5733', '#33FFBD', '#337BFF', '#FF33A8', '#DAFF33']

for i, col in enumerate(df.columns):
    plt.bar(df_percentage.index, df_percentage[col], bottom=bottom, label=col, color=colors[i], width=0.4)
    bottom += df_percentage[col]

plt.xlabel('Food Items')
plt.ylabel('Percentage')
plt.title('Nutrient Composition in Various Foods (100% Stacked Bar)', pad=20)
plt.legend(title='Nutrients', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()