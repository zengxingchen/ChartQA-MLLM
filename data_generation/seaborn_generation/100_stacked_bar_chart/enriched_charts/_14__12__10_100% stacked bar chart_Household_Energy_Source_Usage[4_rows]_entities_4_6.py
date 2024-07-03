
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = [
    {'Year': 2019, 'Exercise (%)': 40, 'Meditation (%)': 15, 'Diet (%)': 25, 'Sleep (%)': 20},
    {'Year': 2020, 'Exercise (%)': 42, 'Meditation (%)': 18, 'Diet (%)': 22, 'Sleep (%)': 18},
    {'Year': 2021, 'Exercise (%)': 45, 'Meditation (%)': 20, 'Diet (%)': 20, 'Sleep (%)': 15},
    {'Year': 2022, 'Exercise (%)': 48, 'Meditation (%)': 22, 'Diet (%)': 18, 'Sleep (%)': 12}
]

df = pd.DataFrame(data)
df.set_index('Year', inplace=True)
df_percent = df.div(df.sum(axis=1), axis=0)

ax = df_percent.plot(kind='bar', stacked=True, color=['#8E44AD', '#2980B9', '#27AE60', '#F39C12'], figsize=(12, 8), width=0.75)

plt.title('Participation in Health Activities Over Years (Percentage Stacked)', pad=20)
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

plt.legend(title='Health Activities', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()