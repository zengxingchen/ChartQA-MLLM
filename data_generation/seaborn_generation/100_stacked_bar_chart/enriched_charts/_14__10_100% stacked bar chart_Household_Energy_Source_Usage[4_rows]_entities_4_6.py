
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = [
    {'Year': 2019, 'Running (%)': 25, 'Cycling (%)': 35, 'Swimming (%)': 20, 'Yoga (%)': 20},
    {'Year': 2020, 'Running (%)': 30, 'Cycling (%)': 30, 'Swimming (%)': 25, 'Yoga (%)': 15},
    {'Year': 2021, 'Running (%)': 35, 'Cycling (%)': 25, 'Swimming (%)': 20, 'Yoga (%)': 20},
    {'Year': 2022, 'Running (%)': 40, 'Cycling (%)': 20, 'Swimming (%)': 25, 'Yoga (%)': 15}
]
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

df_percent = df.div(df.sum(axis=1), axis=0)

ax = df_percent.plot(kind='bar', stacked=True, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], figsize=(10, 7), width=0.65)

plt.title('Sports Activity Distribution Over Years (Percentage Stacked)', pad=20)
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

plt.legend(title='Sports Activities', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()