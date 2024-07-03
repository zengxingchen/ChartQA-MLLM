import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Month': 'January', 'Walking': '40%', 'Cycling': '30%', 'Running': '30%'},
    {'Month': 'February', 'Walking': '42%', 'Cycling': '28%', 'Running': '30%'},
    {'Month': 'March', 'Walking': '38%', 'Cycling': '32%', 'Running': '30%'},
    {'Month': 'April', 'Walking': '41%', 'Cycling': '29%', 'Running': '30%'},
    {'Month': 'May', 'Walking': '39%', 'Cycling': '31%', 'Running': '30%'},
    {'Month': 'June', 'Walking': '43%', 'Cycling': '27%', 'Running': '30%'},
    {'Month': 'July', 'Walking': '40%', 'Cycling': '30%', 'Running': '30%'},
    {'Month': 'August', 'Walking': '41%', 'Cycling': '29%', 'Running': '30%'},
    {'Month': 'September', 'Walking': '39%', 'Cycling': '31%', 'Running': '30%'},
    {'Month': 'October', 'Walking': '42%', 'Cycling': '28%', 'Running': '30%'},
    {'Month': 'November', 'Walking': '40%', 'Cycling': '30%', 'Running': '30%'},
    {'Month': 'December', 'Walking': '43%', 'Cycling': '27%', 'Running': '30%'}
]

df = pd.DataFrame(data)
for col in df.columns[1:]:
    df[col] = df[col].str.rstrip('%').astype('float') / 100

df_long = df.melt(id_vars='Month', var_name='Activity', value_name='Percentage')

pivot_df = df_long.pivot(index='Month', columns='Activity', values='Percentage')

colors = ['#FF6347', '#4682B4', '#32CD32']
pivot_df.plot(kind='bar', stacked=True, color=colors, figsize=(14, 10), width=0.55)

plt.title('Monthly Participation in Outdoor Activities', pad=20)
plt.xlabel('Month', labelpad=15)
plt.ylabel('Percentage', labelpad=15)
plt.legend(title='Activity', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()