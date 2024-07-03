
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = [
    {'Year': 2019, 'Design Elements (%)': 25, 'Typography (%)': 35, 'Imagery (%)': 25, 'Color Usage (%)': 15},
    {'Year': 2020, 'Design Elements (%)': 28, 'Typography (%)': 32, 'Imagery (%)': 26, 'Color Usage (%)': 14},
    {'Year': 2021, 'Design Elements (%)': 30, 'Typography (%)': 30, 'Imagery (%)': 25, 'Color Usage (%)': 15},
    {'Year': 2022, 'Design Elements (%)': 27, 'Typography (%)': 33, 'Imagery (%)': 28, 'Color Usage (%)': 12},
    {'Year': 2023, 'Design Elements (%)': 26, 'Typography (%)': 34, 'Imagery (%)': 27, 'Color Usage (%)': 13}
]
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

df_percent = df.div(df.sum(axis=1), axis=0)

ax = df_percent.plot(kind='bar', stacked=True, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], figsize=(10, 8), width=0.6)

plt.title('Design Trends in Digital Media Over Years (Percentage Stacked)', pad=20)
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

plt.legend(title='Design Elements', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()