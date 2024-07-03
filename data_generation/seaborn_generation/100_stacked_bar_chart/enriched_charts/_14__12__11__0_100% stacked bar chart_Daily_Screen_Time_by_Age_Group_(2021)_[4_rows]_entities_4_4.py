
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedFormatter

# Creating the dataframe
data = {
    'Year': ['2018', '2019', '2020', '2021', '2022'],
    'Action': [35, 30, 20, 25, 25],
    'Romance': [25, 20, 30, 20, 25],
    'Comedy': [15, 25, 20, 30, 20],
    'Drama': [25, 25, 30, 25, 30]
}
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

# Convert to percentages
df_percentage = df.div(df.sum(axis=1), axis=0) * 100

# Starting the stackplot
fig, ax = plt.subplots(figsize=(12, 10))
df_percentage.plot(kind='bar', stacked=True, width=0.6, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], ax=ax)

# Adding the percentage labels on each bar
for c in ax.containers:
    labels = [f'{w:.1f}%' for w in c.datavalues]
    ax.bar_label(c, labels=labels, label_type='center')

ax.set_ylabel('Percentage of Genre Popularity')
ax.set_xlabel('Year')
ax.set_title('Yearly Distribution of Movie Genre Popularity (2018-2022)', pad=20)
ax.yaxis.set_major_formatter(FixedFormatter(['0%', '20%', '40%', '60%', '80%', '100%']))

plt.xticks(rotation=0)
plt.legend(title='Genre Type', loc='upper right', bbox_to_anchor=(1.3, 1))
sns.despine(left=True)

plt.tight_layout()
plt.show()