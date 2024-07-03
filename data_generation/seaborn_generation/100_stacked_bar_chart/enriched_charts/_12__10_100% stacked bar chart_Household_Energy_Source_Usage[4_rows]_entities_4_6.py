
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = [
    {'Year': 2019, 'Fruits & Vegetables (%)': 30, 'Grains (%)': 25, 'Proteins (%)': 35, 'Dairy (%)': 10},
    {'Year': 2020, 'Fruits & Vegetables (%)': 32, 'Grains (%)': 22, 'Proteins (%)': 36, 'Dairy (%)': 10},
    {'Year': 2021, 'Fruits & Vegetables (%)': 35, 'Grains (%)': 20, 'Proteins (%)': 33, 'Dairy (%)': 12},
    {'Year': 2022, 'Fruits & Vegetables (%)': 37, 'Grains (%)': 18, 'Proteins (%)': 32, 'Dairy (%)': 13}
]

df = pd.DataFrame(data)
df.set_index('Year', inplace=True)
df_percent = df.div(df.sum(axis=1), axis=0)

ax = df_percent.plot(kind='bar', stacked=True, color=['#4CAF50', '#FFC107', '#FF5722', '#03A9F4'], figsize=(10, 7), width=0.85)

plt.title('Food Category Distribution Over Years (Percentage Stacked)', pad=20)
plt.xlabel('Year')
plt.ylabel('Percentage %')

for p in ax.patches:
    width = p.get_width()
    height = p.get_height()
    x, y = p.get_xy()
    if height > 0:
        ax.text(x+width/2,
                y+height/2,
                '{:.0%}'.format(height),
                horizontalalignment='center',
                verticalalignment='center')

plt.legend(title='Food Categories', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()