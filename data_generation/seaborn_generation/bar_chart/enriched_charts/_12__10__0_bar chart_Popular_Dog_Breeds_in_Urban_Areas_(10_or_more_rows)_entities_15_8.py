
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Location': ['Site A', 'Site B', 'Site C', 'Site D', 'Site E'],
    'Exploration': [15000, 17000, 16000, 18000, 19000],
    'Surveying': [18000, 19000, 20000, 21000, 22000],
    'Excavation': [22000, 23000, 24000, 25000, 26000],
    'Preservation': [17000, 19000, 18000, 20000, 21000],
    'Research': [20000, 21000, 22000, 23000, 24000]
}

df = pd.DataFrame(data)
df_long = pd.melt(df, id_vars='Location', var_name='Category', value_name='Investment')

plt.figure(figsize=(14, 10))
sns.barplot(
    y='Category', 
    x='Investment', 
    hue='Location', 
    data=df_long,
    palette=['#4c72b0', '#dd8452', '#55a868', '#c44e52', '#8172b3'],
    dodge=True,
    edgecolor='.3',
    linewidth=.8,
    orient='h'
)

plt.yticks(rotation=0)
plt.legend(title='Archaeological Site', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.title('Investment in Archaeological Activities by Site', fontsize=14, pad=20)
plt.xlabel('Total Investment (in USD)')
plt.ylabel('Activity Category')

plt.tight_layout()
plt.show()