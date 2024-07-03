
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
              'August', 'September', 'October', 'November', 'December'],
    'BookSales': [120, 150, 170, 210, 240, 260, 300, 280, 250, 220, 190, 160]
}

df = pd.DataFrame(data)

months_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                'July', 'August', 'September', 'October', 'November', 'December']
df['Month'] = pd.Categorical(df['Month'], categories=months_order, ordered=True)

plt.figure(figsize=(14, 8))
sns.set_theme(style="whitegrid")
ax = sns.lineplot(data=df, x='Month', y='BookSales', color='#4CAF50', lw=2)
ax.fill_between(df.Month, df.BookSales, color='#4CAF50', alpha=0.3)

for line in range(0, df.shape[0]):
     ax.text(df.Month[line], df.BookSales[line], df.BookSales[line], 
             horizontalalignment='center', size='small', color='black', weight='semibold')

ax.set_title('Monthly Book Sales in 2023', fontsize=18, pad=20)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Book Sales', fontsize=14)
ax.set(ylim=(0, None))

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()