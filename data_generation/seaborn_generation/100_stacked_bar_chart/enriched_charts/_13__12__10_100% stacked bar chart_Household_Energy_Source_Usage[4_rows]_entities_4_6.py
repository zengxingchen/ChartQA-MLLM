
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = [
    {'Year': 2019, 'Ancient Civilizations (%)': 25, 'Middle Ages (%)': 30, 'Renaissance (%)': 20, 'Modern Era (%)': 25},
    {'Year': 2020, 'Ancient Civilizations (%)': 28, 'Middle Ages (%)': 27, 'Renaissance (%)': 23, 'Modern Era (%)': 22},
    {'Year': 2021, 'Ancient Civilizations (%)': 22, 'Middle Ages (%)': 35, 'Renaissance (%)': 18, 'Modern Era (%)': 25},
    {'Year': 2022, 'Ancient Civilizations (%)': 30, 'Middle Ages (%)': 25, 'Renaissance (%)': 20, 'Modern Era (%)': 25},
    {'Year': 2023, 'Ancient Civilizations (%)': 26, 'Middle Ages (%)': 28, 'Renaissance (%)': 22, 'Modern Era (%)': 24}
]

df = pd.DataFrame(data)
df.set_index('Year', inplace=True)
df_percent = df.div(df.sum(axis=1), axis=0)

ax = df_percent.plot(kind='bar', stacked=True, color=['#8B4513', '#FFD700', '#8A2BE2', '#4682B4'], figsize=(12, 8), width=0.75)

plt.title('Historical Era Distribution Over Years (Percentage Stacked)', pad=20)
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

plt.legend(title='Historical Eras', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()