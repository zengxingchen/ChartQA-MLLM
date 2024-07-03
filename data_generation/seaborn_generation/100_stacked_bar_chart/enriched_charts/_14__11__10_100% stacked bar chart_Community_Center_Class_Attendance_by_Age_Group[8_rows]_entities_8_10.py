
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Month': 'January', 'Urban Areas': '15%', 'Rural Areas': '45%', 'Suburban Areas': '40%'},
    {'Month': 'February', 'Urban Areas': '18%', 'Rural Areas': '42%', 'Suburban Areas': '40%'},
    {'Month': 'March', 'Urban Areas': '20%', 'Rural Areas': '35%', 'Suburban Areas': '45%'},
    {'Month': 'April', 'Urban Areas': '25%', 'Rural Areas': '30%', 'Suburban Areas': '45%'},
    {'Month': 'May', 'Urban Areas': '22%', 'Rural Areas': '38%', 'Suburban Areas': '40%'},
    {'Month': 'June', 'Urban Areas': '28%', 'Rural Areas': '27%', 'Suburban Areas': '45%'},
    {'Month': 'July', 'Urban Areas': '30%', 'Rural Areas': '25%', 'Suburban Areas': '45%'},
    {'Month': 'August', 'Urban Areas': '35%', 'Rural Areas': '20%', 'Suburban Areas': '45%'},
    {'Month': 'September', 'Urban Areas': '33%', 'Rural Areas': '22%', 'Suburban Areas': '45%'},
    {'Month': 'October', 'Urban Areas': '29%', 'Rural Areas': '26%', 'Suburban Areas': '45%'},
    {'Month': 'November', 'Urban Areas': '27%', 'Rural Areas': '28%', 'Suburban Areas': '45%'},
    {'Month': 'December', 'Urban Areas': '31%', 'Rural Areas': '24%', 'Suburban Areas': '45%'}
]

df = pd.DataFrame(data)
for col in df.columns[1:]:
    df[col] = df[col].str.rstrip('%').astype('float') / 100

df_long = df.melt(id_vars='Month', var_name='Area Type', value_name='Percentage')

pivot_df = df_long.pivot(index='Month', columns='Area Type', values='Percentage')

colors = ['#FF6347', '#4682B4', '#90EE90']
pivot_df.plot(kind='bar', stacked=True, color=colors, figsize=(12, 8), width=0.8)

plt.title('Monthly Population Distribution by Area Type', pad=20)
plt.xlabel('Month', labelpad=15)
plt.ylabel('Percentage', labelpad=15)
plt.legend(title='Area Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()