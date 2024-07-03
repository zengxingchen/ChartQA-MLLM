
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedFormatter

# Creating the dataframe
data = {
    'Year': ['2018', '2019', '2020', '2021', '2022'],
    'Books': [60, 58, 55, 52, 50],
    'Magazines': [15, 14, 13, 12, 10],
    'Newspapers': [10, 8, 7, 6, 5],
    'Ebooks': [10, 12, 15, 18, 20],
    'AudioBooks': [5, 8, 10, 12, 15]
}
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

# Convert to percentages
df_percentage = df.div(df.sum(axis=1), axis=0) * 100

# Starting the stackplot
fig, ax = plt.subplots(figsize=(8, 10))
df_percentage.plot(kind='bar', stacked=True, width=0.5, color=['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2'], ax=ax)

# Adding the percentage labels on each bar
for c in ax.containers:
    labels = [f'{w:.1f}%' for w in c.datavalues]
    ax.bar_label(c, labels=labels, label_type='center')

ax.set_ylabel('Percentage of Reading Materials')
ax.set_xlabel('Year')
ax.set_title('Reading Preferences Over the Years (2018-2022)', pad=20)
ax.yaxis.set_major_formatter(FixedFormatter(['0%', '20%', '40%', '60%', '80%', '100%']))

plt.xticks(rotation=0)
plt.legend(title='Reading Material', loc='upper left', bbox_to_anchor=(1, 1))
sns.despine(left=True)

plt.tight_layout()
plt.show()