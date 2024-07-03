
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedFormatter

# Creating the dataframe
data = {
    'Year': ['2018', '2019', '2020', '2021', '2022'],
    'Documentary': [30, 35, 40, 45, 50],
    'Drama': [25, 20, 15, 10, 5],
    'Comedy': [20, 15, 10, 5, 5],
    'Action': [15, 20, 25, 30, 30],
    'Animation': [10, 10, 10, 10, 10]
}
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

# Convert to percentages
df_percentage = df.div(df.sum(axis=1), axis=0) * 100

# Starting the stackplot
fig, ax = plt.subplots(figsize=(10, 8))
df_percentage.plot(kind='bar', stacked=True, width=0.8, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'], ax=ax)

# Adding the percentage labels on each bar
for c in ax.containers:
    labels = [f'{w:.1f}%' for w in c.datavalues]
    ax.bar_label(c, labels=labels, label_type='center')

ax.set_ylabel('Percentage of Movie Genres')
ax.set_xlabel('Year')
ax.set_title('Yearly Distribution of Movie Genres (2018-2022)', pad=20)
ax.yaxis.set_major_formatter(FixedFormatter(['0%', '20%', '40%', '60%', '80%', '100%']))

plt.xticks(rotation=0)
plt.legend(title='Movie Genre', loc='upper left', bbox_to_anchor=(1, 1))
sns.despine(left=True)

plt.tight_layout()
plt.show()