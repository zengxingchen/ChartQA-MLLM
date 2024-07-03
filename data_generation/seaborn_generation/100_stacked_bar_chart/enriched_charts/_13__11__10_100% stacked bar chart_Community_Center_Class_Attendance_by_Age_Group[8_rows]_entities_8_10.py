
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = [
    {'Month': 'January', 'Philosophy': '20%', 'Ethics': '30%', 'Morality': '50%'},
    {'Month': 'February', 'Philosophy': '25%', 'Ethics': '35%', 'Morality': '40%'},
    {'Month': 'March', 'Philosophy': '22%', 'Ethics': '33%', 'Morality': '45%'},
    {'Month': 'April', 'Philosophy': '30%', 'Ethics': '25%', 'Morality': '45%'},
    {'Month': 'May', 'Philosophy': '27%', 'Ethics': '30%', 'Morality': '43%'},
    {'Month': 'June', 'Philosophy': '35%', 'Ethics': '25%', 'Morality': '40%'},
    {'Month': 'July', 'Philosophy': '33%', 'Ethics': '27%', 'Morality': '40%'},
    {'Month': 'August', 'Philosophy': '30%', 'Ethics': '28%', 'Morality': '42%'},
    {'Month': 'September', 'Philosophy': '28%', 'Ethics': '32%', 'Morality': '40%'},
    {'Month': 'October', 'Philosophy': '26%', 'Ethics': '34%', 'Morality': '40%'},
    {'Month': 'November', 'Philosophy': '29%', 'Ethics': '31%', 'Morality': '40%'},
    {'Month': 'December', 'Philosophy': '31%', 'Ethics': '29%', 'Morality': '40%'}
]

df = pd.DataFrame(data)
for col in df.columns[1:]:
    df[col] = df[col].str.rstrip('%').astype('float') / 100

df_long = df.melt(id_vars='Month', var_name='Category', value_name='Percentage')

pivot_df = df_long.pivot(index='Month', columns='Category', values='Percentage')

colors = ['#6A5ACD', '#FFD700', '#ADFF2F']
pivot_df.plot(kind='bar', stacked=True, color=colors, figsize=(10, 12), width=0.85)

plt.title('Monthly Interest in Philosophy & Ethics Topics', pad=20)
plt.xlabel('Month', labelpad=15)
plt.ylabel('Percentage', labelpad=15)
plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()