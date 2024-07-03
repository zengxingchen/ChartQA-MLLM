
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedFormatter

data = {
    'Year': ['2018', '2019', '2020', '2021', '2022'],
    'International': [35.2, 32.5, 30.1, 28.7, 27.3],
    'Domestic': [45.6, 47.3, 49.2, 50.4, 51.6],
    'Budget': [10.8, 11.4, 12.5, 13.2, 14.1],
    'Independent': [8.4, 8.8, 8.2, 7.7, 7.0]
}
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

df_percentage = df.div(df.sum(axis=1), axis=0) * 100

fig, ax = plt.subplots(figsize=(12, 8))
df_percentage.plot(kind='bar', stacked=True, width=0.8, color=['#8B0000', '#00008B', '#008000', '#FFD700'], ax=ax)

for c in ax.containers:
    labels = [f'{w:.1f}%' for w in c.datavalues]
    ax.bar_label(c, labels=labels, label_type='center')

ax.set_ylabel('Percentage of Movie Releases')
ax.set_xlabel('Year')
ax.set_title('Yearly Movie Releases by Category (2018-2022)', pad=20)
ax.yaxis.set_major_formatter(FixedFormatter(['0%', '20%', '40%', '60%', '80%', '100%']))

plt.xticks(rotation=0)
plt.legend(title='Movie Category', loc='upper left', bbox_to_anchor=(1, 1))
sns.despine(left=True)

plt.tight_layout()
plt.show()