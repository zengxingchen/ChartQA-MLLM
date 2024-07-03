
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Month': 'January', 'Soccer': '25%', 'Basketball': '35%', 'Swimming': '40%'},
    {'Month': 'February', 'Soccer': '28%', 'Basketball': '33%', 'Swimming': '39%'},
    {'Month': 'March', 'Soccer': '27%', 'Basketball': '32%', 'Swimming': '41%'},
    {'Month': 'April', 'Soccer': '30%', 'Basketball': '31%', 'Swimming': '39%'},
    {'Month': 'May', 'Soccer': '29%', 'Basketball': '34%', 'Swimming': '37%'},
    {'Month': 'June', 'Soccer': '32%', 'Basketball': '30%', 'Swimming': '38%'},
    {'Month': 'July', 'Soccer': '31%', 'Basketball': '29%', 'Swimming': '40%'},
    {'Month': 'August', 'Soccer': '30%', 'Basketball': '33%', 'Swimming': '37%'},
    {'Month': 'September', 'Soccer': '28%', 'Basketball': '34%', 'Swimming': '38%'},
    {'Month': 'October', 'Soccer': '27%', 'Basketball': '35%', 'Swimming': '38%'},
    {'Month': 'November', 'Soccer': '29%', 'Basketball': '33%', 'Swimming': '38%'},
    {'Month': 'December', 'Soccer': '30%', 'Basketball': '32%', 'Swimming': '38%'}
]

df = pd.DataFrame(data)
for col in df.columns[1:]:
    df[col] = df[col].str.rstrip('%').astype('float') / 100

df_long = df.melt(id_vars='Month', var_name='Sport', value_name='Percentage')

pivot_df = df_long.pivot(index='Month', columns='Sport', values='Percentage')

colors = ['#FFA07A', '#20B2AA', '#778899']
pivot_df.plot(kind='bar', stacked=True, color=colors, figsize=(16, 12), width=0.65)

plt.title('Monthly Participation in Sports Activities', pad=20)
plt.xlabel('Month', labelpad=15)
plt.ylabel('Percentage', labelpad=15)
plt.legend(title='Sport', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()