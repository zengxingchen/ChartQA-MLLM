
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Month': 'January', 'Math': '15%', 'Science': '40%', 'Art': '45%'},
    {'Month': 'February', 'Math': '20%', 'Science': '35%', 'Art': '45%'},
    {'Month': 'March', 'Math': '25%', 'Science': '30%', 'Art': '45%'},
    {'Month': 'April', 'Math': '22%', 'Science': '33%', 'Art': '45%'},
    {'Month': 'May', 'Math': '18%', 'Science': '37%', 'Art': '45%'},
    {'Month': 'June', 'Math': '20%', 'Science': '35%', 'Art': '45%'},
    {'Month': 'July', 'Math': '25%', 'Science': '30%', 'Art': '45%'},
    {'Month': 'August', 'Math': '23%', 'Science': '32%', 'Art': '45%'},
    {'Month': 'September', 'Math': '19%', 'Science': '36%', 'Art': '45%'},
    {'Month': 'October', 'Math': '21%', 'Science': '34%', 'Art': '45%'},
    {'Month': 'November', 'Math': '24%', 'Science': '31%', 'Art': '45%'},
    {'Month': 'December', 'Math': '20%', 'Science': '35%', 'Art': '45%'}
]

df = pd.DataFrame(data)
for col in df.columns[1:]:
    df[col] = df[col].str.rstrip('%').astype('float') / 100

df_long = df.melt(id_vars='Month', var_name='Category', value_name='Percentage')

pivot_df = df_long.pivot(index='Month', columns='Category', values='Percentage')

colors = ['#FF6347', '#4682B4', '#32CD32']
pivot_df.plot(kind='bar', stacked=True, color=colors, figsize=(8, 10), width=0.7)

plt.title('Monthly Interest in Education Subjects', pad=20)
plt.xlabel('Month', labelpad=15)
plt.ylabel('Percentage', labelpad=15)
plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()