
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Month': 'January', 'Books Read': '5', 'Articles Read': '10', 'Papers Read': '2'},
    {'Month': 'February', 'Books Read': '6', 'Articles Read': '12', 'Papers Read': '3'},
    {'Month': 'March', 'Books Read': '7', 'Articles Read': '14', 'Papers Read': '2'},
    {'Month': 'April', 'Books Read': '8', 'Articles Read': '9', 'Papers Read': '4'},
    {'Month': 'May', 'Books Read': '9', 'Articles Read': '11', 'Papers Read': '3'},
    {'Month': 'June', 'Books Read': '10', 'Articles Read': '13', 'Papers Read': '2'},
    {'Month': 'July', 'Books Read': '11', 'Articles Read': '12', 'Papers Read': '4'},
    {'Month': 'August', 'Books Read': '12', 'Articles Read': '15', 'Papers Read': '3'}
]

df = pd.DataFrame(data)
for col in df.columns[1:]:
    df[col] = df[col].astype('float')

df_long = df.melt(id_vars='Month', var_name='Reading Material', value_name='Count')

pivot_df = df_long.pivot(index='Month', columns='Reading Material', values='Count')

colors = ['#FF6F61', '#6B5B95', '#88B04B']
pivot_df.plot(kind='bar', stacked=True, color=colors, figsize=(12, 8), width=0.6)

plt.title('Monthly Reading Habits', pad=20)
plt.xlabel('Month', labelpad=15)
plt.ylabel('Reading Count', labelpad=15)
plt.legend(title='Reading Material', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()