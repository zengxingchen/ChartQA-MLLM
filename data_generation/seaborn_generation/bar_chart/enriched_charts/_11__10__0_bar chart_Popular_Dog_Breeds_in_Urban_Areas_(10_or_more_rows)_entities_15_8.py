
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Location': ['City A', 'City B', 'City C', 'City D', 'City E'],
    'Health Care': [15000, 18000, 16000, 17000, 19000],
    'Technology': [24000, 26000, 25000, 27000, 28000],
    'Environment': [22000, 23000, 24000, 21000, 25000],
    'Arts & Culture': [17000, 19000, 20000, 18000, 21000],
    'Education': [28000, 31000, 29000, 30000, 32000]
}

df = pd.DataFrame(data)
df_long = pd.melt(df, id_vars='Location', var_name='Category', value_name='Investment')

plt.figure(figsize=(14, 10))
sns.barplot(
    y='Category', 
    x='Investment', 
    hue='Location', 
    data=df_long,
    palette=['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2'],
    dodge=True,
    edgecolor='.2',
    linewidth=.6,
    orient='h'
)

plt.yticks(rotation=0)
plt.legend(title='City', loc='lower right')
plt.title('Investment in Various Sectors by City', pad=20)
plt.xlabel('Total Investment')
plt.ylabel('Sector')

plt.show()