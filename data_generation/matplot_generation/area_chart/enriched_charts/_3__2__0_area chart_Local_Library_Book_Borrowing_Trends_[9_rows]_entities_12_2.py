
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
              'August', 'September', 'October', 'November', 'December'],
    'Books_Read': [5, 8, 12, 15, 10, 6, 7, 9, 13, 14, 11, 16]
}

df = pd.DataFrame(data)

months_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                'July', 'August', 'September', 'October', 'November', 'December']
df['Month'] = pd.Categorical(df['Month'], categories=months_order, ordered=True)

plt.figure(figsize=(16, 10))
sns.set_theme(style="whitegrid")
ax = sns.lineplot(data=df, x='Month', y='Books_Read', color='#2E86C1', lw=2)
ax.fill_between(df.Month, df.Books_Read, color='#2E86C1', alpha=0.3)

for line in range(0, df.shape[0]):
     ax.text(df.Month[line], df.Books_Read[line], df.Books_Read[line], 
             horizontalalignment='center', size='small', color='black', weight='semibold')

ax.set_title('Monthly Books Read in 2023', fontsize=18, y=1.03)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Books Read', fontsize=14)
ax.set(ylim=(0, None))

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()