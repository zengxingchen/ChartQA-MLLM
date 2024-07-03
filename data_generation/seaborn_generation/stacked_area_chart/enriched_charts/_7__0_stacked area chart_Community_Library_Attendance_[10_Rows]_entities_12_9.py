
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
              'September', 'October', 'November', 'December'],
    'Books': [1200, 1500, 1600, 1700, 1800, 2000, 2100, 2300, 2400, 2500, 2600, 2800],
    'Stationery': [800, 900, 950, 1000, 1100, 1150, 1200, 1250, 1300, 1400, 1500, 1600],
    'Online Courses': [600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1200]
}

df = pd.DataFrame(data)

df_long = pd.melt(df, id_vars='Month', var_name='Category', value_name='Sales')

df_long['Month'] = pd.Categorical(df_long['Month'], 
                                  categories=['January', 'February', 'March', 'April', 'May', 'June', 
                                              'July', 'August', 'September', 'October', 'November', 'December'],
                                  ordered=True)

plt.figure(figsize=(14, 10))

sns.set_theme(style="whitegrid")
pal = ['#377eb8', '#ff7f00', '#4daf4a']

ax = df.set_index('Month').plot(kind='area', stacked=True, color=pal)

df['Total'] = df['Books'] + df['Stationery'] + df['Online Courses']
for idx, total in enumerate(df['Total']):
    ax.text(idx, total, str(total), va='bottom', ha='center')

ax.set_title('Monthly Sales Distribution in Educational Products', fontsize=18)
ax.set_ylabel('Monthly Sales', fontsize=14)
ax.set_xlabel('Month', fontsize=14)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()