
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Month': 'January', 'Domestic Travel': '20%', 'International Travel': '35%', 'Adventure Travel': '45%'},
    {'Month': 'February', 'Domestic Travel': '25%', 'International Travel': '30%', 'Adventure Travel': '45%'},
    {'Month': 'March', 'Domestic Travel': '22%', 'International Travel': '33%', 'Adventure Travel': '45%'},
    {'Month': 'April', 'Domestic Travel': '18%', 'International Travel': '40%', 'Adventure Travel': '42%'},
    {'Month': 'May', 'Domestic Travel': '30%', 'International Travel': '25%', 'Adventure Travel': '45%'},
    {'Month': 'June', 'Domestic Travel': '28%', 'International Travel': '30%', 'Adventure Travel': '42%'},
    {'Month': 'July', 'Domestic Travel': '25%', 'International Travel': '35%', 'Adventure Travel': '40%'},
    {'Month': 'August', 'Domestic Travel': '27%', 'International Travel': '33%', 'Adventure Travel': '40%'}
]

df = pd.DataFrame(data)
for col in df.columns[1:]:
    df[col] = df[col].str.rstrip('%').astype('float') / 100

df_long = df.melt(id_vars='Month', var_name='Travel Type', value_name='Percentage')

pivot_df = df_long.pivot(index='Month', columns='Travel Type', values='Percentage')

colors = ['#FFA07A', '#20B2AA', '#778899']
pivot_df.plot(kind='bar', stacked=True, color=colors, figsize=(10, 12), width=0.6)

plt.title('Monthly Distribution of Travel Types', pad=20)
plt.xlabel('Month', labelpad=15)
plt.ylabel('Percentage', labelpad=15)
plt.legend(title='Travel Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()