
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = [
    {'Year': 2019, 'Protein (%)': 30, 'Carbohydrates (%)': 40, 'Fats (%)': 20, 'Vitamins (%)': 10},
    {'Year': 2020, 'Protein (%)': 25, 'Carbohydrates (%)': 45, 'Fats (%)': 20, 'Vitamins (%)': 10},
    {'Year': 2021, 'Protein (%)': 35, 'Carbohydrates (%)': 30, 'Fats (%)': 25, 'Vitamins (%)': 10},
    {'Year': 2022, 'Protein (%)': 32, 'Carbohydrates (%)': 38, 'Fats (%)': 20, 'Vitamins (%)': 10},
    {'Year': 2023, 'Protein (%)': 28, 'Carbohydrates (%)': 42, 'Fats (%)': 20, 'Vitamins (%)': 10}
]

df = pd.DataFrame(data)
df.set_index('Year', inplace=True)
df_percent = df.div(df.sum(axis=1), axis=0)

ax = df_percent.plot(kind='bar', stacked=True, color=['#FF6347', '#4682B4', '#FFD700', '#32CD32'], figsize=(10, 6), width=0.6)

plt.title('Nutritional Composition Over Years (Percentage Stacked)', pad=20)
plt.xlabel('Year')
plt.ylabel('Percentage %')

for p in ax.patches:
    width = p.get_width()
    height = p.get_height()
    x, y = p.get_xy()
    if height > 0:
        ax.text(x + width / 2,
                y + height / 2,
                '{:.0%}'.format(height),
                horizontalalignment='center',
                verticalalignment='center')

plt.legend(title='Nutritional Components', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()