
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Location': ['City A', 'City B', 'City C', 'City D', 'City E'],
    'Renewable Energy': [22000, 26000, 24000, 21000, 23000],
    'Transportation': [19000, 21000, 23000, 20000, 22000],
    'Infrastructure': [30000, 28000, 29000, 27000, 31000],
    'Innovation': [25000, 27000, 26000, 24000, 28000],
    'Education': [28000, 32000, 31000, 29000, 33000]
}

df = pd.DataFrame(data)
df_long = pd.melt(df, id_vars='Location', var_name='Category', value_name='Investment')

plt.figure(figsize=(10, 14))
sns.barplot(
    x='Category', 
    y='Investment', 
    hue='Location', 
    data=df_long,
    palette=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'],
    dodge=True,
    edgecolor='.2',
    linewidth=.6,
    orient='v'
)

plt.xticks(rotation=45)
plt.legend(title='City')
plt.title('Investment in Various Sectors by City')
plt.xlabel('Sector')
plt.ylabel('Total Investment')

plt.show()