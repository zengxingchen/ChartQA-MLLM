import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Season': ['Spring', 'Summer', 'Autumn', 'Winter'],
    'Sales': [1200, 2500, 1800, 1500]
}
df = pd.DataFrame(data)

df['Season'] = pd.Categorical(df['Season'], categories=data['Season'], ordered=True)

sns.set_theme()

plt.figure(figsize=(12, 6))
area_chart = sns.lineplot(data=df, x='Season', y='Sales', sort=False, color='#1f77b4')
area_chart.fill_between(df['Season'], df['Sales'], alpha=0.4, color='#aec7e8')

plt.text(x='Summer', y=2500, s='Highest Sales (2500)', color='red', va='bottom', ha='center')

plt.title('Seasonal Sales Data', fontsize=16)
plt.xlabel('Season')
plt.ylabel('Sales')

plt.tight_layout()
plt.show()