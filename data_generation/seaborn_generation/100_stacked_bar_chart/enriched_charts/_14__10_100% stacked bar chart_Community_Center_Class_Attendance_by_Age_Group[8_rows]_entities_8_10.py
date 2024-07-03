
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Month': 'January', 'Urban Areas': '20%', 'Rural Areas': '35%', 'Suburban Areas': '45%'},
    {'Month': 'February', 'Urban Areas': '25%', 'Rural Areas': '40%', 'Suburban Areas': '35%'},
    {'Month': 'March', 'Urban Areas': '30%', 'Rural Areas': '25%', 'Suburban Areas': '45%'},
    {'Month': 'April', 'Urban Areas': '35%', 'Rural Areas': '30%', 'Suburban Areas': '35%'},
    {'Month': 'May', 'Urban Areas': '22%', 'Rural Areas': '38%', 'Suburban Areas': '40%'},
    {'Month': 'June', 'Urban Areas': '28%', 'Rural Areas': '32%', 'Suburban Areas': '40%'},
    {'Month': 'July', 'Urban Areas': '32%', 'Rural Areas': '33%', 'Suburban Areas': '35%'},
    {'Month': 'August', 'Urban Areas': '34%', 'Rural Areas': '26%', 'Suburban Areas': '40%'},
    {'Month': 'September', 'Urban Areas': '29%', 'Rural Areas': '34%', 'Suburban Areas': '37%'},
    {'Month': 'October', 'Urban Areas': '31%', 'Rural Areas': '29%', 'Suburban Areas': '40%'},
    {'Month': 'November', 'Urban Areas': '33%', 'Rural Areas': '30%', 'Suburban Areas': '37%'},
    {'Month': 'December', 'Urban Areas': '28%', 'Rural Areas': '34%', 'Suburban Areas': '38%'}
]

df = pd.DataFrame(data)
for col in df.columns[1:]:
    df[col] = df[col].str.rstrip('%').astype('float') / 100

df_long = df.melt(id_vars='Month', var_name='Area Type', value_name='Percentage')

pivot_df = df_long.pivot(index='Month', columns='Area Type', values='Percentage')

colors = ['#FF7F50', '#6495ED', '#90EE90']
pivot_df.plot(kind='bar', stacked=True, color=colors, figsize=(10, 6), width=0.7)

plt.title('Monthly Distribution of Population by Area Type in Urban, Rural, and Suburban Areas', pad=20)
plt.xlabel('Month', labelpad=15)
plt.ylabel('Percentage', labelpad=15)
plt.legend(title='Area Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()