
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Location': ['City A', 'City B', 'City C', 'City D', 'City E'],
    'Entertainment': [14000, 18000, 17000, 19000, 16000],
    'Politics & Governance': [16000, 20000, 22000, 18000, 21000],
    'Education & Learning': [21000, 23000, 24000, 22000, 25000],
    'Music & Performing Arts': [15000, 17000, 16000, 18000, 19000],
    'Health & Psychology': [19000, 21000, 20000, 22000, 23000]
}

df = pd.DataFrame(data)
df_long = pd.melt(df, id_vars='Location', var_name='Category', value_name='Investment')

plt.figure(figsize=(10, 14))
sns.barplot(
    x='Category', 
    y='Investment', 
    hue='Location', 
    data=df_long,
    palette=['#1E90FF', '#FF4500', '#3CB371', '#FFD700', '#BA55D3'],
    dodge=True,
    edgecolor='.2',
    linewidth=.6,
    width=0.6
)

plt.xticks(rotation=45)
plt.legend(title='City', loc='upper right')
plt.title('Investment in Various Sectors by City', pad=20)
plt.ylabel('Total Investment')
plt.xlabel('Sector')

plt.show()